# Integration-Testing-Framework
Project to store files related to automating testing for SIL Software on Linux

Packaging a Vagrant Box: 
C:\Users\mccoppinR>vagrant package --base box_to_package
--output ubuntu64

Run Script as root: sudo -u root command

Big picture
* Powershell 
 * presents options for os, software suite
  * uses software suite to load list of scripts from proper repo
   * uses software suite chosen to edit Vagrant file (perl script?)
    * for right suite 
    * for right test scripts (from repo)
   * choose scripts to use, write to file
 * calls vagrant up followed by vagrant reload

* Vagrant
** Installs software and scripts
** Boots software and scripts in "auto run" folder
** Reboot login starts scripts

* Python/Sikuli
** Sikuli control scripts
** Report errors

*REPORT EVERY ERROR*
* If expect breaks, needs to be reported


Need to do:

Generica

  * Install VirtualBox

  * Install Git  =  put git commands on windows shell

  * Install Vagrant

  * Use Vagrant File (Ryan’s) OR follow tutorial at Vagrant website. Boot into a linux machine!

  * Auto open FLEX and run script sikuli_runall.sh by Vagrantfile

