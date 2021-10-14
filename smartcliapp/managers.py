import sys

import click

from smartcliapp.printers import Printer


class ActionMan:
    printer = Printer()

    @classmethod
    def get_action(cls, title: str) -> bool:
        while 1:
            cls.printer.default.echo(f'{title} [y/n/e]: ')
            char = click.getchar()

            if char.lower() in ('y', ):
                return True
            elif char.lower() in ('n',):
                return False
            elif char.lower() in ('e', ):
                sys.exit(0)


class LaunchMan:
    @classmethod
    def launch(cls, url):
        click.launch(url)


class InputMan:
    @classmethod
    def input(cls, title):
        return input(f'{title}: ')

    @classmethod
    def prompt(cls, title):
        return click.prompt(title)


class StatusMan:
    printer = Printer()

    @classmethod
    def show_status(cls, status, show=True):
        msg = 'Ok!' if status else 'Error!'
        if show:
            cls.printer.default.echo(msg)
        return msg


class ClickMan:
    printer = Printer()
    input_man = InputMan()
    status_man = StatusMan()
    action_man = ActionMan()
    launcher = LaunchMan()
