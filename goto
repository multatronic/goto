#!/usr/bin/env python3
# @python3
# @author sabot <sabot@inuits.eu>
"""Switch directories without wearing out your slash key"""
import sys
import os
import json
import click

__VERSION__ = '0.0.1'

# 3 params are needed for click callback
def show_version(ctx, param, value):
    """Print version information and exit."""
    if not value:
        return
    click.echo('Goto %s' % __VERSION__)
    ctx.exit() # quit the program

def add_entry(dictionary, filepath, path, alias):
    """Add a new path alias."""
    print("Adding alias {} for path {} ".format(alias,path))
    dictionary[alias] = path

    try:
        jsondata = json.dumps(dictionary, sort_keys=True)
        fd = open(filepath, 'w')
        fd.write(jsondata)
        fd.close()
    except Exception as e:
        print('Error writing to dictionary file: ', str(e))
        pass

def get_entries(filename):
    """Get the alias entries in json."""
    returndata = {}
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            fd = open(filename, 'r')
            entries = fd.read()
            fd.close()
            returndata = json.loads(entries)

        except Exception as e:
            print('Error reading dictionary file: ', str(e))
            pass
    else:
        print('Dictionary file not found or empty- spawning new one in', filename)
        newfile = open(filename,'w')
        newfile.write('')
        newfile.close()

    return returndata

@click.command()
@click.option('--version', '-v', is_flag=True, is_eager=True,
              help='Print version information and exit.', expose_value=False,
              callback=show_version)
@click.option('--add', '-a', help="Add a new path alias")
@click.option('--target', '-t', help="Alias target path instead of the current directory")
@click.argument('alias', default='currentdir')
@click.pass_context
def goto(ctx, add, alias, target):
    '''Go to any directory in your filesystem''' 

    # load dictionary
    filepath = os.path.join(os.getenv('HOME'), '.g2dict')
    dictionary = get_entries(filepath)

    # add a path alias to the dictionary
    if add:
        if target: # don't use current dir as target
            if not os.path.exists(target):
                print('Target path not found!')
                ctx.exit()
            else:
                add_entry(dictionary, filepath, target, add)
        else: # use current dir as target
            current_dir = os.getcwd()
            add_entry(dictionary, filepath, current_dir, add)

    elif alias != 'currentdir':
        if alias in dictionary:
            entry = dictionary[alias]
            print('jumping to ',entry)
            os.chdir(entry)
        elif alias == 'hell':
            print("Could not locate C:\Documents and settings")
        else:
            print("Alias not found in dictionary - did you forget to add it?")

if __name__ == '__main__':
    goto()
