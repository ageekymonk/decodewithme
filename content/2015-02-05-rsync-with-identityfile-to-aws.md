Title: Rsync wtih Identity File to EC2 Machine
Date: 2015-02-05 17:46:37
Modified: 2015-02-05 17:46:37
Category: Tools
Tags: code, rsync
Slug: rsync-with-identity-file-to-ec2-machine
Authors: Ramz
Summary: One Liner to use rsync with Identity File to Ec2 Machine

To rsync the local folder to EC2 Machine with Identity file is by using the following command

        rsync -rave ‘ssh -i somekey.pem’ /home/local/somefolder ec2user@somehost:/home/ec2/remotefolder


