from smartcliapp.informers import Informer
from smartcliapp.managers import (
    ActionMan,
    LaunchMan,
    InputMan,
    StatusMan,
    ClickMan
)
from smartcliapp.printers import Printer


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
