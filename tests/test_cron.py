import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_crontab_file(Command):
    c = Command('crontab -l').stdout
    assert 'MAIL=mail@example.com' in c
    assert '#Ansible: log env' in c
    assert '1 * * * * env > /tmp' in c
