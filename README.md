GOTO
====

A simple python module to help preserve your sanity when working in multiple directories in the command line.

####requirements: 

- python3 

- python click module 





How to install:
```
1) put g2dict in your /usr/local/bin or wherever 
   and symlink it to /bin/g2dict so you can use it anywhere

2) copy the contents of goto.sh to your .bashrc (or .zshrc or whatever) file 

3) open a new shell 
```   


Add a new path alias with with `g2dict -a [ALIAS] [-t TARGET]`. The target can be relative to your current directory. If no target is supplied, the current directory will be assumed. 

You can add an alias with spaces by putting quotes around it, providing you also use them when running the goto command.


Entries are stored in a json file `.g2dict` in your home folder. G2dict will create it if it isn't there, so you can safely delete it (you will lose your aliases ofcourse). 

jump to a directory with `goto [ALIAS]`, you can jump back to the previous directory with 'goto prev'

