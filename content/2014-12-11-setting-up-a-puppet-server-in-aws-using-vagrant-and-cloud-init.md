Title: Setting up a Puppet master in aws using Vagrant and cloud init
Date: 2014-12-11 20:50:52
Modified: 2014-12-11 20:50:52
Category: Snippets
Tags: ruby
Slug: setting-up-a-puppet-master-in-aws-using-vagrant
Authors: Ramz
Summary: A snippet to create a Puppet Master in aws using Vagrant and Cloud init

Vagrant provides an elegant way to bring up a EC2 Instance in aws. Cloud init provides
an easy way to configure the aws instance.

Below is the sample template to bring up a EC2 instance with puppet installed. The ami
being used is ubuntu 14.04.

To bring up and ssh to the instance use the following commands.

```
    vagrant up puppet --provider=aws
    vagrant ssh puppet
```


[gist:id=a3632cae54cc98855cea]
