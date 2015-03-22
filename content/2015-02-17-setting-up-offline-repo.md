Title: Setting up an offline repository in Debian
Date: 2015-02-17 09:20
Modified: 2015-02-17 09:20
Category: debian
Tags: debian, repository
Slug: setting-up-offline-repository
Authors: Ramz
Summary: Steps to setup an offline repository in Debian

Below are the steps to setup an offline repository in debian which can be used to serve custom packages for the system.

1. Create a directory for storing all the deb files.

        sudo mkdir /opt/repo

2. Copy all the deb files to the directory created

3. scan the directory to create the Packages file.

        cd /opt/repo
        sudo dpkg-scanpackages . /dev/null > Packages

4. Add the local repository to the sources. Be a root while doing this.

        echo "deb file:/opt/repo ./" > /etc/apt/sources.list.d/localrepo.list

5. Update the packages

        sudo apt-get update


    Now all your custom packages should be available. Now you should be able to install them using apt-get install xxx.
    