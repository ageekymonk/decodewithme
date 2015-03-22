Title: Scala Equivalent of Ruby's times method on int
Date: 2015-01-29 16:46:37
Modified: 2015-01-29 16:46:37
Category: Snippets
Tags: code, scala, overloading
Slug: Scala-equivalent-of-ruby-times-method
Authors: Ramz
Summary: A snippet about using implicit methods for fun and profit

An elegant way of looping in Ruby is as below

```ruby

    3.times {
        print "Hello"
    }

```


Can we have something similar in scala.

```scala

    implicit def methods_for_int(x:Int) = new {
        def times(f: => Any) = (1 to x).foreach(_ => f)
    }
    
    3.times {
        print("Hello")
    }

```