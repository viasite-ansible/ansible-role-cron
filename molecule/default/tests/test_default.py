import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_crontab_file(host):
    c = host.command('crontab -l').stdout
    assert 'MAIL=mail@example.com' in c
    assert '#Ansible: log env' in c
    assert '1 * * * * env > /tmp' in c
