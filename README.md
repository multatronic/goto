GOTO
====

A python/bashscript combo to bookmark directories in the command line.

####requirements: 

- python3 

- python click module 





How to install:
```
1) symlink g2dict to any of your $PATH directories so you can use it anywhere

2) Append the contents of goto to your .bashrc (or .zshrc or whatever) file. 

3) open a new shell
```  


Add a new path alias with with `goto -a [ALIAS] [-t TARGET]`. The target can be relative to your current directory. If no target is supplied, the current directory will be assumed. 

You can add an alias with spaces by putting quotes around it, providing you also use them when jumping to the directory.


Entries are stored in a json file `.g2dict` in your home folder. G2dict will create it if it isn't there, so you can safely delete it (you will lose your aliases ofcourse). 

jump to a directory with `goto [ALIAS]`, you can jump back to the previous directory with `goto prev`

delete entries with `goto -d [ALIAS]`

scrub dead links with `goto -s`

print list of commands with `goto -h`
