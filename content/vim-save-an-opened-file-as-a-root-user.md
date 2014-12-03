Title: Vim: Save an opened file as a root user
Date: 2014-07-12 17:38
Modified: 2014-07-12 17:38
Category: Snippets
Tags: vim
Slug: vim-save-opened-file-as-a-root-user
Authors: Ramz
Summary: A snippet to save a file in vim as a root user

Almost every time i forget to open vim as sudo user, that are supposed to be edited by root and make changes.
And finally when saving you see one of the most dreaded message "readonly option is set (add ! to override)".

To save the file without losing all the editing that you have done use the following command

        :w !sudo tee %
