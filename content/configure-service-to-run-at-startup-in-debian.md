Title: Configure service to run at startup in Debian
Date: 2014-06-23 15:20:45
Modified: 2014-06-23 15:20:45
Category: Tools
Tags: debian, configs
Slug: configure-service-to-run-at-startup-in-debian
Authors: Ramz
Summary: Commands to run service at startup in debian

1. To configure a service say squid to run at startup

        update-rc.d squid3 defaults

2. To Remove a service which is running at startup

        updatd-rc.d -f squid3 remove