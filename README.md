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

- One example is the console utility : [github-ssh-key](https://github.com/smartlegionlab/github-ssh-key)

***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## What's new?

___smartcliapp v0.3.0___

- New opportunities.
- Clearer description.
- A more informative example.

## Warning!

The package is under active development, so new versions
may not be compatible with the old ones.

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

```python
from smartcliapp import Informer, CliManager

class CliMan(Informer):
    tools = CliManager()
    name = 'App Name'
    title = 'App title'
    description = 'App Description'
    copyright = 'App copyright'
    url = 'app url'
    msg = ''
    version = '0.0.0'

```

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

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
