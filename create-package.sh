#!/usr/bin/env bash

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")

set -e

clear

ansible-playbook -vv -i $SCRIPT_DIR/inventory.yaml $SCRIPT_DIR/operations/create-package/01-create-package/playbook.yaml