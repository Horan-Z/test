#!/usr/bin/env bash
set -e

clear

ansible-playbook -vv -i inventory.yaml operations/create-package/01-create-package/playbook.yaml