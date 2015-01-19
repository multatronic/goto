#!/usr/bin/env python3
# @python3
# @author sabot <sabot@inuits.eu>
"""Go to any directory without typing a bunch of slashes"""
import sys
import click

__VERSION__ = '0.0.1'

def show_version(ctx, param, value):
    """Print version information and exit."""
    if not value:
        return
    click.echo('Goto %s' % __VERSION__)
    ctx.exit()

@click.command()
@click.option('--version', '-v', is_flag=True, is_eager=True,
              help='Print version information and exit.', expose_value=False,
              callback=show_version)
@click.pass_context
def goto(ctx):
    '''Go to any directory in your filesystem'''
    print("this is where the magic happens.\nCome back later")

if __name__ == '__main__':
    goto()
