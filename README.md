[![build status](http://git.viasite.ru/ansible/ansible-role-cron/badges/master/build.svg)](http://git.viasite.ru/ansible/ansible-role-cron/commits/master)

## Usage
Place role call to meta/main.yml:
```
dependencies:
  - { role: cron, cron_tasks: "{{backups_mysql_cron_tasks}}" }
```

Or you can include role as task from Ansible 2.2:
```
- name: Add cron tasks
  include_role:
    name: cron
  vars:
    cron_tasks: "{{backups_mysql_cron_tasks}}"
```
