Title: sync your folder with remote machine continuously
Date: 2014-06-13 14:20
Modified: 2014-06-13 14:20
Category: Snippets
Tags: Python, rsync, snippets, watchmedo
Slug: sync-your-folder-with-remote-machine-continuously
Authors: Ramz
Summary: A snippet using watchmedo python library to automatically syncing a local folder with remote on changing the local folder

I make code changes locally. And i need to put it in remote machine to test it. For doing so i needed to run rsync manually every time.
To avoid this

1. Install watchdog.

        pip install watchdog

2. Setup passwordless login for your ssh. Follow the steps specified in [this site](http://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/)


3. Run the following command to sync your current folder to remote machine.

        watchmedo shell-command --patterns="*" --recursive --command 'rsync -avz . -e ssh private@private:privateFolder'

Voila ... Its done.
