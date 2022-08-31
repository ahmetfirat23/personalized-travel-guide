# Welcome to Personalized Travel Guide (PTG)!

Hi! Personalized Travel Guide (PTG) is an AI powered software that generates travel guide for travelers depending on their flight history.


# Quick Start

Quick start to test out PTG and get a sample with default configurations and preset database. All random seeds are set to 42.

## Requirements

This project is written with python and utilizes scikit-learn, matplotlib, pandas, numpy, requests, beautifulsoup and sqlite. Also it creates city info database by using scrapy, scrapy-splash and docker. A new image of splash should be started in Docker if a new  database will be created.

## Starting the program
You can start main.py and wait until the html file is loaded. Then turn back to program window to create another file.

# Connecting to the real data

You can run PTG with your own passenger data. 
To connect your own data you need to modify **main.py**. Find the line starts with **trimmed_data** and change **mdg.generate_mock_data** function with your own data. Data must be in pandas DataFrame format and it's column names are city names. Indexes are passengers and values are the count of how many times passenger visited that city.
To add the target passenger change **pass_name** to your passenger's name and modify **target_passenger** to passenger's data. Passenger's data is formatted the same way previous data with only one index. 
To change where passenger flies from modify the last argument in **fetcher.fetch_flight** function to your airport code. Airport codes can be gathered from **city_dict** with city name.
After connecting you can use **inspection.ipynb** file to tune the k-means model.
Remember that all random seeds set to 42. Remove all 42's before using for actual results.

# Creating info database

All city info scraped from TripAdvisor. To re-create the database delete sample.db, run splash image in docker and start main.py again. Scraper scrapes for the cities it gets from **fetcher.fetch_api** and outputs **sample.db** in main folder. Be aware creation of database may take a long time.

# Output and displaying 

Output html file is created in **site_template** folder named same as passenger's name with it's generated javascript file **script.js** (Be aware that javascript file is named same for different html files. If you create many html files consecutively it will only work for the last one).  Also CSS file is in the same folder with the name **style.css**. You can make modifications at both **html_editor** and **template_html** to modify the output.
