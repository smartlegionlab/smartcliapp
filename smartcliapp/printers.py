# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Printers"""
import shutil
from abc import ABC, abstractmethod

import click


class PrinterBase(ABC):

    @abstractmethod
    def echo(self, text=''):
        """Abstract Printer"""


class DefaultPrinter(PrinterBase):
    @classmethod
    def echo(cls, text='', show=True):
        """
        Default printer.

        - Normal console output by default.

        :param show: <bool> - printing to console;
        :param text: string;
        :return: <str> string;
        """
        if show:
            print(text)
        return text


class ClickPrinter(PrinterBase):
    @classmethod
    def echo(cls, text='', show=True, color=None):
        """
        Click printer.

        - Prints a line with the ability to stylize in colors.

        :param text: <str> - string;
        :param show: <bool> - printing to console;
        :param color: <str> - color;
        :return: <str> - styled string;
        """
        msg = click.style(text, fg=color)
        if show:
            click.echo(msg)
        return msg


class PagerPrinter(PrinterBase):
    # Use Click Printer
    _click_printer = ClickPrinter()

    @classmethod
    def echo(cls, text='', show=True, color=None):
        """
        Pager printer.

        - Displays a line inside a pager like less,
        with the ability to move up and down and exit when
        clicking on [q];

        - Using the show parameter, you can additionally
         print to the console, with the ability to stylize with colors.

        :param text: <str> - string;
        :param show: <bool> - printing to console;
        :param color: <str> - color;
        :return: <str> - string;
        """
        try:
            click.echo_via_pager(text)
        except (PermissionError, OSError):
            pass
        cls._click_printer.echo(text=text, show=True, color=color)
        return text


class SmartPrinter(PrinterBase):
    _def = DefaultPrinter()

    @classmethod
    def echo(cls, text='', char='-', show=True):
        """
        Smart printer.

        - Using the size of the width of the console, prints the text centered,
         indented and padded with the specified character.

        :param text: <str> - string;
        :param char: <str> - symbol;
        :param show: <bool> - printing to console;
        :return: <str> - styled string;
        """
        columns = cls._term_width()
        symbol = ' ' if not char else char
        msg = f' {text} '.center(columns, symbol[:1]) \
            if text else f''.center(columns, symbol[:1])
        if show:
            cls._def.echo(msg)
        return msg

    @classmethod
    def _term_width(cls):
        return shutil.get_terminal_size()[0]


class PrintersFactory:
    """Printers factory"""

    @classmethod
    def get_default(cls):
        """Get default printer"""
        return DefaultPrinter()

    @classmethod
    def get_click(cls):
        """Get click printer"""
        return ClickPrinter()

    @classmethod
    def get_smart(cls):
        return SmartPrinter()

    @classmethod
    def get_pager(cls):
        return PagerPrinter()


class Printer:
    """Multifunction Printer"""
    factory = PrintersFactory()
    default = DefaultPrinter()
    click = ClickPrinter()
    pager = PagerPrinter()
    smart = SmartPrinter()
