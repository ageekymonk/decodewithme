Title: Abstracting ConfigParser as a dictionary
Date: 2014-06-30 16:35:09
Modified: 2014-06-30 16:35:09
Category: Snippets
Tags: code, python, configparser
Slug: abstracting-config-parser-as-a-dict
Authors: Ramz
Summary: A brief idea about how to use configparser as a dict


When we are parsing the config file which has only one section, to get a particular config in a file we have to
specify config.get('default', 'key1'). This looks little cumbersome if you have to do too many times.

``` python
import ConfigParser
config = ConfigParser.ConfigParser()
config.read(config_file)

value1 = config.get('default', 'key1')
value2 = config.get('default', 'key2')
value3 = config.get('default', 'key3')
```

To avoid this we can abstract this as a dictionary. This way it provides better readability too.

``` python 
class AppConfig(dict):
    def __init__(self,fn, *args):
        self.config = ConfigParser.ConfigParser()
        self.config.read(fn)
        dict.__init__(self,args)

    def __getitem__(self, key):
        try:
            val = self.config.get('default', key)
        except:
            val = dict.__getitem__(self, key)
        return val


myconfig = AppConfig(config_file)

value1 = myconfig['key1']
value2 = myconfig['key2']
value3 = myconfig['key3']
```

