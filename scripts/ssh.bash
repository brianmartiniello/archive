#!/bin/bash

sudo systemctl start ssh
sudo geany /etc/ssh/sshd_config -> Uncomment 'PubkeyAuthentication yes'
sudo systemctl enable ssh
sudo systemctl restart ssh
sudo reboot
sudo systemctl status ssh
