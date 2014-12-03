Title: Python's way of overloading operator []
Date: 2014-10-30 16:46:37
Modified: 2014-10-30 16:46:37
Category: Snippets
Tags: code, python, overloading
Slug: python-way-of-operator-overloading
Authors: Ramz
Summary: An insight about python's way of overloading []



In C++, we can overload the [] operators. Python also supports [] overloading but it is done via overriding `__getitem__`, `__setitem__`
for reading and writing respectively.


`__setitem__` creates a new element if it does not exist.
Once created, What if we need to remove the element entirely. Thats why `__delitem__` is for.

Below is a class which behaves like a dictionary as well as a class.

``` python

class DictLikeClass:

    def __init__(self):
        pass

    def __getitem__(self, key):
        print "Getting Item " + key + " => ",
        if not self.__dict__.has_key(key):
            print "No such key "+ key + ", so returning None =>",
        else:
            return self.__dict__[key]

    def __setitem__(self, key, value):
        print "Setting Item " + key + " with value " + str(value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print "Deleting Item " + key
        del self.__dict__[key]

inst = DictLikeClass()

print inst['x']

inst['x'] = 10
print inst['x']
print inst.x

del inst['x']
print inst['x']

```

*The output for this is*

        Getting Item x =>  No such key x, so returning None => None
        Setting Item x with value 10
        Getting Item x =>  10
        10
        Deleting Item x
        Getting Item x =>  No such key x, so returning None => None


