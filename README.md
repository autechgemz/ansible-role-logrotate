# Ansible Role: logrotate

## Description

Manage system logs rotate system.

## Requirements

None

## Dependencies

None

## OS Platforms

- Debian family
- RedHat family

## Example Playbook

```
- hosts: all
  roles:
    - logrotate
```

## Role Variables

### logrotate_debug: (bool)

```
logrotate_debug: false
```

### logrotate_package_ensure: (string)

```
logrotate_package_ensure: 'present'
```

### logrotate_global_config_options: (list)

```
logrotate_global_config_options: []
```

### logrotate_dropin_config_purge: (bool)

```
logrotate_dropin_config_purge: false
```

### logrotate_dropin_config_options: (list)

```
logrotate_dropin_config_options: []
```

## Example vars

```
logrotate_global_config_options:
  - 'weekly'
  - 'su root adm'
  - 'rotate 4'
  - 'create'
  - 'include /etc/logrotate.d'

logrotate_dropin_config_options:
  - name: typesystem
    state: present
    targets:
      - '/var/log/test*.log'
      - '/var/log/typesystem*.log'
    options:
      - 'su root root'
      - 'create 0644 root root'
      - 'rotate 32'
      - 'monthly'
      - 'compress'
      - 'delaycompress'
      - 'missingok'
      - 'notifempty'
```