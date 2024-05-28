### Forcing a data type conversion

The below code forces the string entered to be converted to boolean.
```yaml
- ansible.builtin.debug:
     msg: test
  when: some_string_value | bool
```

The below code converts to release version to an integer, and then checks the same.
```yaml
- shell: echo "only on Red Hat 6, derivatives, and later"
  when: ansible_facts['os_family'] == "RedHat" and ansible_facts['lsb']['major_release'] | int >= 6
```

### Formatting data to json/yaml

```
{{ some_variable | to_json }}
{{ some_variable | to_yaml }}
```

