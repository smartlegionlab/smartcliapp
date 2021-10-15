from smartcliapp.managers import LaunchMan
from smartcliapp.printers import Printer


class Informer:
    """
    Informer

    - Override the attributes to yours.

    """
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

    @classmethod
    def launch(cls, url=None):
        """Launches the default browser, navigates to your url from the console."""
        site = url or cls.url
        cls.launcher.launch(site)
