#!/usr/bin/env python3
#Notando v1.1.1 for Windows systems running at least Python 3.6

#imports
from pathlib import Path
from shutil import rmtree, copytree
from getpass import getuser
import os

#declaration of global variables
#global path #deprecated
#global prefPath #deprecated
global path
global usrname
global lang
global availableLangs
availableLangs  = ['English', 'Deutsch']
#path = '/home/pi/.notando/notes/' #deprecated
#prefPath = '/home/pi/.notando/preferences/' #deprecated
#Path = '/home/pi/.notando/' #deprecated
usrname = getuser()

with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'rt') as f:
    path = f.read()

with open('C:/users/'+usrname+'/.notando/preferences/lang.txt', 'rt') as f:
    lang = f.read()
    availableLangs.remove(lang)

#main menu
def menu(language):
    
    if language == 'English':
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
                print()
                print('Available categories:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                print()
                category = input('Category: ')
                filename = input('Headline: ')
                text = input('Text: ')
                take(lang, path+'notes/'+category+'/', filename, text)

            #preparations for reading a note & call to readN()
            elif choice == '2':
                print('')
                print('--------------------')
                print('Read a note')
                print('--------------------')
                print('Available categories:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                category = input('Category: ')
                print('Notes in '+category+':')
                nts = os.listdir(path+'notes/'+category)
                for m in nts:
                    print('-- '+m)
                print()
                filename = input('Headline: ')
                readN(lang, path+'notes/'+category+'/', filename)

            #preparations for 'editing' a note & call to edit()
            elif choice == '3':
                print('')
                print('--------------------')
                print('Edit a note')
                print('--------------------')
                print('Available categories:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                category = input('Category: ')
                print('Notes in '+category+':')
                nts = os.listdir(path+'notes/'+category)
                for m in nts:
                    print('-- '+m)
                print()
                filename = input('Headline: ')
                edit(lang, path+'notes/'+category+'/', filename)

            #preparations for removing a note & call to removeN()
            elif choice == '4':
                print('')
                print('--------------------')
                print('Remove a note')
                print('--------------------')
                print('Caution! This will irreversibly delete the note.')
                category = input('Category: ')
                filename = input('Headline: ')
                removeN(lang, path+'notes/'+category+'/', filename)

            #show headline 'Preferences' & call prefs() to present prefs sub-menu
            elif choice == '5':
                print('')
                print('--------------------')
                print('Preferences')
                print('--------------------')
                prefs(lang)

            #quit Notando
            elif choice == '6':
                exit()

            #resetting the choice variable so you'll be able to reuse the menu the next time
            choice = '0'
            
    elif language == 'Deutsch':
        options = ['1', '2', '3', '4', '5', '6']
        choice = '0'
        while True:
            while choice not in options:
                #the standard prompt
                print('--------------------')
                print('Schön, dass du Notando nutzt!')
                print('Bitte tippe eine Zahl um die App zu steuern:')
                print('1. Eine Notiz verfassen')
                print('2. Deine Notizen lesen')
                print('3. Eine Notiz bearbeiten')
                print('4. Eine Notiz löschen')
                print('5. Einstellungen')
                print('6. Schließen')
                print('--------------------')
                choice = input()

            #preparations for taking a note & call to take()
            if choice == '1':
                print()
                print('--------------------')
                print('Eine Notiz verfassen')
                print('--------------------')
                print('Achtung! Die Überschrift darf nur die herkömmlichen Zeichen für die Benennung von Dateien beinhalten (also keine Sonderzeichen, Leerzeichen, Umlaute)')
                print('Achtung! Diese Aktion wird jede bestehende Notiz mit derselben Überschrift unwiederbringlich überschreiben. Besser du schaust erst nach, ob es solche Notizen gibt.')
                print('Bitte beachte auch: Im Moment ist es unmöglich, deinen Text auf irgendeine Art zu formatieren. Selbst gewöhnliche Formatierer wie \n funktionieren nicht und werden ignoriert.')
                print()
                print('Verfügbare Kategorien:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                print()
                category = input('Kategorie: ')
                filename = input('Überschrift: ')
                text = input('Text: ')
                take(lang, path+'notes/'+category+'/', filename, text)

            #preparations for reading a note & call to readN()
            elif choice == '2':
                print('')
                print('--------------------')
                print('Eine Notiz lesen')
                print('--------------------')
                print('Verfügbare Kategorien:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                category = input('Kategorie: ')
                print('Notizen in '+category+':')
                nts = os.listdir(path+'notes/'+category)
                for m in nts:
                    print('-- '+m)
                print()
                filename = input('Überschrift: ')
                readN(lang, path+'notes/'+category+'/', filename)

            #preparations for 'editing' a note & call to edit()
            elif choice == '3':
                print('')
                print('--------------------')
                print('Eine Notiz bearbeiten')
                print('--------------------')
                print('Verfügbare Kategorien:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                category = input('Kategorie: ')
                print('Notizen in '+category+':')
                nts = os.listdir(path+'notes/'+category)
                for m in nts:
                    print('-- '+m)
                print()
                filename = input('Überschrift: ')
                edit(lang, path+'notes/'+category+'/', filename)

            #preparations for removing a note & call to removeN()
            elif choice == '4':
                print('')
                print('--------------------')
                print('Eine Notiz löschen')
                print('--------------------')
                print('Achtung! Dieser Vorgang löscht die Notiz unwiderruflich.')
                print()
                print('Verfügbare Kategorien:')
                cats = os.listdir(path+'notes/')
                for n in cats:
                    print('+ '+n)
                category = input('Kategorie: ')
                print('Notizen in '+category+':')
                nts = os.listdir(path+'notes/'+category)
                for m in nts:
                    print('-- '+m)
                print()
                filename = input('Überschrift: ')
                removeN(lang, path+'notes/'+category+'/', filename)

            #show headline 'Preferences' & call prefs() to present prefs sub-menu
            elif choice == '5':
                print('')
                print('--------------------')
                print('Einstellungen')
                print('--------------------')
                prefs(lang)

            #quit Notando
            elif choice == '6':
                exit()

            #resetting the choice variable so you'll be able to reuse the menu the next time
            choice = '0'

#taking a note
def take(language, argpath, filename, text):
    if language == 'English':
        try:
            with open(argpath+filename+'.txt', 'wt') as f:
                f.write(text)
            input('Note successfully added! Press enter to proceed.')
        except BaseException as error: #react to any error that may occure, analogue within the next functions
            print('An error occured:', error)
            menu(lang) #call the menu in order to prevent the program from crashing, analogue within the next functions
    
    elif language == 'Deutsch':
        try:
            with open(argpath+filename+'.txt', 'wt') as f:
                f.write(text)
            input('Notiz erfolgreich hinzugefügt! Drücke Enter, um fortzufahren.')
        except BaseException as error: #react to any error that may occure, analogue within the next functions
            print('Fehler:', error)
            menu(lang) #call the menu in order to prevent the program from crashing, analogue within the next functions

#reading a note
def readN(language, argpath, filename):
    if language == 'English':
        try:
            with open(argpath+filename+'.txt', 'rt') as f:
                print('--------------------')
                print(filename+' reads:')
                print(f.read())
                print('--------------------')
            input('Press enter to proceed')
        except BaseException as error:
            print('An error occured:', error)
            menu(lang)
    elif language == 'Deutsch':
        try:
            with open(argpath+filename+'.txt', 'rt') as f:
                print('--------------------')
                print(filename+':')
                print(f.read())
                print('--------------------')
            input('Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            menu(lang)

#'editing' a note, while in practice only being able to add some text to the end
def edit(language, argpath, filename):
    if language == 'English':
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
            menu(lang)
    elif language == 'Deutsch':
        try:
            with open(argpath+filename+'.txt', 'rt') as f:
                oldContent = f.read()
                print('--------------------')
                print(filename+' bisher:')
                print(oldContent)
                print('--------------------')
            newContent = oldContent+input('Neuer Inhalt (wird am Ende eingefügt): ') 
            with open(argpath+filename+'.txt', 'wt') as f:
                f.write(newContent)
            input('Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            menu(lang)

#deleting a note irreversibly
def removeN(language, argpath, filename):
    if language == 'English':
        try:
            Path(argpath+filename+'.txt').unlink()
            input(filename+' removed successfully. Press enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            menu(lang)
    
    elif language == 'Deutsch':
        try:
            Path(argpath+filename+'.txt').unlink()
            input(filename+' erfolgreich entfernt. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            menu(lang)

#show 
def prefs(language):
    if language == 'English':
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
                    print('6. Change language')
                    print('7. Return to main menu')
                    print('--------------------')
                    subchoice = input()
                if subchoice == '1': # prepare & make a new category
                    print('--------------------')
                    print('Make a category')
                    print('--------------------')
                    catname = input('Title: ')
                    mkcat(lang, path+'notes/', catname)
                elif subchoice == '2': #prepare & remove a category
                    print('--------------------')
                    print('Remove a category')
                    print('--------------------')
                    print('Available categories:')
                    cats = os.listdir(path+'notes/')
                    for n in cats:
                        print('+ '+n)
                    print()
                    catname = input('Title: ')
                    rmcat(lang, path+'notes/', catname)
                elif subchoice == '3': #prepare & rename a category
                    print('--------------------')
                    print('Rename a category')
                    print('--------------------')
                    print('Available categories:')
                    cats = os.listdir(path+'notes/')
                    for n in cats:
                        print('+ '+n)
                    print()
                    oldname = input('current name: ')
                    newname = input('new name: ')
                    renameCat(lang, oldname, newname)
                elif subchoice == '4': #make a backup image of Notando. Check the print-statements
                    print('--------------------')
                    print('Copy Notando')
                    print('--------------------')
                    print('This will copy every note and preference to a new location provided in the process.')
                    print('This works like a backup, changes made hereafter won\'t apply to the copy.')
                    print('Caution! This will entirely and irreversibly overwrite the provided directory if it is already existing.')
                    newpath = input('Enter the entire path to the new location: ')
                    copyNotando(lang, newpath)
                elif subchoice == '5': #prepare & change the standard path
                    print('--------------------')
                    print('Change standard path')
                    print('--------------------')
                    print('Caution! Only do this if you\'ve manually moved your .notando file.')
                    newpath = input('Enter the absolute path to the new location of .notando with / at the end: ')
                    changePath(lang, newpath)
                elif subchoice == '6': #change the language
                    print('--------------------')
                    print('Change language')
                    print('--------------------')
                    print('Active language: '+lang)
                    print('Other available languages: '+str(availableLangs))
                    newLang = input('To which language do you wish to change? Choose  from '+str(availableLangs)+'. ')
                    while newLang not in availableLangs:
                        newLang = input('This language is not available. Mind the case and choose from '+str(availableLangs)+'. ')
                    changeLang(newLang)
                elif subchoice == '7': #set the terminatePrefs variable to True in order to leave the prefs sub-menu
                    terminatePrefs = True
                subchoice = '0' #ensure the sub-menu is reusable

        except BaseException as error:
            print('An error occured:', error)
            menu(lang)
    elif language == 'Deutsch':
        try:
            #this sub-menu works the same way as the main menu
            terminatePrefs = False
            while terminatePrefs == False:
                suboptions = ['1', '2', '3', '4', '5', '6', '7']
                subchoice = '0'
                while subchoice not in suboptions: #prefs menu's standard prompt
                    print('--------------------')
                    print('1. Neue Kategorie erstellen')
                    print('2. Kategorie entfernen')
                    print('3. Kategorie umbenennen')
                    print('4. Notando kopieren (Backup-Kopie)')
                    print('5. Den Standard-Pfad ändern')
                    print('6. Die Sprache ändern')
                    print('7. Zurück zum Hauptmenü')
                    print('--------------------')
                    subchoice = input()
                if subchoice == '1': # prepare & make a new category
                    print('--------------------')
                    print('Neue Kategorie erstellen')
                    print('--------------------')
                    catname = input('Titel: ')
                    mkcat(lang, path+'notes/', catname)
                elif subchoice == '2': #prepare & remove a category
                    print('--------------------')
                    print('Kategorie löschen')
                    print('--------------------')
                    print('Verfügbare Kategorien:')
                    cats = os.listdir(path+'notes/')
                    for n in cats:
                        print('+ '+n)
                    print()
                    catname = input('Titel: ')
                    rmcat(lang, path+'notes/', catname)
                elif subchoice == '3': #prepare & rename a category
                    print('--------------------')
                    print('Kategorie umbenennen')
                    print('--------------------')
                    print('Verfügbare Kategorien:')
                    cats = os.listdir(path+'notes/')
                    for n in cats:
                        print('+ '+n)
                    print()
                    oldname = input('Aktueller Name: ')
                    newname = input('Neuer Name: ')
                    renameCat(lang, oldname, newname)
                elif subchoice == '4': #make a backup image of Notando. Check the print-statements
                    print('--------------------')
                    print('Notando kopieren (Backup)')
                    print('--------------------')
                    print('Dieser Vorgang wird jede Notiz und jede Einstellung an einen neuen Ort kopieren')
                    print('Dies funktioniert wie ein Backup, hiernach durchgeführte Änderungen werden die Kopie nicht verhändern.')
                    print('Achtung! Gib einen Ordner an, der noch nicht existiert oder gelöscht werden kann, denn falls der angegebene Ordner bereits existiert, wird er unwiderruflich rekursiv gelöscht!')
                    newpath = input('Der absolute Pfad zum Ort des Backups: ')
                    copyNotando(lang, newpath)
                elif subchoice == '5': #prepare & change the standard path
                    print('--------------------')
                    print('Den Standard-Pfad ändern')
                    print('--------------------')
                    print('Achtung! Tu das nur, wenn du deinen .notando-Ordner manuell verschoben hast.')
                    newpath = input('Der neue absolute Pfad des .notando-Ordners mit / am Ende: ')
                    changePath(lang, newpath)
                elif subchoice == '6': #change the language.
                    print('--------------------')
                    print('Sprache ändern')
                    print('--------------------')
                    print('Momentane Sprache: '+lang)
                    print('Weitere verfügbare Sprachen: '+str(availableLangs))
                    newLang = input('Zu welcher Sprache möchtest du wechseln? Wähle aus '+str(availableLangs)+'. ')
                    while newLang not in availableLangs:
                        newLang = input('Diese Sprache ist nicht verfügbar. Beachte Groß- und Kleinschreibung und wähle aus '+str(availableLangs)+'. ')
                    changeLang(newLang)
                elif subchoice == '7': #set the terminatePrefs variable to True in order to leave the prefs sub-menu
                    terminatePrefs = True
                subchoice = '0' #ensure the sub-menu is reusable

        except BaseException as error:
            print('Fehler:', error)
            menu(lang)

#pref-option: make up a new category
def mkcat(language, argpath, catname):
    if language == 'English':
        try:
            newCat = Path(argpath+catname+'/')
            newCat.mkdir(exist_ok=True)
            input(catname+' successfully made. Press Enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            prefs(lang)
    elif language == 'Deutsch':
        try:
            newCat = Path(argpath+catname+'/')
            newCat.mkdir(exist_ok=True)
            input(catname+' erfolgreich erstellt. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            prefs(lang)

#pref-option: remove a category
def rmcat(language, argpath, catname):
    if language == 'English':
        try:
            rmtree(argpath+catname+'/')
            input(catname+' successfully removed. Press Enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            prefs(lang)
    elif language == 'Deutsch':
        try:
            rmtree(argpath+catname+'/')
            input(catname+' erfolgreich entfernt. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            prefs(lang)

#pref-option: rename an existing category 
def renameCat(language, oldname, newname):
    if language == 'English':
        try:
            oldpath = Path(path+'notes/'+oldname+'/')
            newpath = Path(path+'notes/'+newname+'/')
            oldpath.rename(newpath)
            input(oldname+' successfully renamed to '+newname+'. Press Enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            prefs(lang)
    elif language == 'Deutsch':
        try:
            oldpath = Path(path+'notes/'+oldname+'/')
            newpath = Path(path+'notes/'+newname+'/')
            oldpath.rename(newpath)
            input(oldname+' erfolgreich umbenannt in '+newname+'. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            prefs(lang)

#pref-option: change the standard path
def changePath(language, newpath):
    if language == 'English':
        try:
            with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'rt') as f:
                oldpath = f.read()
            path = newpath
            with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'wt') as f:
                f.write(newpath)
            input('Standard path successfully changed from: '+oldpath+' to: '+newpath+'. Press Enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            prefs(lang)
    elif language == 'Deutsch':
        try:
            with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'rt') as f:
                oldpath = f.read()
            path = newpath
            with open('C:/users/'+usrname+'/.notando/preferences/stdpath.txt', 'wt') as f:
                f.write(newpath)
            input('Standard-Pfad erfolgreich von '+oldpath+' zu '+newpath+' geändert. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            prefs(lang)

#pref-option: make a backup-image (while in fact only making a copy of the whole program in a different place)
def copyNotando(language, newpath):
    if language == 'English':
        try:
            if Path(newpath).exists():
                rmtree(newpath)
            copytree(path, newpath)
            input('Notando has been copied successfully. Press Enter to proceed.')
        except BaseException as error:
            print('An error occured:', error)
            prefs(lang)
    elif language == 'Deutsch':
        try:
            if Path(newpath).exists():
                rmtree(newpath)
            copytree(path, newpath)
            input('Notando erfolgreich kopiert. Drücke Enter, um fortzufahren.')
        except BaseException as error:
            print('Fehler:', error)
            prefs(lang)

#pref-option: change the language
def changeLang(newlang):
    try:
        with open('C:/users/'+usrname+'/.notando/preferences/lang.txt', 'wt') as f:
            f.write(newlang)
            lang = newlang
        if lang == 'English':
            input('Language successfull changed to English. App restart required for the change to take effect. Press enter to proceed.')
        elif lang == 'Deutsch':
            input('Sprache erfolgreich nach Deutsch geändert. Programmneustart erforderlich um die Änderungen wirksam zu machen. Drücke Enter, um fortzufahren.')
    except BaseException as error:
        print('An error occured: / Fehler: '+error)

#this is written to the terminal when the program's started
if lang == 'English':
    print('====================')
    print('NOTANDO 1.1.0')
    print('The Note Taking And Organizing App – by Nina Tolfersheimer')
    print('Open source, feel free to edit and spread Notando :)')
    print('Having Problems? Open an issue on GitHub or mail to nina.tolfersheimer@gmail.com')
    print('====================')
    print('Please notice that although this version of Notando can be considered stable, bugs or errors may occur any time.')
    print('')
elif lang == 'Deutsch':
    print('====================')
    print('NOTANDO 1.1.0')
    print('Die App, um Notizen aufzunehmen und zu verwalten (The Note Taking And Organizing App) – von Nina Tolfersheimer')
    print('Open-Source, bearbeite und verbreite Notando gerne :)')
    print('Probleme? Eröffne einen Issue auf GitHub oder schreib eine Mail an nina.tolfersheimer@gmail.com')
    print('====================')
    print('Bitte beachte, dass Fehler jederzeit auftreten können, auch wenn diese Version "stable" ist.')
    print('')

menu(lang) #initialy calling the main menu
