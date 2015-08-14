Title: Bootstrap openwrt or any dev env with puppet and vagrant in osx
Date: 2015-03-03 20:50:52
Modified: 2014-12-11 20:50:52
Category: Snippets
Tags: python
Slug: bootstrap-openwrt-dev-env-with-puppet
Authors: Ramz
Summary: A tutorial to setup openwrt or any development env with puppet

If you wan to create your dev environment then this is how to use puppet to do it.
Here i am taking the example of creating an openwrt development environment

Developing openwrt in osx natively is not possible. To aid with it we can create a vagrant box
with linux as guest OS and try to do the development in the vagrant box. If you want to automate
the creation of the openwrt env in the box, we can use puppet to do that.

1. Create a vagrant box. Do vagrant init and edit the Vagrantfile with the following content.

        # -*- mode: ruby -*-
        # vi: set ft=ruby :

        unless Vagrant.has_plugin?("vagrant-vbguest")
          raise 'vagrant-vbguest is not installed!. Run "vagrant plugin install vagrant-vbguest"'
        end

        # Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
        VAGRANTFILE_API_VERSION = "2"

        Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
          # All Vagrant configuration is done here. The most common configuration
          # options are documented and commented below. For a complete reference,
          # please see the online documentation at vagrantup.com.

          config.vm.define "openwrtdev" do |skyos|
            skyos.vm.box = "ubuntu/trusty64"

            # We have an additional Public network so that we can flash the openmesh device
            skyos.vm.network "public_network"

            skyos.vm.provider "virtualbox" do |vb|
              vb.customize ["modifyvm", :id, "--memory", "1024", "--nicpromisc2", "allow-all"]
            end

            skyos.vm.provision "puppet" do |puppet|
              puppet.manifests_path = "devel-infra/manifests"
              puppet.module_path = "devel-infra/modules"
              puppet.manifest_file = "default.pp"
              puppet.facter = {
                  'hw' => ENV.has_key?('HW') ? ENV['HW'] : 'om2p'
              }
            end

            skyos.vm.synced_folder ".", "/home/vagrant/Projects/skyos", id: "vagrant-root",
                owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=775"]
          end

        end

2. Create a manifest file default.pp, with puppet action to be done on the created vagrant box. Here, i am
   installing the required softwares, checkingout code, performing build.
   You can change the name and path in the Vagrantfile.


        # Install all the relevant Packages
        package { ["git", "unzip", "build-essential", "subversion", "gawk", "libncurses5-dev", "libssl-dev", "zlib1g-dev", "dnsmasq"]:
          ensure => present
        }

        # Need to change the home location
        file { ["/home/vagrant/Projects", "/home/vagrant/Projects/build", "/home/vagrant/Projects/build/openwrt"]:
          owner => vagrant,
          group => vagrant,
          ensure => directory
        }

        vcsrepo { "/home/vagrant/Projects/build/openwrt":
          owner => vagrant,
          group => vagrant,
          ensure   => present,
          provider => git,
          source   => "git://git.openwrt.org/14.07/openwrt.git",
        }


        file { "/home/vagrant/Projects/build/openwrt/.config":
          owner => vagrant,
          group => vagrant,
          mode => 644,
          ensure => file,
          source => "somelocation/.config"
        }

        exec { "feeds_update":
          command     => "/home/vagrant/Projects/build/openwrt/scripts/feeds update",
          require => File['/home/vagrant/Projects/build/openwrt/.config']
        }

        exec { "pkg_install":
          command     => "/home/vagrant/Projects/build/openwrt/scripts/feeds install monit coova-chilli libconfig luci",
          require => Exec['feeds_update']
        }


        exec { "make":
            command => "make",
            require => Exec["pkg_install"]
        }

3. All the relevant modules needs to be checked out at a location and the path to be provided in Vagrantfile.

4. ```vagrant up openwrtdev``` to start the vagrant box and puppet & vagrant will take care of the rest to setup for you.

Thats all Folks. This is how we can bootstrap your dev environment in osx using puppet and vagrant.
