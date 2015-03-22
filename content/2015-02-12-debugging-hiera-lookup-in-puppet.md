Title: Debugging hiera lookup in puppet
Date: 2015-02-12 23:20
Modified: 2015-02-12 23:20
Category: puppet
Tags: puppet, hiera
Slug: debugging-hiera-lookup
Authors: Ramz
Summary: A brief idea about how to debug hiera lookup in puppet

The best way to debug hiera lookup is to

        puppet master --debug --compile yournode.example.com | grep hiera

This will show all the logs where the puppet is looking for a key/value in hierarchy of files.

Tips:
    If you see that the puppet is looking for a file and even though it is present puppet is not able to find it
    it is because of the file permissions. Check the file permissions
