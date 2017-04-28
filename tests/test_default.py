import re

sdkman_dir = '/usr/local/sdkman'
shell_header = "/bin/bash -c 'export SDKMAN_DIR=" + sdkman_dir + '\n'
shell_header += 'source ' + sdkman_dir + '/bin/sdkman-init.sh\n'


def test_config_file(host):
    f = host.file(sdkman_dir + '/etc/config')
    setup = host.ansible("setup")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o644
    assert f.user == setup['ansible_facts']['ansible_user_id']
    assert f.gid == setup['ansible_facts']['ansible_effective_group_id']
    assert f.contains('sdkman_auto_answer=true\n')


def test_java_installed(host):
    cmd = 'java -version\n'
    script = shell_header + cmd
    result = host.run(script + "'")
    expected = '^java version "1.8.0_131"$'
    assert result.rc == 0
    assert re.match(expected, result.stderr.split('\n')[0])


def test_mvn_installed(host):
    cmd = 'mvn --version\n'
    script = shell_header + cmd
    result = host.run(script + "'")
    expected = '^Apache Maven 3\.3\.9.*$'
    assert result.rc == 0
    assert re.match(expected, result.stdout.split('\n')[0])


def test_other_mvn_installed(host):
    cmd = 'mvn --version\n'
    script = shell_header + 'sdk use maven 3.5.0\n' + cmd
    result = host.run(script + "'")
    expected = 'Apache Maven 3.5.0'
    assert result.rc == 0
    assert result.stdout.find(expected) != -1


def test_gradle_installed(host):
    cmd = 'gradle --version\n'
    script = shell_header + cmd
    result = host.run(script + "'")
    expected = 'Gradle 3.5'
    assert result.rc == 0
    assert result.stdout.find(expected) != -1


def test_other_gradle_installed(host):
    cmd = 'gradle --version\n'
    script = shell_header + 'sdk use gradle 2.14.1\n' + cmd
    result = host.run(script + "'")
    expected = 'Gradle 2.14.1'
    assert result.rc == 0
    assert result.stdout.find(expected) != -1
