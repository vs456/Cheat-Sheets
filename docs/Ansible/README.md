# Format of Ansible inventory file:

```yaml
leafs:
  hosts:
    leaf01:
      ansible_host: 192.0.2.100
      http_port: 80
    leaf02:
      ansible_host: 192.0.2.110

spines:
  hosts:
    spine01:
      ansible_host: 192.0.2.120
      http_port: 80
    spine02:
      ansible_host: 192.0.2.130
      http_port: 80

network:
  children:
    leafs:
    spines:

webservers:
  hosts:
    webserver01:
      ansible_host: 192.0.2.140
      http_port: 80
    webserver02:
      ansible_host: 192.0.2.150
      http_port: 80
  vars:
    ansible_user: my_server_user

datacenter:
  children:
    network:
    webservers:
```

# Ansible CLI Cheat Sheet
https://docs.ansible.com/ansible/latest/command_guide/cheatsheet.html