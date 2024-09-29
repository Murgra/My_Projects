# Weather Web Scraping

Web scraping and visualization  weather data for the 100 largest cities in Poland.

Weather data comes from the website [https://openweathermap.org]

These are data for 5 days at 3-hour intervals. 

The files in the repository contain data for the days 28-09-2024 to 03-10-2024.

## Getting Started

[<img src="https://images.theconversation.com/files/442675/original/file-20220126-17-1i0g402.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=1356&h=668&fit=crop" width="550"/>](image.png)

### Supported Python Versions

* Python 3.8+

### Installing

You need several libraries to work correctly.
If you have pip on your system, you can simply install the required libraries by using the file requirements.txt:

* requirements.txt file
```
pip install -r requirements.txt
```

* Firefox 

    [Download](https://www.mozilla.org/pl/firefox/download/thanks/)

* API key

    To download weather data, you need an API key to [https://openweathermap.org]. 

    If you don't have one, you can run the dashboard itself using data from the weather_data.csv file (data for the days 28-09-2024 to 03-10-2024).

### Drivers

Selenium requires geckodriver to connect to the browser in order to work. This file must be in the same folder as the application to function properly.

Its absence causes an error.

This file can be found in the repository (Windows 64 version)

Versions for other systems can be popped from: 

[Firefox - geckodriver](https://github.com/mozilla/geckodriver/releases)

### How to run the program

After downloading the files
you should put the application file and csv file in one folder.

Next start code in Web_Scraoing.ipynb file or Visualization.ipynb if you only want to see the dashboard.

After running the code in Web_Scraoing.ipynb file, the browser will open automatically. 


