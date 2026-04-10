# smartcliapp <sup>v1.0.0</sup>

Cross-platform library of tools for creating console applications, based on the click library.
Use a variety of out-of-the-box tools to create console applications.

---

[![PyPI Downloads](https://static.pepy.tech/badge/smartcliapp)](https://pepy.tech/projects/smartcliapp)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartcliapp)](https://github.com/smartlegionlab/smartcliapp/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartcliapp?label=pypi%20downloads)](https://pypi.org/project/smartcliapp/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartcliapp)
[![PyPI](https://img.shields.io/pypi/v/smartcliapp)](https://pypi.org/project/smartcliapp)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartcliapp)](https://github.com/smartlegionlab/smartcliapp/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartcliapp)](https://pypi.org/project/smartcliapp)

---

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).


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

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/smartcliapp/blob/master/DISCLAIMER.md)

---

## Help:

### Install:

- `pip install smartcliapp`

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

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/smartcliapp/blob/master/LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)

---

