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

### Manage /etc/crontab
You can delete system `/etc/crontab`.  
**Attention**, detecting just by "system-wide crontab" comment, may delete your manual tasks!  
Enable owerwrite: `cron_crontab_tasks_overwrite: yes`, 
then define `cron_crontab_vars` and `cron_crontab_tasks`.
