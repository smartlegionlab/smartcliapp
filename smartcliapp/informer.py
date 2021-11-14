# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartprinter.printers import Printer


class Informer:
    """
    Informer
    - Override the attributes to yours.
    """
    printer = Printer()
    name = ''
    title = ''
    description = ''
    copyright = ''
    url = ''
    msg = ''
    version = '0.0.0'

    @classmethod
    def show_head(cls, char='*'):
        """Displays a header with information when the application starts."""
        cls.printer.smart.echo(char=char)
        cls.printer.smart.echo(cls.title, char=char)
        cls.printer.smart.echo(cls.description, char=char)

    @classmethod
    def show_footer(cls, char='*'):
        """Displays a footer with information when the application ends."""
        cls.printer.smart.echo(cls.url, char=char)
        cls.printer.smart.echo(cls.copyright, char=char)
        cls.printer.smart.echo(char=char)
