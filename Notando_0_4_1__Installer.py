#!/usr/bin/env python3

#CAUTION: This installer version is deprecated and has been replaced by the united installer for any OS.

#PURPOSE: This script will set up the required directories and files for Notando 0.4.0 on your Windows device.

#Imports
from pathlib import Path
from shutil import copytree
from getpass import getuser

usrname = getuser()

availableLangs = ['English', 'Deutsch']

#this will be written to the terminal when the program is started
print('====================')
print('NOTANDO 0.4.0 – Installer for Windows')
print('====================')
print()
lang = input('Which language do you want to use for installation and as default? | Welche Sprache möchtest du für die Installation und als Standardwert benutzen? | '+str(availableLangs))
while lang not in availableLangs:
    lang = input('Choose from '+str(availableLangs)+'. | Gültige Antworten: '+str(availableLangs))

if lang == 'English':
    print('Thanks for choosing Notando!')
    print()
    print('Notando is open-source software. You may edit the program, but you do so AT YOUR OWN RISK. You may spread the program, but please be fair: I\'ve done this work, not you; so please refrain from selling the software. It\'d also be nice of you to mention who actually developed this when sharing ;) Thanks!')
    input('Got this? Press enter to proceed.')
    print()

    destPath = input('Where do you want Notando to keep all the files? Please provide an absolute path with / at the end: ')+'.notando/'
    copyPath = Path(destPath)
    installPath = input('Please locate your personal home directory, i.e. C:/users/<yourname>/')+'.notando/'
    installPathPath = Path(installPath)

    try:
        installPathPath.mkdir(exist_ok = True)

        notesPath = Path(installPath+'notes/')
        prefsPath = Path(installPath+'preferences/')

        notesPath.mkdir(exist_ok = True)
        prefsPath.mkdir(exist_ok = True)

        stdCatPath = Path(installPath+'notes/general/')

        stdCatPath.mkdir(exist_ok = True)

        with open(installPath+'notes/general/firstNote.txt', 'wt') as f:
            f.write('This is Notando. Here\'s your first note. You may keep, edit or remove it any time and start noting!')

        with open(installPath+'preferences/lang.txt', 'wt') as f:
            f.write(lang)

        with open(installPath+'preferences/stdpath.txt', 'wt') as f:
            f.write(destPath)

        try:
            copytree(installPathPath, copyPath)
        except BaseException as error:
            print('An error occured when copying Notando to your desired location:', error)

        print('--------------------')
        print('Installation successfully completed!')
        print('You can use Notando by executing Notando_0_4_0__WIN.py, which you should\'ve received together with this one.')
        print('If you\'re in doubt how to start Notando, ask the people you\'ve received your copy from for help, or write an email to nina.tolfersheimer@posteo.de')
        print('--------------------')
        input()

    except BaseException as error:
        print('An error occured:', error)

elif lang == 'Deutsch':
    print('Schön, dass du Notando nutzt!')
    print()
    print('Notando ist open-source software. Du darfst das Programm gerne bearbeiten, aber du tust das AUF EIGENE GEFAHR. Du darfst das Programm gerne verbreiten, aber bitte bleib fair: Ich habe diese Arbeit gemacht, nicht du; also verkaufe Notando bitte nicht. Es wäre auch nett von dir, wenn du beim Weitergeben erwähnen könntest, wer das Programm ursprünglich entwickelt hat ;) Danke!')
    input('Alles klar? Drücke Enter, um fortzufahren.')
    print()

    destPath = input('In welchem Ordner soll Notando deine Dateien aufbewahren? Bitte gib einen absoluten Pfad mit / am Ende an: ')+'.notando/'
    copyPath = Path(destPath)
    installPath = input('Bitte gib dein persönliches Stammverzeichnis an, z.B. C:/users/<deinname>/')+'.notando/'
    installPathPath = Path(installPath)

    try:
        installPathPath.mkdir(exist_ok = True)

        notesPath = Path(installPath+'notes/')
        prefsPath = Path(installPath+'preferences/')

        notesPath.mkdir(exist_ok = True)
        prefsPath.mkdir(exist_ok = True)

        stdCatPath = Path(installPath+'notes/general/')

        stdCatPath.mkdir(exist_ok = True)

        with open(installPath+'notes/general/firstNote.txt', 'wt') as f:
            f.write('Willkommen bei Notando. Dies ist deine erste Notiz. Du kannst sie behalten oder jederzeit bearbeiten oder löschen. Viel Erfolg mit deinen Notizen!')

        with open(installPath+'preferences/lang.txt', 'wt') as f:
            f.write(lang)

        with open(installPath+'preferences/stdpath.txt', 'wt') as f:
            f.write(destPath)

        try:
            copytree(installPathPath, copyPath)
        except BaseException as error:
            print('Beim Kopieren von Notando an die gewünschte Stelle ist ein Fehler aufgetreten:', error)

        print('--------------------')
        print('Installation erfolgreich abgeschlossen!')
        print('Du kannst Notando benutzen, indem du das Script Notando_0_4_0__WIN.py ausführst, das du bekommen haben solltest.')
        print('Wenn du dir unsicher bist wie du Notando startest, frag die Leute, von denen du deine Kopie von Notando bekommen hast, oder schreib eine Mail an nina.tolfersheimer@posteo.de')
        print('--------------------')
        input()

    except BaseException as error:
        print('Fehler:', error)

