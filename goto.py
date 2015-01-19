#!/usr/bin/env python3
# @python3
# @author sabot <sabot@inuits.eu>
"""Go to any directory without typing a bunch of slashes"""
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

def add_alias(ctx, param, value):
    """Add a new path alias."""
    print("I'll get right on that")

def get_dictionary():
    filepath = os.path.join(os.getenv('HOME'), '.g2dict')
    returndata = {}
    if os.path.exists(filepath):
        try:
            dictfile = open(filepath, 'r')
            entries = dictfile.read()
            dictfile.close()
            returndata = json.read(entries)
        except:
            print('Error reading dictionary file', sys.exc_info()[0])
    else:
        print('Dictionary file not found - spawning new one in', filepath)
        newfile = open(filepath,'w')
        newfile.write('')
        newfile.close()

    return returndata
        

@click.command()
@click.option('--version', '-v', is_flag=True, is_eager=True,
              help='Print version information and exit.', expose_value=False,
              callback=show_version)
@click.option('--add', '-a', help="Add a new path alias") 
@click.pass_context
def goto(ctx, add):
    '''Go to any directory in your filesystem'''
    dictionary = get_dictionary()

    print("this is where the magic happens.\nCome back a little later.")
    if add:
        print('Add parameter detected')

if __name__ == '__main__':
    goto()
