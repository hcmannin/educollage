# -*- coding: utf-8 -*-
"""BME.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sXgTLCEUFpJeeLYkw-NlSg6H-1oklK5-
"""

import requests

from bs4 import BeautifulSoup

url = "https://catalog.ucsc.edu/en/current/general-catalog/courses/bme-biomolecular-engineering/"

response = requests.get(url)

response

response = response.content

soup = BeautifulSoup(response, 'html.parser')

cat = soup.find("div", class_="courselist")

a_elements = cat.find_all('a')

for a in a_elements:
    span_element = a.find('span')  # Find the <span> element within <a>
    if span_element:  # Check if <span> exists
        span_text = span_element.get_text().strip()
        print('"',span_text,',"')