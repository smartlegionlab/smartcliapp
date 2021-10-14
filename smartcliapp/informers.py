from smartcliapp.managers import LaunchMan
from smartcliapp.printers import Printer


class Informer:
    printer = Printer()
    launcher = LaunchMan()
    name = ''
    title = ''
    description = ''
    copyright = ''
    url = ''
    msg = ''
    version = '0.0.0'

    @classmethod
    def show_head(cls):
        cls.printer.smart.echo(char='*')
        cls.printer.smart.echo(cls.title, char='*')
        cls.printer.smart.echo(cls.description, char='*')

    @classmethod
    def show_footer(cls):
        cls.printer.smart.echo(cls.url, char='*')
        cls.printer.smart.echo(cls.copyright, char='*')
        cls.printer.smart.echo(char='*')

    @classmethod
    def site(cls):
        cls.launcher.launch(cls.url)
