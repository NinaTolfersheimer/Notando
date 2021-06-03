#!/usr/bin/env python3

#PURPOSE: This script will set up the required directories and files for Notando 0.2.0 on your Linux Debian device. It should work as well on interchangeable devices such as USB-sticks

#Imports
from pathlib import Path

#this will be written to the terminal when the program is started
print('====================')
print('NOTANDO 0.2.0 – Installer for Linux Debian')
print('====================')
print()
print('Thanks for choosing Notando!')
print()
input('You will in the following be presented with Notando\'s Terms of Use as well as its Data Protection Policy. You have to agree to the entirety of both of them (together called "the/this policy"). Press Enter to show the policy.')
print()
print('PLEASE NOTE – IMPORTANT INFORMATION – READ CAREFULLY')
print()
print()
print('====================')
print('NOTANDO 0.2.0 – Terms of Use')
print('NOTANDO 0.2.0 – Data Protection Policy')
print('====================')
print()
print('I. Definitions, limits of this policy')
print('(1) This policy only applies to the unmodified versions of Notando provided by Nina Tolfersheimer or an approved distributor. The term "this/the policy" refers to the entity of the Terms of Use and the Data Protection Policy.')
print('(2) In the very moment you make any changes to the versions of Notando this policy applies to, THE ENTIRETY of ALL RISKS and ALL RESPONSIBILITY WHATSOEVER will immediately be translated to you.')
print('(3) The terms "Notando" and "the app" as well as "the program" in this policy refers to all the pieces of software, every bit of programming code and every file and directory on your local device that you copy or download from the initial program directory or resource as well as those that that software sets up either automatically or on your behalf.')
print('(4) This original English version is the only one really applicable. This policy underlies exclusively European and German law.')
print('(5) Should any part of this policy be found invalid, all its other parts remane in power.')
print('(6) Although this policy may change any time, the only valid version for this specific installation of Notando is this very one. Note that when you some day choose to install another version of Notando, the only valid policy to this specific installation is the one you\'re presented with while installing that very future version.')
print('(7) This policy enters into force as from the moment you agree with it and remains in force until you make any changes to the files that make up the app, including deleting or corrupting one or more of those file(s).')
print('(8) The only applicable version of this policy is the one the user was presented with when installing Notando by running an installer script. If the user hasn\'t done so and installed Notando manually, the one to be found at the project\'s GitHub page (https://github.com/NinaTolfersheimer/Notado/) is the only one applicable.')
print()
print('II. Open-source software, license')
print('(1) The Notando software is open-source. You may share and/or edit Notando,')
print('(2) but you MUST NOT sell it directly or indirectly')
print('(3) or use it for commercial purposes without a permission in written form by Nina Tolfersheimer.')
print('(4) You are required to name the original author, NINA TOLFERSHEIMER, when sharing this or any other version of Notando, even one you\'ve edited or set up yourself.')
print()
print('III. Denial of any warranty, risks')
print('(1) There is ABSOLUTELY NO WARANTY WHATSOEVER that Notando will work on your device by any means.')
print('(2) Notando has been tested on a Raspberry Pi running Raspberry Pi OS as of March 2021, a distribution of Linux Debian. However, some parts may not work on your specific device')
print('(3) or may be loosely tested and/or bugged. This includes bugs with the potential to CAUSE DAMAGE of ANY LEVEL to your device and/or network')
print('(4) You are running Notando AT YOUR OWN RISK and are ENTIRELY RESPONSIBLE FOR EVERY DAMAGE that Notando may cause to your device and/or network.')
print()
print('IV. Data protection')
print('(1) By default, Notando is running completely local on your device.')
print('(2) It does not establish a connection to the internet, unless you modify it to do so. In this case, YOU are the only one responsible for ANY RISKS AND THREATS this may cause to your or other\'s personal data.')
print('(3) Because there is NO PROTECTION GUARANTEED to the data you store through the app, you should both')
print('   (a) be very careful which data you store through the app. Although nobody, not even Notando\'s author(s), will be able to access your notes remotely, except for the case displayed in (2), everybody who gaines access to the directory you provide to Notando to store its files and your data in later on will be able to read all of the information you stored through the app without having any extended knowledge.')
print('   (b) for that reason MAKE ABSOLUTELY SURE to select a directory for Notando to live in you and ONLY YOU have permission to read.')
print('(4) Notando does only use data directly provided to the app by yourself (when Notando asks you to provide it) and NO OTHER except for such already included in the initial software release file.')
print()
print()








      

      


yesno = input('Do you accept the terms above? [yes/no] ')

while yesno not in ['yes', 'y', 'no', 'n']:
    yesno = input('Please type "yes", "y", "no" or "n": ')

if yesno == 'yes' or yesno == 'y':

    destPath = input('Where do you want Notando to keep all the files? Please provide a full path with / at the end: ')+'.notando_0_2_0/'
    installPath = Path(destPath)

    try:
        installPath.mkdir(exist_ok = True)

        notesPath = Path(destPath+'notes/')
        prefsPath = Path(destPath+'preferences/')

        notesPath.mkdir(exist_ok = True)
        prefsPath.mkdir(exist_ok = True)

        stdCatPath = Path(destPath+'notes/general/')

        stdCatPath.mkdir(exist_ok = True)

        with open(destPath+'notes/general/firstNote.txt', 'wt') as f:
            f.write('This is Notando. Here\'s your first note. You may keep, edit or remove it any time and start noting!.')

        destlang = input('Which language do you prefer for your installation? Choose from the following ones: [English] ')

        while destlang not in ['English']:
            destlang = input('That\'s not a valid language! Choose from [English] and mind the case: ')

        with open(destPath+'preferences/lang.txt', 'wt') as f:
            f.write(destlang)

        with open(destPath+'preferences/stdpath.txt', 'wt') as f:
            f.write(destPath+'notes/')

        print('--------------------')
        print('Installation successfully completed!')
        print('You can use Notando by executing the other Python script you should\'ve received together with this one.')
        print('If you\'re in doubt how to start Notando, ask the people you\'ve received your copy from for help, or write an email to nina.tolfersheimer@posteo.de')
        print('--------------------')

    except BaseException as error:
        print('An error occured:', error)

else:
    print('You\'ve chosen not to accept the policy. That\'s perfectly fine, but you won\'t be able to use Notando in this case. You may change your mind any time and re-run this script.')
