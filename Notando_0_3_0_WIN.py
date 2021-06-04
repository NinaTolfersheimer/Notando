#!/usr/bin/env python3
#Notando v0.3.0 for Windows systems running at least Python 3.6

#imports
from pathlib import Path
from shutil import rmtree, copytree
from getpass import getuser

#declaration of global variables
#global path #deprecated
#global prefPath #deprecated
global path
global usrname
#path = '/home/pi/.notando/notes/' #deprecated
#prefPath = '/home/pi/.notando/preferences/' #deprecated
#Path = '/home/pi/.notando/' #deprecated
usrname = getuser()

with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'rt') as f:
    path = f.read()

#main menu
def menu():
    options = ['1', '2', '3', '4', '5', '6']
    choice = '0'
    while True:
        while choice not in options:
            #the standard prompt
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
        
        #preparations for taking a note & call to take()
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
            take(path+'notes/'+category+'/', filename, text)
        
        #preparations for reading a note & call to readN()
        elif choice == '2':
            print('')
            print('--------------------')
            print('Read a note')
            print('--------------------')
            category = input('Category: ')
            filename = input('Headline: ')
            readN(path+'notes/'+category+'/', filename)
        
        #preparations for 'editing' a note & call to edit()
        elif choice == '3':
            print('')
            print('--------------------')
            print('Edit a note')
            print('--------------------')
            category = input('Category: ')
            filename = input('Headline: ')
            edit(path+'notes/'+category+'/', filename)
        
        #preparations for removing a note & call to removeN()
        elif choice == '4':
            print('')
            print('--------------------')
            print('Remove a note')
            print('--------------------')
            print('Caution! This will irreversibly delete the note.')
            category = input('Category: ')
            filename = input('Headline: ')
            removeN(path+'notes/'+category+'/', filename)
        
        #show headline 'Preferences' & call prefs() to present prefs sub-menu
        elif choice == '5':
            print('')
            print('--------------------')
            print('Preferences')
            print('--------------------')
            prefs()
        
        #quit Notando
        elif choice == '6':
            exit()
        
        #resetting the choice variable so you'll be able to reuse the menu the next time
        choice = '0'

#taking a note
def take(argpath, filename, text):
    try:
        with open(argpath+filename+'.txt', 'wt') as f:
            f.write(text)
        input('Note successfully added! Press enter to proceed.')
    except BaseException as error: #react to any error that may occure, analogue within the next functions
        print('An error occured:', error)
        menu() #call the menu in order to prevent the program from crashing, analogue within the next functions

#reading a note
def readN(argpath, filename):
    try:
        with open(argpath+filename+'.txt', 'rt') as f:
            print('--------------------')
            print(filename+' reads:')
            print(f.read())
            print('--------------------')
        input('Press enter to proceed')
    except BaseException as error:
        print('An error occured:', error)
        menu()

#'editing' a note, while in practice only being able to add some text to the end
def edit(argpath, filename):
    try:
        with open(argpath+filename+'.txt', 'rt') as f:
            oldContent = f.read()
            print('--------------------')
            print(filename+' reads so far:')
            print(oldContent)
            print('--------------------')
        newContent = oldContent+input('New content to be inserted at the end: ') 
        with open(argpath+filename+'.txt', 'wt') as f:
            f.write(newContent)
        input('Press enter to proceed')
    except BaseException as error:
        print('An error occured:', error)
        menu()

#deleting a note irreversibly
def removeN(argpath, filename):
    try:
        Path(argpath+filename+'.txt').unlink()
        input(filename+' removed successfully. Press enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        menu()

#show 
def prefs():
    try:
        #this sub-menu works the same way as the main menu
        terminatePrefs = False
        while terminatePrefs == False:
            suboptions = ['1', '2', '3', '4', '5', '6', '7']
            subchoice = '0'
            while subchoice not in suboptions: #prefs menu's standard prompt
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
            if subchoice == '1': # prepare & make a new category
                print('--------------------')
                print('Make a category')
                print('--------------------')
                catname = input('Title: ')
                mkcat(path+'notes/', catname)
            elif subchoice == '2': #prepare & remove a category
                print('--------------------')
                print('Remove a category')
                print('--------------------')
                catname = input('Title: ')
                rmcat(path+'notes/', catname)
            elif subchoice == '3': #prepare & rename a category
                print('--------------------')
                print('Rename a category')
                print('--------------------')
                oldname = input('current name: ')
                newname = input('new name: ')
                renameCat(oldname, newname)
            elif subchoice == '4': #make a backup image of Notando. Check the print-statements
                print('--------------------')
                print('Copy Notando')
                print('--------------------')
                print('This will copy every note and preference to a new location provided in the process.')
                print('This works like a backup, changes made hereafter won\'t apply to the copy.')
                print('Caution! This will entirely and irreversibly overwrite the provided directory if it is already existing.')
                newpath = input('Enter the entire path to the new location: ')
                copyNotando(newpath)
            elif subchoice == '5': #prepare & change the standard path
                print('--------------------')
                print('Change standard path')
                print('--------------------')
                print('Caution! Only do this if you\'ve manually moved your .notando file.')
                newpath = input('Enter the absolute path to the new location of .notando with / at the end: ')
                changePath(newpath)
            elif subchoice == '6': #change the language. Not yet available.
                changeLang()
            elif subchoice == '7': #set the terminatePrefs variable to True in order to leave the prefs sub-menu
                terminatePrefs = True
            subchoice = '0' #ensure the sub-menu is reusable

    except BaseException as error:
        print('An error occured:', error)
        menu()

#pref-option: make up a new category
def mkcat(argpath, catname):
    try:
        newCat = Path(argpath+catname+'/')
        newCat.mkdir(exist_ok=True)
        input(catname+' successfully made. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

#pref-option: remove a category
def rmcat(argpath, catname):
    try:
        rmtree(argpath+catname+'/')
        input(catname+' successfully removed. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

#pref-option: rename an existing category 
def renameCat(oldname, newname):
    try:
        oldpath = Path(path+'notes/'+oldname+'/')
        newpath = Path(path+'notes/'+newname+'/')
        oldpath.rename(newpath)
        input(oldname+' successfully renamed to '+newname+'. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

#pref-option: change the standard path
def changePath(newpath):
    try:
        with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'rt') as f:
            oldpath = f.read()
        path = newpath
        with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'wt') as f:
            f.write(newpath)
        input('Standard path successfully changed from: '+oldpath+' to: '+newpath+'. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

#pref-option: make a backup-image (while in fact only making a copy of the whole program in a different place)
def copyNotando(newpath):
    try:
        if Path(newpath).exists():
            rmtree(newpath)
        copytree(path, newpath)
        input('Notando has been copied successfully. Press Enter to proceed.')
    except BaseException as error:
        print('An error occured:', error)
        prefs()

#pref-option: change the language
def changeLang():
    input('This feature is not available yet. Hope you do speak English... Either way, please press Enter to proceed')

#this is written to the terminal when the program's started
print('====================')
print('NOTANDO 0.3.0')
print('The Note Taking And Organizing App – by Nina Tolfersheimer')
print('Open source, feel free to edit and spread Notando :)')
print('====================')
print('Please notice that this version of Notando should be considered unstable.')
print('')

menu() #initialy calling the main menu
