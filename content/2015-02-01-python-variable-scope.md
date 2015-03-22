Title: Scope of Python local variables
Date: 2015-02-01 09:46:37
Modified: 2015-02-01 09:46:37
Category: Snippets
Tags: code, python
Slug: scope-of-python-local-variables
Authors: Ramz
Summary: Understanding the scope of local variables for writing pythonic code

If you want to find out At want index the loop broke out

```python

    count = 0
    for i in range(10):
        count = i
        if (i == 6):
            break

    print count

```

But an elegant way is

```python

    for i in range(10):
        if (i == 6):
            break

    print i

```

This is possible because the variable i used in the loop, which never existed above, will continue to exist
even after the loop is done

For people coming from other languages will be shocked to know that python have only class, function or module scope.
Variable scope starts from the where they are declared in the function to the end of the function.

This allows us to write elegant code.
