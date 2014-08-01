#!/usr/bin/env bash

echo "Create virtualenv"
mkdir /home/vagrant/envs
export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv vagrant

cp -p /vagrant/provisioning/conf/.bashrc /home/vagrnat/.bashrc

echo "Finished!"
echo "Please run 'vagrant ssh' to ssh to dev machine"
