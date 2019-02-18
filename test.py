#!/usr/bin/env python

import click

@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--debug', is_flag=True, help="Will print debug messages.")
@click.group()
def test(verbose, debug):
    if verbose:
        click.echo('Verbose is on')
    if debug:
        click.echo('Debug is on')
    pass

@test.command()
@click.argument('name')
def create(name):
    '''Create ...'''
    click.echo('test create with %s' % name)

@test.command()
@click.argument('name')
def run(name):
    '''Run ...'''
    click.echo('test run with %s' % name)

@test.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

def main():
    test()


if __name__ == '__main__':
    main()
