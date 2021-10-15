# smartcliapp

***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartcliapp)](https://github.com/smartlegionlab/smartcliapp/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartcliapp?label=pypi%20downloads)](https://pypi.org/project/smartcliapp/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartcliapp)
[![PyPI](https://img.shields.io/pypi/v/smartcliapp)](https://pypi.org/project/smartcliapp)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartcliapp)](https://github.com/smartlegionlab/smartcliapp/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartcliapp)](https://pypi.org/project/smartcliapp)

***

## Short Description:
___smartcliapp___ - Cross-platform library of tools for creating console applications, based on the click library.
***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## What's new?

- New opportunities.
- Clearer description.
- A more informative example.

***

## Description:

___smartcliapp___ - Cross-platform library of tools for creating console applications, based on the click library.

Use a variety of out-of-the-box tools to create console applications.

Use [click](https://github.com/pallets/click) to develop console applications. 


### Possibilities:

- Displays the title and footer of the application at startup and shutdown. In the center of the console. 
- Display of name, description, copyright, site address in your application.
- Launch the default browser from the console to go to the specified URL, or to your site.
- Storing meta information about your application in one place. 
- Request for action from the user with an instant response to his input without confirmation, consent, refusal, exit from the application (yes/no/exit).
- Various input methods, including non-display input for passwords.
- Operation status output (Ok!/Error!).
- Different ways of displaying information (normal, in the center of the console with filling with characters, in a pager). 
- Top-level ready-made classes containing the necessary tools. 
- Factory for creating objects.

- Use Informer to display meta information.
- Use ClickMan as a toolbox (Printer, InputMan, StatusMan, ActionMan, Launcher).
- Use Factory to create objects individually.

***

## Help:

### Install:

- `pip3 install smartcliapp`

### Use:

#### When creating your application, use (optional) the following approach:

Start by planning your application,
think about and describe in the code what commands,
attributes and options will be passed to it at startup.

- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install [click](https://github.com/pallets/click) `pip3 install click`
- Create app.py file

file: app.py
```python
import click

@click.group(context_settings={'help_option_names': ['-h', '--help']},invoke_without_command=True)
def cli():
    pass

```

- Import Informer from informers.py module 
- Create your CliManager class
- Inherit CliMan from Informer
- Override attributes
- Use the head and footer output of your application as an example.

```python
import click
from smartcliapp.informers import Informer # Import Informer from informers.py module 


# Create your CliManager class
class CLiManager(Informer): # Inherit CliMan from Informer
    # Override attributes
    name = 'myapp'
    title = 'My App'
    description = 'My one application'
    copyright = 'Copyright © 2018-2021, My App'
    url = 'https://yoursite'
    version = '0.0.0'


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
def cli():
    # Use the head and footer output of your application as an example.
    CLiManager.show_head()
    CLiManager.show_footer()

if __name__ == '__main__':
    cli()

```

- Run your application: `python3 app.py`

##### Output:

    ****************************************************************
    **************************** My App ****************************
    ********************** My one application **********************
    *********************** https://yoursite ***********************
    **************** Copyright © 2018-2021, My App *****************
    ****************************************************************

- Let's add additional features using the class ClickMan
- Importing ClickMan
- ClickMan can be used without creating an object, but we will create 
an object inside CliManager for convenience. Thus, when new instruments appear
we will simply extend our CliManager by adding new objects to it.
- We use an action request in our application, an exit, a message display, or an immediate exit.
- We also use the built-in printer (default) to output information.

```python
import click
from smartcliapp.informers import Informer
from smartcliapp.managers import ClickMan  # Importing ClickMan


class CLiManager(Informer):
    # ClickMan can be used without creating an object, but we will create
    # an object inside CliManager for convenience.
    click_man = ClickMan()
    name = 'myapp'
    title = 'My App'
    description = 'My one application'
    copyright = 'Copyright © 2018-2021, My App'
    url = 'https://yoursite'
    version = '0.0.0'


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
def cli():
    CLiManager.show_head()
    
    # We use an action request in our application, an exit, a message display, or an immediate exit.
    action = ClickMan.action_man.get_action('Do you want to continue?')
    if action:
        ClickMan.printer.default.echo('Hello World!)')
    
    CLiManager.show_footer()


if __name__ == '__main__':
    cli()

```

- Run the app several times and try typing `y`, `n`, `e`.

The application will respond to input immediately, without pressing enter!

#### Output:

    ****************************************************************
    **************************** My App ****************************
    ********************** My one application **********************
    Do you want to continue? [y/n/e]: 
    Hello World!)
    *********************** https://yoursite ***********************
    **************** Copyright © 2018-2021, My App *****************
    ****************************************************************

Let's use another tool:

- Let's create a command to launch the default browser with a transition to our site.

I will use link to my site, you can override url attribute, in your CliManager
and indicate your site, if you have not done so earlier.

- We create a command.
- We use the class inherited from Informer to launch the browser with our url.
- Using context to get information about commands.
- We use a condition that will help us run the application without commands and using commands independently.
- We use the process_result function to get the result of executing our command, 
and display the footer after the command completes. 

```python
import click
from smartcliapp.informers import Informer
from smartcliapp.managers import ClickMan  # Importing ClickMan


class CLiManager(Informer):
    # ClickMan can be used without creating an object, but we will create
    # an object inside CliManager for convenience.
    click_man = ClickMan()
    name = 'myapp'
    title = 'My App'
    description = 'My one application'
    copyright = 'Copyright © 2018-2021, My App'
    url = 'https://github.com/smartlegionlab'
    version = '0.0.0'


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
    CLiManager.launch()


# We use the process_result function to get the result of executing our command, 
# and display the footer after the command completes. 
@cli.result_callback()
def process_result(result):
    CLiManager.show_footer()


if __name__ == '__main__':
    cli()

```

- Run the application using the `url` command: `python3 app.py url`

The default browser will open and go to your site, works even in the Termux!

You can still run your application without any commands: `python3 app.py`

We will remove our command, as it was used to demonstrate the possibility of going to your site. 


I propose to create a new class CommandMan, which will have methods for executing commands.
In this case, all our teams will be in one place, and when a new team is added to our application
we will extend our CommandMan by creating a new method.

Next, we will extend our CliManager by adding a CommandMan object to it so we can use it globally,
in the whole application without creating an object.

Next, create a couple of commands with options and attributes and look at the sequence of our actions.

Let's create a command, for example, we will get the width and height, calculate the area, and display the answer.

- We create a command.
- Create class CommandMan
- Create method area in CommandMan.
- Adding the CommandMan to the CliManager.
- We run the area method inside our command to get the result.
- We can also return the result from our command to the process_result function and output it from there.

```python
import click
from smartcliapp.informers import Informer
from smartcliapp.managers import ClickMan  # Importing ClickMan


# Create class CommandMan
class CommandMan:
    # Create method area in CommandMan.
    @classmethod
    def area(cls, width=0, height=0):
        return width * height


class CLiManager(Informer):
    # ClickMan can be used without creating an object, but we will create
    # an object inside CliManager for convenience.
    click_man = ClickMan()
    # Adding the CommandMan to the CliManager.
    command_man = CommandMan()
    name = 'myapp'
    title = 'My App'
    description = 'My one application'
    copyright = 'Copyright © 2018-2021, My App'
    url = 'https://github.com/smartlegionlab'
    version = '0.0.0'


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
    msg = f'Open url: {CLiManager.url}'
    CLiManager.launch()
    return msg
    


# We create a command.
@cli.command(name='area')
@click.option('-w', '--width', default=0, type=click.INT)
@click.option('-h', '--height', default=0, type=click.INT)
def area(width, height):
    # We run the area method inside our command to get the result.
    result = CLiManager.command_man.area(width=width, height=height)
    CLiManager.printer.click.echo(result)
    # We can also return the result from our command to the process_result function and output it from there.
    return result
    


# We use the process_result function to get the result of executing our command, 
# and display the footer after the command completes. 
@cli.result_callback()
def process_result(result):
    if result is not None:
        CLiManager.printer.default.echo(f'Show result in process_result: {result}')
        CLiManager.show_footer()


if __name__ == '__main__':
    cli()

```

- Run your application with the new command and the required arguments: `python3 app.py area -w 10 -h 10`.

#### Output:

    ****************************************************************
    **************************** My App ****************************
    ********************** My one application **********************
    100
    Show result in process_result: 100
    ************** https://github.com/smartlegionlab ***************
    **************** Copyright © 2018-2021, My App *****************
    ****************************************************************

Use this approach and your application will be extensible and simple. 

- Created a command. 
- Created a method inside CommandMan. 
- We used this method within the team.

***

A small but good example would be the file  [app.py](https://github.com/smartlegionlab/smartcliapp/blob/master/smartcliapp/app.py)
Also, after installing the package, you can run the example by typing :

- `pip3 install smartcliapp`
- `smartcliapp`
- `smartcliapp.py url`
- `smartcliapp.py area -w 10 -h 10`

or:

- `pip3 install -r requirements.txt`
- `python3 smartcliapp.py`
- `python3 smartcliapp.py url`
- `python3 smartcliapp.py area -w 10 -h 10`

***

I spent a lot of time and effort to make my dear friend comfortable and understandable for you,
if you liked my project, my little tutorial, you can always help financially,
for which I will be very grateful to you! Thanks) 

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)


- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)


- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)


- Visa: 4048 0250 0089 5923

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Information:

- Use [click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/main/LICENSE.rst)

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
