Title: Cscope Plugin for Sublime Text
Date: 2014-05-17 09:28:17
Modified: 2014-05-17 09:28:17
Category: Tools
Tags: code, cscope, sublime, sublimetext
Slug: cscope-plugin-for-sublime-text
Authors: Ramz
Summary: A brief tutorial to configure cscope plugin for sublime text

 For browsing large c/c++ code base, the best way is to use cscope. To integrate cscope with sublime text, we need a plugin called CscopeSublime

#####Installation

  1. Go to Preferences -> Package Control

  2. Select: Install Package

  3. Select: cscope

#####Configuration

  1. To set the cscope path, Select "Preferences -> Settings User", this will open preferences.sublime-settings file. Add the following line in that file.

		"CscopeSublime_executable": "/usr/local/bin/cscope"

#####Using in your project

  1. Create Cscope Database at the root of the project

    	find . -name "*" -print > cscope.files

		cscope -b -q

  Now you are all set to go

#####shortcuts

        command panel:  Ctrl + \ 
        Look up symbol: Ctrl + L  Ctrl + S
        Symbol Definition: Ctrl + L Ctrl + D
