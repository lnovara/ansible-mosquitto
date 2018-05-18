Ansible Role: Mosquitto
=========

[![Build Status](https://travis-ci.com/lnovara/ansible-mosquitto.svg?branch=master)](https://travis-ci.com/lnovara/ansible-mosquitto)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-lnovara.mosquitto-blue.svg)](https://galaxy.ansible.com/lnovara/mosquitto)

Install and configure [Mosquitto](https://mosquitto.org/) MQTT message broker.

Requirements
------------

An Ansible 2.2 or higher installation.

Role Variables
--------------

Available variables are listed below, along with default values (see
`defaults/main.yml`).

    mosquitto_packages:
      - mosquitto
      - mosquitto-clients

Packages to install for Mosquitto.

    mosquitto_python_packages:
      - paho-mqtt

Python packages to install for Mosquitto.

    mosquitto_user: mosquitto
    mosquitto_group: mosquitto

Mosquitto system user and group.

    mosquitto_home: /var/lib/mosquitto

Mosquitto user home directory.

    mosquitto_add_groups: []

Additional groups for Mosquitto user.

    mosquitto_config_file: /etc/mosquitto/mosquitto.conf

Path to Mosquitto configuration file

    mosquitto_config: {}

Dictionary holding Mosquitto configuration. The complete Mosquitto configuration
reference can be found
[here](https://mosquitto.org/man/mosquitto-conf-5.html).<br/>
**NOTE**: the provided Mosquitto configuration will be merged with the default
one defined in `vars/main.yml`.

    mosquitto_listeners: []

Example:

    mosquitto_listeners:
      - listener: "1883 localhost"
        protocol: mqtt
        use_username_as_clientid: true

List holding Mosquitto listeners configuration.

    mosquitto_bridges: []

Example:

    mosquitto_bridges:
      - connection: bridge_name
        address: exmaple.com:1883

List holding Mosquitto bridges configuration.

    mosquitto_auth_anonymous: []

    mosquitto_auth_users: []

    mosquitto_auth_patterns: []

Examples:

    mosquitto_auth_anonymous:
      - "topic read topic_name"

    mosquitto_auth_users:
      - name: user_name
        state: present
        psk: zfEGZkTMPOhxNBTe # Optional. Needs mosquitto_config.psk_file set.
        acl:
          - "topic read topic1_name"
          - "topic readwrite topic2_name"

    mosquitto_auth_patterns:
      - "pattern write $SYS/broker/connection/%c/state"

Lists holding Mosquitto ACLs.

Dependencies
------------

None.

Example Playbook
----------------

    - name: Install and configure Mosquitto on all hosts.
      hosts: all
      roles:
         - lnovara.mosquitto

Testing
-------

This role uses [molecule](https://molecule.readthedocs.io/en/latest/) to
implement automatic testing of its functionalities.

To execute the tests

```bash
pip install tox

git clone https://github.com/lnovara/ansible-mosquitto.git

cd ansible-mosquitto

# test all the scenarios
tox
```

License
-------

MIT

Author Information
------------------

Luca Novara
