Title: CoovaChilli: Setting up MAC Based Authentication
Date: 2014-06-15 15:20
Modified: 2014-06-15 15:20
Category: Snippets
Tags: coovachilli, mac authentication
Slug: coovachilli-mac-based-authentication
Authors: Ramz
Summary: A brief tutorial to configure coovachilli to support MAC Based Authentication


Coovachilli supports MAC Based authentication. It supports static list which could be configured at start time.

 System Configuration:

OS                : Ubuntu 13.10

Coovachilli  : 1.3.1

Edit the configuration file in location /etc/chilli/defaults 

                   HS_MACAUTHMODE=local

                   HS_MACALLOW="00-11-22-33-44-55" 

Change the mac address with your required ones.

If you want to add multiple mac address, separate them by commas.

    HS_MACALLOW="00-11-22-33-44-55, 22-22-22-22-22-22"

