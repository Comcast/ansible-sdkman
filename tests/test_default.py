sdkman_dir = '/usr/local/sdkman'


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
    setup = host.ansible("setup")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o644
    assert f.user == setup['ansible_facts']['ansible_user_id']
    assert f.gid == setup['ansible_facts']['ansible_user_gid']
    assert f.contains('sdkman_auto_answer=true')


def test_gradle_installed(host):
    cmds = ['gradle --version']
    expected = 'Gradle 4.6'
    check_run_for_rc_and_result(cmds, expected, host)


def test_other_gradle_installed(host):
    cmds = ['sdk use gradle 3.5.1', 'gradle --version']
    expected = 'Gradle 3.5.1'
    check_run_for_rc_and_result(cmds, expected, host)
