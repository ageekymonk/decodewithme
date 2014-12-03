Title: UnPackaging Debian Source Package
Date: 2014-05-19 11:25:23
Modified: 2014-05-19 11:25:23
Category: Snippets
Tags: dpkg
Slug: unpackaging-debian-source-package
Authors: Ramz
Summary: A snippet about how to unpackage the debian source package

If you have downloaded debian source package manually using wget, the easier way to unpackage is to use dpkg-source. Because it is not just untaring and placing the debian folder in the source folder. There might be some extra patches that need to be applied.

For any debian package, there will be three files
 	1. package_name.dsc
 	2. package_name.orig.tar.gz
 	3. package_name.debian.tar.gz

To unpackage

	dpkg-source -x package_name.dsc

#####Example:
For squidguard package
	squidguard_1.5-1.dsc
	squidguard_1.5.orig.tar.gz
	squidguard_1.5-1.debian.tar.gz

To unpackage

	dpkg-source -x squidguard_1.5-1.dsc
