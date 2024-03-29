# Notando
_A small open-source alternative to MS OneNote etc. Notando is actively maintained and currently runs in v1.1.1_

## What Notando 1.1.1 can do
Notando 1.1.1 presents you with a menu to choose options from. You can:

1. Take a note – _Allows you to take a note and store it in a specific category. This will take some string and store in a file with the path_ ```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
_. The so-called 'standard path' is the path to the directory where Notando itself lives._
2. Read your notes – _Lets you read a specified note. This will ask for the category the note is stored within as well as the headline you gave it. It will then try to read from the path_ ```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
_and present you with the content of the specified text file._
3. Edit a note – _Allows you to 'edit' a note, although you can currently only write to the file's end. This performs essentially the same task as read would do, but after presenting the file's content, edit will take some string, add it to the end of the content, and re-write the file to the provided path._
4. Remove a note – _Allows you to permanently and irreversibly delete a note. Takes a category and a headline and removes the file at the path_ ```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
5. set Preferences – _You enter the following prefs sub-menu:_
  * Make a category – _Allows you to set up a new category. Takes a name and tries to make a directory with_ ```<standard path>/.notando/notes/<provided category>/```
  * Remove a category – _Allows you to delete a category permanently and irreversibly with all the contained notes. Takes a name and tries to remove the directory with_ ```<standard path>/.notando/notes/<provided category>/``` _recursively._
  * Rename a category – _Allows you to rename a category. Takes an old and a new name and then tries to rename_ ```<standard path>/.notando/notes/<old name>/``` _to_ ```<standard path>/.notando/notes/<new name>/``` 
  * Copy Notando – _Allows you to make a backup of Notando including all the notes and preferences. Takes a path to a directory **THAT IS NOT YET TO EXIST**, deletes this directory recursively if it already exists (useful for regular backing up to the same location), re-makes it, and copies the .notando directory currently set as standard path to the new directory_
_Note that this won't actually make a backup but simply copy the entire installation to the provided location_
  * Change standard path – _In case you've moved your .notando file somewhere else, this tells Notando about it. Takes that directory's path and overwrites the_ ```<standard path>/.notando/preferences/stdpath.txt``` _file with this new content._ 
  * Change language – _Allows you to choose between English and German. Takes the desired language and overwrites_ ```<standard path>/.notando/preferences/lang.txt``` _with it. Checks whether the language you provided is available beforehand._
  * Quit submenu and return to main menu – _Effectively sends a terminate signal which collapses the sub-menu and shows the main menu._
6. Quit – _Sends a terminating signal to exit the program._ `KeyboardInterrupt` / `Ctrl + C` _should work as well._

## How Notando 1.1.1 works
Notando 1.1.1 lets you take and manage notes and organizes them into _categories_. Those categories are effectively the directories the specific note files live in. Every note takes a specific _headline_, which is effectively the file's name, which is why it should only contain letters & numbers and **no whitespace**.

Notando 1.1.1 stores your notes as plain .txt files, but an update to a markup language is currently developed. Any format specifiers, even common ones like \n, are currently neither recognized nor processed.

Notando 1.1.1 operates by default from a .notando directory in your home directory, though this can be customized.

You're explicitely encouraged to check out the actual code yourself at [GitHub](https://github.com/NinaTolfersheimer/Notando/).

## Terms of Use, Licences & stuff
This is open-source software. However, there is a separate file somewhere in your initial installation directory or [over on the project's GitHub page](https://github.com/NinaTolfersheimer/Notando/) that explains Notando's usage of your data and that further encourages you to handle this as an open-source project when editing or sharing.

## About the author
_Notando has been created and is maintained by [Nina Tolfersheimer](https://github.com/NinaTolfersheimer). Make sure to check out [my projects website](https://ninatolfersheimer.github.io) to look for other projects you may like_ 😉
