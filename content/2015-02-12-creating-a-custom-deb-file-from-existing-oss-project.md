Title: Creating a custom version of .deb file from an existing one
Date: 2015-02-12 23:20
Modified: 2015-02-12 23:20
Category: Snippets
Tags: dpkg
Slug: creating-a-custom-deb-file-from-existing-oss-project
Authors: Ramz
Summary: A brief idea about how to create a .deb file for an oss project with your own custom changes on top

Sometimes we do need to modify the existing code base and create a .deb file so that it can be used. To do that

1. Get the source code from the upstream debian repository

            apt-get source <yourpkg>

2. Apply your custom patch.
3. Bump up the version so that you can identify it. To do that go to the source folder adn give the command.
   This will add version to the already existing one. For example if the already existing version is
   3.3.8-1 now it will become 3.3.8-1.1 (or something similar). You can provide your own numbering as well.

        dch -i ‘my changes'

4. To build the deb file

        debuild -i -uc -us -b

    Thats it folks :)

    


