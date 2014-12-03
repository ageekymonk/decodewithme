Title: Increasing number of Arp entries in Arp Table
Date: 2014-06-15 15:20
Modified: 2014-06-15 15:20
Category: Snippets
Tags: Arp, Linux
Slug: increasing-max-arp-entries
Authors: Ramz
Summary: A configuration snippet to increase the max number of arp entries


Sometimes during testing you want to add lot of arp entries statically in the arp table. By default, linux is configured
to have entries upto 128. If you want to change that you can do it by adding these three lines in your **/etc/sysctl.conf** file.
These changes will be retained across reboot.

To increase it to 1024 entries. 


        net.ipv4.neigh.default.gc_thresh3 = 1024
        net.ipv4.neigh.default.gc_thresh2 = 1024
        net.ipv4.neigh.default.gc_thresh1 = 1024


If you need to do it on a live system, run the following commands. 


        sysctl -w net.ipv4.neigh.default.gc_thresh3=1024
        sysctl -w net.ipv4.neigh.default.gc_thresh2=1024
        sysctl -w net.ipv4.neigh.default.gc_thresh1=1024
        
      