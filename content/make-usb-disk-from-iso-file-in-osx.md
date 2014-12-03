Title: Make USB Bootable disk from ISO File in Mac/OSX
Date: 2014-06-14 15:20
Modified: 2014-06-14 15:20
Category: Snippets
Tags: OSX, bootable disk 
Slug: make-usb-disk-from-iso-file-in-osx
Authors: Ramz
Summary: A snippet to make a bootable disk form the ISO file


Convert iso file to img

	hdiutil convert -format UDRW -o ~/path/to/target.img ~/path/to/ubuntu.iso

Insert the usb drive. Find the device number using

	diskutil list

Load the image to the right device. *(Replace N with the disk number from the last command)*

	diskutil unmountDisk /dev/diskN 
		
	sudo dd if=/path/to/downloaded.img of=/dev/rdiskN bs=1m

	diskutil eject /dev/diskN