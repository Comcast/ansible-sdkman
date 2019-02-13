sdkman_user = 'jenkins'
sdkman_group = 'jenkins'


def script_wrap(host, cmds):
    # run as interactive shell to ensure .bashrc is sourced
    wrapped_cmd = "/bin/bash -i -c '{0}'".format('; '.join(cmds))

    if host.user.name == sdkman_user:
        return wrapped_cmd
    else:
        return "sudo -H -u {0} {1}".format(sdkman_user, wrapped_cmd)


def check_run_for_rc_and_result(cmds, expected, host, check_stderr=False):
    result = host.run(script_wrap(host, cmds))
    assert result.rc == 0
    if check_stderr:
        assert result.stderr.find(expected) != -1
    else:
        assert result.stdout.find(expected) != -1


def test_config_file(host):
    result = host.run(script_wrap(host, ['echo $SDKMAN_DIR']))
    config_file_path = "{0}/etc/config".format(result.stdout)

    f = host.file(config_file_path)
    assert f.exists
    assert f.is_file
    assert f.mode in [0o644, 0o654, 0o655]
    assert f.user == sdkman_user
    assert f.group == sdkman_group
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

    cmds = ['sdk offline disable', 'sdk list gradle']
    expected = 'Available Gradle Versions'
    check_run_for_rc_and_result(cmds, expected, host)
