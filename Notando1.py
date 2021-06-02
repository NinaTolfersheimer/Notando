#!/usr/bin/env python3

from pathlib import Path
from shutil import rmtree, copytree

global path
global prefPath
global currentInstallPath
path = '/home/pi/.notando/notes/'
prefPath = '/home/pi/.notando/preferences/'
currentInstallPath = '/home/pi/.notando/'

def menu():
    options = ['1', '2', '3', '4', '5', '6']
    choice = '0'
    while True:
        while choice not in options:
            print('--------------------')
            print('Thanks for using Notando')
            print('Please type a number to controll the app:')
            print('1. Take a note')
            print('2. Read your notes')
            print('3. Edit a note')
            print('4. Remove a note')
            print('5. Preferences')
            print('6. Quit')
            print('--------------------')
            choice = input()

        if choice == '1':
            print()
            print('--------------------')
            print('Take a note')
            print('--------------------')
            print('Caution! Headline may only contain common characters for naming files.')
            print('Caution! This action will overwrite any existing notes sharing the same headline irreversibly. Better check for such if in doubt.')
            print('Please note as well: It\'s impossible at the present state of development to format your input by any means, so format specifiers won\'t be processed.')
            category = input('Category: ')
            filename = input('Headline: ')
            text = input('Text: ')
            take(path+category+'/', filename, text)

        elif choice == '2':
            print('')
            print('--------------------')
            print('Read a note')
            print('--------------------')
            category = input('Category: ')
            filename = input('Headline: ')
            readN(path+category+'/', filename)

        elif choice == '3':
            print('')
            print('--------------------')
            print('Edit a note')
            print('--------------------')
            category = input('Category: ')
            filename = input('Headline: ')
            edit(path+category+'/', filename)

        elif choice == '4':
            print('')
            print('--------------------')
            print('Remove a note')
            print('--------------------')
            print('Caution! This will irreversibly delete the note.')
            category = input('Category: ')
            filename = input('Headline: ')
            removeN(path+category+'/', filename)

        elif choice == '5':
            print('')
            print('--------------------')
            print('Preferences')
            print('--------------------')
            prefs()

        elif choice == '6':
            exit()

        choice = '0'

def take(path, filename, text):
    try:
        with open(path+filename+'.txt', 'wt') as f:
            f.write(text)
        input('Note successfully added! Press enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        menu()

def readN(path, filename):
    try:
        with open(path+filename+'.txt', 'rt') as f:
            print('--------------------')
            print(filename+' reads:')
            print(f.read())
            print('--------------------')
        input('Press enter to proceed')
    except BaseException as error:
        print('An error occured:', error)
        menu()

def edit(path, filename):
    try:
        with open(path+filename+'.txt', 'rt') as f:
            oldContent = f.read()
            print('--------------------')
            print(filename+' reads so far:')
            print(oldContent)
            print('--------------------')
        newContent = oldContent+input('New content to be inserted at the expressed place [NOTE: Currently only the end. Check note titled "IdeaForEditInserting"]: ')
        with open(path+filename+'.txt', 'wt') as f:
            f.write(newContent)
        input('Press enter to proceed')
    except BaseException as error:
        print('An error occured:', error)
        menu()

def removeN(path, filename):
    try:
        Path(path+filename+'.txt').unlink()
        input(filename+' removed successfully. Press enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        menu()

def prefs():
    try:
        terminatePrefs = False
        while terminatePrefs == False:
            suboptions = ['1', '2', '3', '4', '5', '6', '7']
            subchoice = '0'
            while subchoice not in suboptions:
                print('--------------------')
                print('1. Make a category')
                print('2. Remove a category')
                print('3. Rename a category')
                print('4. Copy Notando')
                print('5. Change standard path')
                print('6. Change language [not available yet]')
                print('7. Return to main menu')
                print('--------------------')
                subchoice = input()
            if subchoice == '1':
                print('--------------------')
                print('Make a category')
                print('--------------------')
                catname = input('Title: ')
                mkcat(path, catname)
            elif subchoice == '2':
                print('--------------------')
                print('Remove a category')
                print('--------------------')
                catname = input('Title: ')
                rmcat(path, catname)
            elif subchoice == '3':
                print('--------------------')
                print('Rename a category')
                print('--------------------')
                oldname = input('current name: ')
                newname = input('new name: ')
                renameCat(oldname, newname)
            elif subchoice == '4':
                print('--------------------')
                print('Copy Notando')
                print('--------------------')
                print('This will copy every note and preference to a new location provided in the process.')
                print('This works like a backup, changes made hereafter won\'t apply to the copy.')
                print('Caution! This will entirely and irreversibly overwrite the provided directory if it is already existing.')
                newpath = input('Enter the entire path to the new location: ')
                copyNotando(newpath)
            elif subchoice == '5':
                print('--------------------')
                print('Change standard path')
                print('--------------------')
                print('This will store new notes to a new location provided in the process and save this change.')
                newpath = input('Enter the entire path to the new location: ')
                changePath(newpath)
            elif subchoice == '6':
                changeLang()
            elif subchoice == '7':
                terminatePrefs = True
            subchoice = '0'

    except BaseException as error:
        print('An error occured:', error)
        menu()

def mkcat(path, catname):
    try:
        newCat = Path(path+catname+'/')
        newCat.mkdir(exist_ok=True)
        print(catname, 'successfully made')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

def rmcat(path, catname):
    try:
        rmtree(path+catname+'/')
        print(catname, 'successfully removed')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

def renameCat(oldname, newname):
    try:
        oldpath = Path(path+oldname+'/')
        newpath = Path(path+newname+'/')
        oldpath.rename(newpath)
        print(oldname, 'successfully renamed to', newname)
    except BaseException as error:
        print('An error occured:', error)
        prefs()

def changePath(newpath):
    try:
        oldpath = path
        path = newpath
        with open(prefPath+'stdpath.txt', 'wt') as f:
            f.write(newpath)
        print('Standard path for storing notes successfully changed from: '+oldpath+' to: '+newpath)
    except BaseException as error:
        print('An error occured:', error)
        prefs()

def copyNotando(newpath):
    try:
        if Path(newpath).exists():
            rmtree(newpath)
        copytree(currentInstallPath, newpath)
        input('Notando has been copied successfully. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

def changeLang():
    print('This feature is not available yet. Hope you do speak English...')

print('====================')
print('NOTANDO 1.0')
print('The Note Taking And Organizing App – (c) 2021 by Nina Tolfersheimer')
print('====================')
print('')

menu()