from ..shared import *


def test_update_alternatives(host):
    cmds = ['/usr/bin/java -version']
    expected = 'OpenJDK'
    check_run_for_rc_and_result(
        cmds, expected, host, check_stderr=True, as_interactive=False)

    java_parent_dir = '/home/jenkins/.sdkman/candidates/java/.*/bin'

    cmds = ['readlink -f /usr/bin/java']
    expected = java_parent_dir + '/java'
    check_run_for_rc_and_result(cmds, expected, host, regex_match=True)

    cmds = ['/usr/bin/javac -version']
    expected = 'javac'
    check_run_for_rc_and_result(
        cmds, expected, host, check_stderr=False, as_interactive=False)

    cmds = ['readlink -f /usr/bin/javac']
    expected = java_parent_dir + '/javac'
    check_run_for_rc_and_result(cmds, expected, host, regex_match=True)
