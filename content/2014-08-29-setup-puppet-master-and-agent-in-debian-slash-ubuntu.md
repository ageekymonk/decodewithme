Title: Setup Puppet Master & Agent in debian/ubuntu
Date: 2014-08-29 09:28:49
Modified: 2014-08-29 09:28:49
Category: Tools
Tags: puppet
Slug: setup-puppet-master-and-agent
Authors: Ramz
Summary: A Tutorial to quickly setup puppet master and agent

1. Configure repository on Debian and Ubuntu

    a. Based on the version of Debian or Ubuntu, download the deb file. It follows the convention puppetlabs-release-\<CODE NAME>.deb
    
    
        For Ubuntu 12.04, use
            
            wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
            
        For Ubuntu 14.04, use
                
            wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
                
        For Debian 7.4, use
                
            wget https://apt.puppetlabs.com/puppetlabs-release-wheezy.deb
                
    
    b. Install the deb file downloaded
            
            sudo apt-get update
            sudo dpkg -i puppetlabs-release-precise.deb
            
2. Install Puppet master on the server

        sudo apt-get install puppetmaster
        
        
3. Install Puppet Agent/Client on the clients
    
        sudo apt-get install puppet
        
4. With the installation the puppet master should be already running. Or start the master using 

        sudo puppet master 
        
5. To connect the Agent or client with the puppet master

        sudo puppet agent --server <server-name> --waitforcert 60 --test
        
6. The Agent waits for the puppet master to authorize it. In the Puppet master

        sudo puppet cert list
        
   This will list the clients which are not authorized. To authorize it
   
        sudo puppet cert sign <client-name>
        

Now you are good to go. 
        