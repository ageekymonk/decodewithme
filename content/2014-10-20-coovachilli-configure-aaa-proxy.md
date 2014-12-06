Title: Coovachilli: Configure AAA Proxy
Date: 2014-10-20 14:00
Modified: 2014-10-20 14:00
Category: Tools
Tags: coovachilli, aaa proxy
Slug: coovachilli-configure-aaa-proxy
Authors: Ramz
Summary: A Tutorial to configure HTTP based AAA Proxy so that you can avoid creating your own radius servers

The general outlook of coovachilli network is as below. 
     
![HTOP]({filename}/images/coovachilli.jpg)


What If you chose not to use a AAA Server but manage AAA via http. It is possible to do that. Coovachilli supports 
AAA Proxy, which it comes inbuilt with. All HTTP requests by the proxy have a User-Agent HTTP header of "CoovaChilli (version)".
The architecture of chilli with radius proxy looks something like this.

![HTOP]({filename}/images/coovachilli-with-proxy.jpg)

Coovachilli sends a AAA Request to the proxy which converts AAA Request to HTTP Request to our specified URL. All the 
AAA Parameter is sent as a Key Value Pair in the GET Request to our specified URL. When it gets a response from the HTTP Server 
it converts those response to the AAA Response and sends it back to coovachilli. 

For example: Below is the sample HTTP Request from the proxy

        http://localhost/script.php?stage=login&service=login&user=test&pass=test
        &ap=00-XX-XX-XX-XX-XX&mac=00-XX-XX-XX-XX-XX&ip=10.1.0.2&sessionid=4adb5f4000000001
        &nasid=nas01&md=A9EA5F98B104F41FC330CFE44B2681AD

The expected response by the proxy is empty HTML File with value Auth: 1 for authentication success and
Auth: 0 for failure.

**Configuration**
To configure this we just need to specify, the following in the defaults file (/etc/chilli/defaults). 

        HS_AAA=http 
        HS_UAMAAAURL=http://www.somesite.com/auth
        
HS_AAA config specifies to use http based rather than AAA. In HS_UAMAAAURL you need to specify the url to which the translated
radius request will be sent to.

A sample php code to allow the user with session timeout of 60 seconds, Idle timeout of 60 seconds, max bandwidth up and
down of 256K 

        <?php
        echo "Auth: 1\r\n";
        echo "Session-Timeout: 60\r\n";
        echo "Idle-Timeout: 60\r\n";
        echo "ChilliSpot-Bandwidth-Max-Up: 256000\r\n";
        echo "ChilliSpot-Bandwidth-Max-Down: 256000\r\n";
        ?>

Refer to http://coova.org/CoovaChilli/Proxy to further information about the parameters sent in the url and the expected 
response. 

