
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky", "almalinux"]
    assert host.system_info.arch == 'x86_64' 

def test_logrotate_config(host):
    logrotate_config = host.file("/etc/logrotate.conf")
    assert logrotate_config.user == "root"
    assert logrotate_config.group == "root" 
    assert logrotate_config.mode == 0o644

def test_logrotate_installed(host):
    logrotate = host.package("logrotate")
    assert logrotate.is_installed
