import os
import pytest
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def ansible_defaults():
    with open('playbook-vars.yml', 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize('package', ansible_defaults()['mosquitto_packages'])
def test_mosquitto_packages(host, package):
    assert host.package(package).is_installed


@pytest.mark.parametrize('python_package',
                         ansible_defaults()['mosquitto_python_packages'])
def test_mosquitto_python_packages(host, python_package):
    assert python_package in host.pip_package.get_packages().keys()


def test_mosquitto_user_exists(host, ansible_defaults):
    u = host.user(ansible_defaults['mosquitto_user'])

    assert u.exists
    assert u.group == ansible_defaults['mosquitto_group']
    assert u.home == ansible_defaults['mosquitto_home']


def test_mosquitto_group_exists(host, ansible_defaults):
    assert host.group(ansible_defaults['mosquitto_group']).exists


@pytest.mark.parametrize('mosquitto_group',
                         ansible_defaults()['mosquitto_add_groups'])
def test_mosquitto_add_groups(host, ansible_defaults, mosquitto_group):
    u = host.user(ansible_defaults['mosquitto_user'])

    assert mosquitto_group in u.groups


def test_mosquitto_service(host):
    assert host.service('mosquitto').is_enabled
    assert host.service('mosquitto').is_running
