# Auto Cookie Clicker

An application to automatically play a coockie clicker for a user-specified amount of time.
Using selenium library and Firefox browser

## Getting Started

[<img src="https://play-lh.googleusercontent.com/Z1MOuuiD05ZN5LkVmMEvKF0mqAc-FknaQ2j8s4dZiO-LSPQX4EEA3RVJdlQEtxe96ok" width="250"/>](image.png)

### Supported Python Versions

* Python 3.8+

### Installing

* If you have pip on your system, you can simply install or upgrade the Python bindings:
    ```
    pip install selenium
    ```
* Firefox 

    [Download](https://www.mozilla.org/pl/firefox/download/thanks/)

### Drivers

Selenium requires geckodriver to connect to the browser in order to work. This file must be in the same folder as the application to function properly.

Its absence causes an error.

This file can be found in the repository (Windows 64 version)

Versions for other systems can be popped from: 

[Firefox - geckodriver](https://github.com/mozilla/geckodriver/releases)

### How to run the program

After downloading the browser
you should put the application file and the geckodriver in one folder.

After running the code in Project_Cookie_Clicker.ipynb file, the browser will open automatically. 
The user will be asked to enter the game time in minutes. 
After the game is finished, the number of cookies/min will be displayed and the program will close the browser. 
