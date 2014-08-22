#!/usr/bin/env bash

apt-get update -y

echo "Install system packages"
apt-get install -y build-essential python-pip python-dev mc git

echo "Install nodejs"
apt-get install -y nodejs

# Dependencies for virtualenv
apt-get install -y libjpeg8 libjpeg8-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev libxml2-dev libxslt1-dev libssl-dev swig

echo "Setup pip and virtualenv"
pip install virtualenv
pip install virtualenvwrapper
pip install envdir
