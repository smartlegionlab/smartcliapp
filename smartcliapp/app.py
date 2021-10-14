# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import click

from smartcliapp.informers import Informer
from smartcliapp import __version__
from smartcliapp.managers import ClickMan


class CommandMan:
    @classmethod
    def one(cls, argument):
        print(f'Start one command with argument: [{argument}]')

    @classmethod
    def two(cls, options):
        print(f'Start two command with options: {options}')


class CliMan(Informer):
    command_man = CommandMan()
    click_man = ClickMan()
    name = 'smartcliapp'
    title = 'Smart Cli App'
    description = 'A cross-platform library.'
    url = 'https://github.com/smartlegionlab'
    copyright = 'Copyright © 2018-2021, A.A Suvorov'
    version = __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']},invoke_without_command=True)
@click.version_option(version=f'{CliMan.name} {CliMan.version}; {CliMan.copyright};')
@click.pass_context
def cli(ctx):
    CliMan.show_head()
    if ctx.invoked_subcommand is None:
        print('Hello World!')


@cli.command(name='one')
@click.argument('msg')
def one(msg):
    CliMan.command_man.one(argument=msg)


@cli.command(name='two')
@click.option('-m', '--message', multiple=True, type=click.STRING)
def two(message):
    CliMan.command_man.two(options=message)


@cli.command(name='site')
def site():
    CliMan.click_man.printer.default.echo(f'Open: {CliMan.url}')
    CliMan.click_man.launcher.launch(CliMan.url)


@cli.result_callback()
def process_result(result):
    CliMan.show_footer()
