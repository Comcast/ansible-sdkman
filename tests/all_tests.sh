#!/bin/bash

set -e
WORKSPACE=$(git rev-parse --show-toplevel)
rm -rf "${WORKSPACE}/.venv"
virtualenv --python=$(which python2.7) "${WORKSPACE}/.venv"
source "${WORKSPACE}/.venv/bin/activate"
pip install -U pip
pip install --no-deps -r "${WORKSPACE}/test-requirements.txt"

cd "${WORKSPACE}"
molecule create --platform fedora/25
ssh -p 2222 -l vagrant \
    -i ${WORKSPACE}/.vagrant/machines/ansible-sdkman/virtualbox/private_key \
    127.0.0.1 'sudo yum install -y python'
molecule converge --platform fedora/25
molecule idempotence --platform fedora/25
molecule verify --platform fedora/25
molecule destroy --platform fedora/25

for platform in centos/7 centos/6 fedora/24 xenial trusty jessie wheezy
do
  molecule test --platform ${platform}
done
deactivate
