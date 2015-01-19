#!/usr/bin/env python3
# @python3
# @author sabot <sabot@inuits.eu>
"""Go to any directory without typing a bunch of slashes"""
import sys
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

@click.command()
@click.option('--version', '-v', is_flag=True, is_eager=True,
              help='Print version information and exit.', expose_value=False,
              callback=show_version)
@click.option('--add', '-a', help="Add a new path alias") 
@click.pass_context
def goto(ctx, add):
    '''Go to any directory in your filesystem'''
    dictionary_file = os.path.join(os.getenv('HOME'), '.g2dict')

    print("this is where the magic happens.\nCome back a little later.")
    if add:
        print('uh yeah dude')

if __name__ == '__main__':
    goto()
