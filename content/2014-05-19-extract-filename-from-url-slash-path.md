Title: Bash: Extract Filename from url / pathname
Date: 2014-05-19 10:52:42
Modified: 2014-05-19 10:52:42
Category: Snippets
Tags: Bash
Slug: bash-extract-filename-from-url
Authors: Ramz
Summary: A snippet to extract file name from url or pathname

Bash provides builtin functions to extract part of string. 
#####Some string manipulation operators are
	1. '#' remove minimal matching prefixes
	2. '##' remove maximal matching prefixes
	3. '%' remove minimal matching suffixes
	4. '%%' remove maximal matching suffixes

#####Example1:
	FN=/home/chaos/squidguard_1.5-1.dsc
	echo ${FN##/*/} -> Prints squidguard_1.5-1.dsc
	echo ${FN#/*/}	-> Prints chaos/squidguard_1.5-1.dsc
	echo ${FN%/*}	-> Prints /home/chaos
	echo ${FN%%/*}	-> Prints none. As it removes everything from first / till end. 

#####Example2:
	URL=http://ftp.de.debian.org/debian/pool/main/s/squidguard/squidguard_1.5-1.dsc
	echo ${URL##*/} -> Prints squidguard_1.5-1.dsc
	echo ${URL#*//}	-> Prints ftp.de.debian.org/debian/pool/main/s/squidguard/squidguard_1.5-1.dsc
	echo ${URL%/*}	-> Prints http://ftp.de.debian.org/debian/pool/main/s/squidguard
	echo ${URL%%/*}	-> Prints http:


