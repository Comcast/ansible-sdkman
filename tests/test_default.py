sdkman_dir = '/home/jenkins/.sdkman'


def script_wrap(cmds):
    sdk_init_tmpl = 'export SDKMAN_DIR={0} && source {0}/bin/sdkman-init.sh'
    sdk_init = sdk_init_tmpl.format(sdkman_dir)
    result_cmds = [sdk_init] + cmds
    return "/bin/bash -c '{0}'".format('; '.join(result_cmds))


def check_run_for_rc_and_result(cmds, expected, host, check_stderr=False):
    result = host.run(script_wrap(cmds))
    assert result.rc == 0
    if check_stderr:
        assert result.stderr.find(expected) != -1
    else:
        assert result.stdout.find(expected) != -1


def test_config_file(host):
    f = host.file(sdkman_dir + '/etc/config')
    assert f.exists
    assert f.is_file
    assert f.mode in [0o644, 0o654, 0o655]
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.contains('sdkman_auto_answer=true')


def test_gradle_installed(host):
    cmds = ['gradle --version']
    expected = 'Gradle 4.6'
    check_run_for_rc_and_result(cmds, expected, host)


def test_other_gradle_installed(host):
    cmds = ['sdk use gradle 3.5.1', 'gradle --version']
    expected = 'Gradle 3.5.1'
    check_run_for_rc_and_result(cmds, expected, host)


def test_offline(host):
    cmds = ['sdk list gradle']
    expected = 'Offline: only showing installed gradle versions'
    check_run_for_rc_and_result(cmds, expected, host)
