#!/usr/bin/env python3

#PURPOSE: This script will set up the required directories and files for Notando 0.3.0 on your Linux device.

#Imports
from pathlib import Path
from shutil import copytree
from getpass import getuser

usrname = getuser()

#this will be written to the terminal when the program is started
print('====================')
print('NOTANDO 0.2.1 – Installer for Linux')
print('====================')
print()
print('Thanks for choosing Notando!')
print()
print('Notando is open-source software. You may edit the program, but you do so AT YOUR OWN RISK. You may spread the program, but please be fair: I\'ve done this work, not you; so please refrain from selling the software. It\'d also be nice of you to mention who actually developed this when sharing ;) Thanks!')
input('Got this? Press enter to proceed.')
print()

destPath = input('Where do you want Notando to keep all the files? Please provide an absolute path with / at the end: ')+'.notando/'
copyPath = Path(destPath)
installPath = '/home/'+usrname+'/.notando/'
installPathPath = Path('/home/'+usrname+'/.notando/')

try:
    installPathPath.mkdir(exist_ok = True)

    notesPath = Path(installPath+'notes/')
    prefsPath = Path(installPath+'preferences/')

    notesPath.mkdir(exist_ok = True)
    prefsPath.mkdir(exist_ok = True)

    stdCatPath = Path(installPath+'notes/general/')

    stdCatPath.mkdir(exist_ok = True)

    with open(installPath+'notes/general/firstNote.txt', 'wt') as f:
        f.write('This is Notando. Here\'s your first note. You may keep, edit or remove it any time and start noting!.')

    destlang = input('Which language do you prefer for your installation? Choose from the following ones: [English] ')

    while destlang not in ['English']:
        destlang = input('That\'s not a valid language! Choose from [English] and mind the case: ')

    with open(installPath+'preferences/lang.txt', 'wt') as f:
        f.write(destlang)

    with open(installPath+'preferences/stdpath.txt', 'wt') as f:
        f.write(destPath)

    try:
        copytree(installPathPath, copyPath)
    except BaseException as error:
        print('An error occured when copying Notando to your desired location:', error)

    print('--------------------')
    print('Installation successfully completed!')
    print('You can use Notando by executing the other Python script you should\'ve received together with this one.')
    print('If you\'re in doubt how to start Notando, ask the people you\'ve received your copy from for help, or write an email to nina.tolfersheimer@posteo.de')
    print('--------------------')

except BaseException as error:
    print('An error occured:', error)
