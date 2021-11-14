# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
import sys

import click
from smartprinter.printers import Printer


class CliManager:

    def __init__(self):
        self.printer = Printer()

    def to_continue(self, msg=None):
        if msg is None:
            msg = 'Enter to continue...'
        return self.input(msg)

    @staticmethod
    def input(msg):
        return input(msg)

    def get_action(self, title: str) -> bool:
        """
        Get Action

        - Yes, No , Exit

        :param title: Title string
        :return: <bool> - yes/no True/False
        """
        while 1:
            self.printer.base.echo(f'{title} [y/n/e]: ')
            char = click.getchar()

            if char.lower() in ('y', 'н',):
                return True
            elif char.lower() in ('n', 'т',):
                return False
            elif char.lower() in ('e', 'у'):
                sys.exit(0)

    @staticmethod
    def launch(url):
        """
        Launch the default browser to follow the specified link.

        :param url: <str> url;
        :return: None;
        """
        click.launch(url)

    @classmethod
    def prompt(cls, title, hide_input=False):
        """
        Click input.

        :param title: <str> title;
        :param hide_input: <bool> - hidden input. y/n True/False
        :return:
        """
        return click.prompt(title, hide_input=hide_input)

    def show_status(self, status, show=True):
        """
        Status output.

        :param status: <bool> - True/False;
        :param show: <bool> - Print to Console/Do Not Print;
        :return: <str> status message;
        """
        msg = 'Ok!' if status else 'Error!'
        if show:
            self.printer.base.echo(msg)
        return msg
