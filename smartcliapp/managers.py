# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import sys

import click

from smartcliapp.printers import Printer


class ContinueMan:
    @classmethod
    def to_continue(cls, msg=None):
        if msg is None:
            msg = 'Enter to continue...'
        return input(msg)


class ActionMan:
    printer = Printer()

    @classmethod
    def get_action(cls, title: str) -> bool:
        """
        Get Action

        - Yes, No , Exit

        :param title: Title string
        :return: <bool> - yes/no True/False
        """
        while 1:
            cls.printer.base.echo(f'{title} [y/n/e]: ')
            char = click.getchar()

            if char.lower() in ('y', 'н', ):
                return True
            elif char.lower() in ('n', 'т', ):
                return False
            elif char.lower() in ('e', 'у'):
                sys.exit(0)


class LaunchMan:
    @classmethod
    def launch(cls, url):
        """
        Launch the default browser to follow the specified link.

        :param url: <str> url;
        :return: None;
        """
        click.launch(url)


class InputMan:
    @classmethod
    def input(cls, title):
        """Default input"""
        return input(f'{title}: ')

    @classmethod
    def prompt(cls, title, hide_input=False):
        """
        Click input.

        :param title: <str> title;
        :param hide_input: <bool> - hidden input. y/n True/False
        :return:
        """
        return click.prompt(title, hide_input=hide_input)


class StatusMan:
    printer = Printer()

    @classmethod
    def show_status(cls, status, show=True):
        """
        Status output.

        :param status: <bool> - True/False;
        :param show: <bool> - Print to Console/Do Not Print;
        :return: <str> status message;
        """
        msg = 'Ok!' if status else 'Error!'
        if show:
            cls.printer.base.echo(msg)
        return msg


class ClickMan:
    """A versatile manager"""
    printer = Printer()
    input_man = InputMan()
    status_man = StatusMan()
    action_man = ActionMan()
    launch_man = LaunchMan()
    continue_man = ContinueMan()
