GOTO
====

A simple python module to help preserve your sanity when working in multiple directories in the command line.

requirements:
    * python3
    * python click module

How to install: 
    - put g2dict in your /usr/local/bin or whatever, symlink it to /bin/g2dict so you can use it anywhere
    - copy the contents of goto.sh to your .bashrc/.zshrc/... file 
    - open a new shell 
   


Add a new path alies with with `g2dict -a [ALIAS] [-t TARGET]`. If no target is supplied, the current directory will be
assumed. Entries are stored in a json file `.g2dict` in your home folder. You can safely delete it (you will lose your
aliases ofcourse), g2dict will create it if it isn't there.  

jump to a directory with `goto [ALIAS]`

