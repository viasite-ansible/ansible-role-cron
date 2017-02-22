[![Build Status](https://travis-ci.org/viasite-ansible/ansible-role-cron.svg?branch=master)](https://travis-ci.org/viasite-ansible/ansible-role-cron)

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
