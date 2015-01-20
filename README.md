GOTO
====

A simple python module to help preserve your sanity when working in multiple directories in the command line.

####requirements:#### 

- python3 

- python click module 





How to install:
```
1) put g2dict in your /usr/local/bin or whatever 
   and symlink it to /bin/g2dictso you can use it anywhere

2) copy the contents of goto.sh to your .bashrc/.zshrc/... file 

3) open a new shell 
```   


Add a new path alias with with `g2dict -a [ALIAS] [-t TARGET]`.  
If no target is supplied, the current directory will be
assumed. 

Entries are stored in a json file `.g2dict` in your home folder. You can safely delete it (you will lose your
aliases ofcourse). G2dict will create it if it isn't there.  

jump to a directory with `goto [ALIAS]`

