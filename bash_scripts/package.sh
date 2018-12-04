#!/bin/bash
sudo apt-get update &&

sudo apt-get install --assume-yes python-bottle &&

sudo apt-get install --assume-yes python-pip python-dev build-essential &&

sudo pip install --upgrade pip &&
sudo pip install --upgrade virtualenv &&

sudo pip2 install httplib2 --upgrade &&

sudo pip3 install httplib2 --upgrade &&

sudo -H pip install --upgrade oauth2client &&
sudo -H pip install --upgrade google-api-python-client &&

sudo -H pip install beaker &&

sudo -H pip install requests &&

sudo apt-get install -y python3-bs4 &&

sudo apt-get install --assume-yes python-numpy &&
sudo -H pip install --upgrade numpy &&

sudo apt-get update &&
sudo apt-get install --assume-yes python-bottle &&
sudo apt-get install --assume-yes python3.6 &&
