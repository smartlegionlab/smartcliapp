# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartcliapp.informers import Informer

from smartcliapp.managers import (
    ActionMan,
    LaunchMan,
    InputMan,
    StatusMan,
    ClickMan
)

from smartcliapp.printers import (
    BasePrinter,
    ClickPrinter,
    SmartPrinter,
    PagerPrinter,
    Printer
)


class PrintersFactory:
    """Printers factory"""

    @classmethod
    def get_base(cls):
        """Get base printer"""
        return BasePrinter()

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


class Factory:
    @classmethod
    def get_action_man(cls):
        return ActionMan()

    @classmethod
    def get_launch_man(cls):
        return LaunchMan()

    @classmethod
    def get_input_man(cls):
        return InputMan()

    @classmethod
    def get_status_man(cls):
        return StatusMan()

    @classmethod
    def get_click_man(cls):
        return ClickMan()

    @classmethod
    def get_printer(cls):
        return Printer()

    @classmethod
    def get_informer(cls):
        return Informer()
