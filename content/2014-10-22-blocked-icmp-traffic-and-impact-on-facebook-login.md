Title: Blocked ICMP Traffic and its impact on Facebook Login
Date: 2014-10-22 15:19
Modified: 2014-10-22 15:19
Category: Tools
Tags: Debug, ICMP
Slug: blocked-icmp-traffic-and-impact-on-facebook-login
Authors: Ramz
Summary: Debugging Facebook Login not working on some Android Phones


Recently I encountered a bug, where on some android phones, passing through my server, facebook login did not work. 
But if you clear the cache it works fine. 
 
Step 1: 
    I ran tcpdump and saw that i am not getting any response at all.
     
Step 2: 
    I opened up all the firewall rules. Now it started working. 
    
Step 3: 
    On tcpdump i saw that the packet size is near the 1500 boundary. It seemed like that larger the packet we are seeing the issue in some android phones. 
Comparing the android phones, i saw that when there is no response for a particular packet size, some android versions 
send with other packet size which is less and it works. This confirmed that the issue is with the packet size 
 
Step 4:
    Ran the tracepath command to see what is the maximum mtu. Found some routers in between has smaller mtu and it sends an icmp response, 
    but since i was blocking the icmp the response does not reach causing facebook login to fail. 
    
        tracepath --mtu 
    
This problem is not seen in later version of android as it retries with different packet sizes. 
    
