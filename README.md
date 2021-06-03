# Notando
_A small open-source alternative to MS OneNote etc. Notando is still under construction and currently runs in v0.2.0_

## What Notando 0.2.0 can do
Notando 0.2.0 presents you with a menu to choose options from. You can:

1. Take a note – _Allows you to take a note and store it in a specific category. This will take some string and store in a file with the path _ ```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
The so-called 'standard path' is by default the path to the directory where Notando lives itself, though it can be customized._
2. Read your notes – _Lets you read a specified note. This will ask for the category the note is stored within as well as the headline you gave it. It will then try to read from the path _```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
_and present you with the content of the specified text file._
3. Edit a note – _Allows you to 'edit' a note, although you can currently only write to the file's end. This performs essemtially the same task as read would have done, but after presenting the file's content, edit will take some string, add it to the end of the content, and re-write the file to the provided path._
4. Remove a note – _Allows you to permanently and irreversibly delete a note. Takes a category and a headline and removes the file at the path _```<standard path>/.notando/notes/<provided category>/<provided headline>.txt```
5. set Preferences – _You enter the following prefs sub-menu:_
  * Make a category – _Allows you to set up a new category. Takes a name and tries to make a directory with_ ```<standard path>/.notando/notes/<provided category>/```
  * Remove a category – _Allows you to delete a category permanently and irreversibly. Takes a name and tries to remove the directory with_ ```<standard path>/.notando/notes/<provided category>/``` _recursively._
  * Rename a category – _Allows you to rename a category. Takes an old and a new name and then tries to rename_ ```<standard path>/.notando/notes/<old name>/``` _to_ ```<standard path>/.notando/notes/<new name>/``` 
  * Copy Notando – _Allows you to make a backup of Notando including all the notes and preferences. Takes a path to a directory **THAT IS NOT YET TO EXIST**, deletes this directory recursively if it already exists (useful for regular backing up to the same location), re-makes it, and copies the .notando directory currently set as standard path to the new directory_
_Note that this won't actually make a back up but simply copy the entire installation to the provided location_
  * Change standard path – _Allows you to store your **new** notes after this change to another directory. Takes that directory's path and overwrites the_ ```<standard path>/.notando/preferences/stdpath.txt``` _file with this new content. Note that you'll have to change the path back if you wish to manage the notes you've added before this change._ 
  * Quit submenu and return to main menu – _Effectively sends a terminate signal which collapses the sub-menu and shows the main menu._
6. Quit – _Sends a terminating signal to exit the program._ `KeyboardInterrupt` / `Ctrl + C` _should work as well._

## How Notando 0.2.0 works
Notando 0.2.0 lets you take and manage notes and organizes them into _categories_. Those categories are effectively the directories the specific note files live in.

Notando 0.2.0 stores your notes as plain .txt files, but an update to a markup language is currently developed. No format specifiers, even common ones like \n, are currently neither recognized nor processed.

Notando 0.2.0 operates by default from a .notando directory somewhere within your device or network, though this can be customized.

You're explicitely encouraged to check out the actual code yourself at [GitHub](https://github.com/NinaTolfersheimer/Notando/).

## Terms of Use, Licences & stuff
There is a separate policy somewhere, and a default one over on [Nina Tolfersheimer's GitHub](https://github.com/NinaTolfersheimer/Notando/). However, those might not be the valid ones and may differ from the valid one! The only valid policy is the one you're presented with while installing through an installer script and that should be stored somewhere within the initial release directory. The default policy on GitHub is only valid for your specific installation if your initial resource lacks such a policy for some reason.
Check out those policies for further information!

## About the author
_Notando has been created and is maintained by [Nina Tolfersheimer](https://github.com/NinaTolfersheimer). Make sure to check out [my projects website](https://ninatolfersheimer.github.io) as well as [my blog](http://raspberrypi), if you're located within the same LAN as my computer._ :wink:
