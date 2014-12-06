Title: Jmeter: Adding Beanshell script for extracting URL
Date: 2014-06-30 16:58:52
Modified: 2014-06-30 16:58:52
Category: Snippets
Tags: jmeter, beanshell
Slug: jmeter-adding-beanshell-script-for-extracting-url
Authors: Ramz
Summary: A snippet in beanshell to extract url in jmeter from the http response.

The following code will extract from the response which has redirect url, port and path
and put as a variable with name redirect_url, redirect_port, redirect_path. This can be used in jmeter to redirect to
next page.


    import java.util.regex;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    String response = new String(prev.getResponseHeaders());

    Pattern r = Pattern.compile(“Location:\\s+http://([^:]+):(\\d+)(.*)”);
    Matcher m = r.matcher(response);

    if (m.find())
    {
    vars.put(“redirect_url”, m.group(1));
    vars.put(“redirect_port”,m.group(2));
    vars.put(“redirect_path”,m.group(3));
    }
    else
    {
            vars.put(“redirect_url”,”www.google.com”);
            vars.put(“redirect_port”, “80”);
            vars.put(“redirect_path”, “/“);
    }

