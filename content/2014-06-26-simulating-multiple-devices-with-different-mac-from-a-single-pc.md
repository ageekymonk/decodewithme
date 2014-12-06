Title: Simulating multiple devices with different mac from a single PC
Date: 2014-06-26 09:44:48
Modified: 2014-06-26 09:44:48
Category: Snippets
Tags: macvlan
Slug: simulate-multiple-devices-with-different-mac-from-a-pc
Authors: Ramz
Summary: A brief idea about how to simulate many devices with different mac from a single PC

If we want to simulate multiple devices (say about 1000) , each with its own mac and send TCP traffic, or any kind of traffic from it,
the best way is to use macvlan. I have personally created 5000 macvlan on a single machine. 

To create a macvlan interface, follow the screencast. Use the steps below to create "n" number of interface, each with its own mac address.

<iframe src="http://showterm.io/26596f68595a3afdd21ad" width="1280" height="960"></iframe>

Once we have the interface we can send traffic using any socket programming to do so.
A sample way to send tcp traffic through an interface **eth0.1** created above to connect to example.com to port 5555.

        import socket
        import IN

        # Create a tcp socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to an interface so that the traffic will flow through that. Otherwise eth0 will be used.
        s.setsockopt(socket.SOL_SOCKET, IN.SO_BINDTODEVICE, "eth0.1")
        s.connect(('example.com',5555))
        s.send("hello")
