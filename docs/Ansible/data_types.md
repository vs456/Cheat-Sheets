### String operations

1. Add quotes

    ```yaml
    - name: Run a shell command
      ansible.builtin.shell: echo {{ string_value | quote }}
    ```

2. Concatenate and split strings

    ```yaml
    {{ list | join(" ") }} # Concatenate a list
    {{ list | split }} # Split into a list
    ```

3. Encoding and decoding to base64

    ```yaml
    {{ encoded | b64decode(encoding='utf-16-le') }}
    {{ decoded | string | b64encode(encoding='utf-16-le') }}     # Encoding parameter is optional
    ```

### Dictionaries

```yaml
vars:
  hosts:
    testhost1: 127.0.0.2
    testhost2: 127.0.0.3
tasks:
  - debug:
      msg: '{{ item }}'
    loop: "{{ hosts.items() | list }}"
    loop: "{{ hosts.keys() | list }}"
    loop: "{{ hosts.values() | list }}"
```

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

```yaml
{{ some_variable | to_json }}
{{ some_variable | to_nice_yaml(indent=8, width=1337) }}

both indent and width can be used with to_json as well.
Width: used to increase the width, as python by default inserts a newline after 80 characters.
```

##### [All operations for the variables can be viewed here](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#handling-undefined-variables)

### Handling Filenames

1. Get the filename

    ```yaml
    {{ path | basename }}
    ```

2. Get directory name

    ```yaml
    {{ path | dirname }}
    ```

3. Get relative path

    ```yaml
    {{ path | relpath('/etc') }}
    ```

4. Get rootfilename and extension

    ```yaml
    # with path == 'nginx.conf' the return would be 'nginx'
    {{ path | splitext | first }}

    # with path == 'nginx.conf' the return would be '.conf'
    {{ path | splitext | last }}
    ```

### Datetimes

1. Get datetime objects

    ```yaml
    # Get the total amount of seconds between two dates. Default date format is %Y-%m-%d %H:%M:%S but you can pass your own format
    {{ (("2016-08-14 20:00:12" | to_datetime) - ("2015-12-25" | to_datetime('%Y-%m-%d'))).total_seconds()  }}

    # Get remaining seconds after delta has been calculated. NOTE: This does NOT convert years, days, hours, and so on to seconds. For that, use total_seconds()
    {{ (("2016-08-14 20:00:12" | to_datetime) - ("2016-08-14 18:00:00" | to_datetime)).seconds  }}
    # This expression evaluates to "12" and not "132". Delta is 2 hours, 12 seconds

    # get amount of days between two dates. This returns only the number of days and discards remaining hours, minutes, and seconds
    {{ (("2016-08-14 20:00:12" | to_datetime) - ("2015-12-25" | to_datetime('%Y-%m-%d'))).days  }}
    ```

2. Get current time

```yaml
"Current time (UTC): {{ now(utc=true,fmt='%Y-%m-%d %H:%M:%S') }}"
```

### k8 resources

1. Get resource names

    ```yaml
    {{ configmap_resource_definition | kubernetes.core.k8s_config_resource_name }}
    ```

    for the below code

    ```yaml
    my_secret:
      kind: Secret
      metadata:
        name: my_secret_name

    deployment_resource:
      kind: Deployment
      spec:
        template:
          spec:
            containers:
            - envFrom:
                - secretRef:
                    name: {{ my_secret | kubernetes.core.k8s_config_resource_name }}
    ```

### Lookups

Lookups can be used to do lookups in a file

```yaml
vars:
  motd_value: "{{ lookup('file', '/etc/motd') }}"
tasks:
  - debug:
      msg: "motd value is {{ motd_value }}"
```
