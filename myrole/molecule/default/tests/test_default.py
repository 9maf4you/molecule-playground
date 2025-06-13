"""Role testing files using testinfra."""

def test_unbound_installed(host):
    """Validate unbound installation."""
    package = host.package("unbound")

    assert package.is_installed


def test_file_unbond_config_present(host):
    """Validate unbound configuration file presence."""
    file = host.file("/etc/unbound/unbound.conf")

    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"

