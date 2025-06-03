import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import re
import time

# For transparency, please use this header and url:
headers = {"User-Agent": "LudotecaScraperBot/1.0 (+https://ludotecaenlanube.com)"}
url = "https://ludotecaenlanube.com"

# Step 1
# create a variable named 'response'. Using the 'requests' library assign a get request to the 'url' including custom headers:


#Step 2
# Create a variable 'soup'. Using BeautifulSoup from the 'bs4' library, parse the html content and assign the text to the 'soup' variable:


# Step 3
# Inspect https://ludotecaenlanube.com in a browser and identify how you can target the different sections of the web
# HINT: the gallery is a grid of div's with class of card.


# Step 4
# create a variable 'cards'. Use a bs4 method to find all cards and save them to a list
# Print the length of 'cards'. Run your Docker to test if it is working

pages = []
# Step 5
# Iterate over the 'cards' list and create a dict with the page_name, page_description, page_link, img_link. (In this order)
# On completing each iteration, you should append the dict to pages



# Step 6
# Create a DataFrame using pandas of your scrapings. Then export the DataFrame both as a csv and json to /output


