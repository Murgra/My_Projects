# Flight analysis 

This is the final project that completes the CodersLab data analyst course.

It was aimed at analyzing data on: aircraft, airports, weather and flights.

This task has been divided into several sections

* creation of a mechanism that retrieves data from the provided API
* creation of a database used for analytical and reporting purposes
* feeding the downloaded data into the database
* performing an exploratory analysis of the dataset
* creating an operational report


## Getting Started

You need an API key from CodersLab to download data for analysis.

If you don't have it, you can use the downloaded data that is located in the folder: Raw_data

You can also download them here: [Download](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations)

### Supported Python Versions

* Python 3.8+

### Supported MySQL Versions

* MySQL Workbench 8.0.36+

### Installing

* If you have pip on your system, you can simply install or upgrade the Python bindings:
    ```
    pip install pyperclip
    ```

### Folder structure
```
project                <-- main folder
|____ data             <-- folder with initial data
|   |__ airports.csv   <-- list with airport id 
|   |___readme.txt     <-- documentation of the data available in the API
|
|____ notebooks        <-- folder with *.ipynb and .cvs files (created during analysis)
|
|____ Raw_data         <-- folder with downloaded raw data files
|____ sql              <-- folder with sql files
|____ requirements.txt <-- file with the required list of libraries to recreate the virtual environment
```

![Image](https://images.saymedia-content.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:eco%2Cw_1200/MjAwMTUwMjI4Mzc1NDQ2NjM2/disadvantages-of-travelling-by-plane.jpg "icon")