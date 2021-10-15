# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# This example is for reference, so it contains
# coding best practices are not used.
import click
from smartcliapp.informers import Informer
from smartcliapp.managers import ClickMan  # Importing ClickMan


# Create class CommandMan
class CommandMan:
    # Create method area in CommandMan.
    @classmethod
    def area(cls, width=0, height=0):
        return width * height

    @classmethod
    def open_url(cls, url):
        ClickMan.launcher.launch(url)
        return url


class CLiManager(Informer):
    # ClickMan can be used without creating an object, but we will create
    # an object inside CliManager for convenience.
    click_man = ClickMan()
    # Adding the CommandMan to the CliManager.
    command_man = CommandMan()
    name = 'smartcliapp'
    title = 'Smart Cli App'
    description = 'Tools for creating console applications'
    copyright = 'Copyright © 2018-2021, A.A Suvorov'
    url = 'https://github.com/smartlegionlab'
    version = '0.1.1'


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.pass_context  # Using context to get information about commands.
def cli(ctx):
    CLiManager.show_head()
    # We use a condition that will help us run the application without commands and using commands independently.
    if ctx.invoked_subcommand is None:
        # We use an action request in our application, an exit, a message display, or an immediate exit.
        action = ClickMan.action_man.get_action('Do you want to continue?')
        if action:
            ClickMan.printer.default.echo('Hello World!)')

        CLiManager.show_footer()


# We create a command.
@cli.command(name='url')
def open_url():
    # We use the class inherited from Informer to launch the browser with our url
    url = CLiManager.url
    msg = f'Open url: {url}'
    CLiManager.command_man.open_url(url)
    return msg


# We create a command.
@cli.command(name='area')
@click.option('-w', '--width', default=0, type=click.INT)
@click.option('-h', '--height', default=0, type=click.INT)
def area(width, height):
    # We run the area method inside our command to get the result.
    result = CLiManager.command_man.area(width=width, height=height)
    # We can also return the result from our command to the process_result
    # function and output it from there.
    return result


# We use the process_result function to get the result of executing our command,
# and display the footer after the command completes.
@cli.result_callback()
def process_result(result):
    if result is not None:
        CLiManager.printer.default.echo(f'Result: {result}')
        CLiManager.show_footer()


if __name__ == '__main__':
    cli()
