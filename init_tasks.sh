#!/bin/bash

# Gives a personalised greeting
# Upgrades pip
# Author: Matt Rudge

echo "Setting the greeting"
sed -i "s/USER_NAME/$GITPOD_GIT_USER_NAME/g" ${GITPOD_REPO_ROOT}/README.md
echo "Checking for pip upgrade"
pip3 install --upgrade pip
echo "Done"
rm $GITPOD_REPO_ROOT/.gitpod*
rm $GITPOD_REPO_ROOT/init_tasks.sh
