Title: Sending Basic Auth HTTP Request in Python
Date: 2014-12-06 20:50:52
Modified: 2014-12-06 20:50:52
Category: Snippets
Tags: python
Slug: sending-basic-auth-http-request-in-python
Authors: Ramz
Summary: A small snippet to send Basic Auth HTTP Request in Python


The steps to Send a Basic Auth Request with content type json to a particular URL are

  1. Create a Request Object    
  2. Create base64 encoded string of username and password
  3. Add a authorization header to the request
  4. Add other headers like content type to the request
  5. Send a urlopen request. 


``` python

    #!/usr/bin/python
    
    url = "http://www.somesite.com"
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header('Content-Type', 'application/json')
    json_data = "{}"
    response = urllib2.urlopen(request, json_data)
    if response.getcode() == 200:
        print("Successfully uploaded json_data")
    
```

