def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
