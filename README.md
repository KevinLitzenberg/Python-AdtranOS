# Python-AdrtanOS
Python Scripts

This script creates a sshConnect() object that leverages Paramiko to connect and speak to Adtran devices via ssh.  The object gets created with the call to conn = sshConnnect().  Then we call the object's only method getConnection and pass in the arguments.  Once getConnect() method is called we can then begin talking to the device.

In this eample we are logging in.  We first call the command 'show arp' which returns the arp table of the device.  Then we jump up to the enabled user by calling 'en'.  Once we are in enable mode the command 'show ver' is run to show the version of the firmware.

This script can be used to automate to AOS products.  This basic framework is provided as an example.
