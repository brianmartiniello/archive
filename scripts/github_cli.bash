#!/bin/bash

type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update && sudo apt install gh -y
sudo apt update
sudo apt install gh
sudo apt upgrade

gh auth login
#? What account do you want to log into? GitHub.com
#? What is your preferred protocol for Git operations on this host? HTTPS
#? Authenticate Git with your GitHub credentials? Yes
#? How would you like to authenticate GitHub CLI? Login with a web browser

#! First copy your one-time code: B076-62CD
#Press Enter to open github.com in your browser...
