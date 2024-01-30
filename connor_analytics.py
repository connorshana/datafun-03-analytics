"""Econest_Analytics_py

Python module for Module 03 Data Analytics skills competance demonstration.
"""


#Import Dependencies
# Standard library imports
import csv
import json
import pathlib
import pandas as pd
from collections import Counter

# External library imports (requires virtual environment)
import requests
url = "https://www.gutenberg.org/cache/epub/1112/pg1112.txt"

# Local module imports
import econest_utils
import Shana_projsetup



# Data Acquisition - fetch data from specified web APIs or online data sources.
import requests

# Fetch and save text data
def fetch_and_write_text_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and writing text data: {e}")

 # Fetch and save csv data
def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.content.decode ('utf-8'))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and writing csv data: {e}")

# Fetch and save excel data
def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and writing excel data: {e}")

# Fetch and save json data
def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and writing json data: {e}")


#Write data - write functions to save content to different file types.
from pathlib import Path

#Function 1.  Process Text Data
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

#Function 2.  Process CSV Data
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w' , newline= '', encoding='utf-8') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

#Function 3.  Process Excel Data
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

#Function 4.  Process json Data
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")


#Process data and generate output - also includes exception handling.
def process_txt_data(input_file, output_file):
    # Count occurences of each word in the input file
    try:

        with open(input_file, 'r') as file:
            text = file.read()
        words = text.split()
        word_count = Counter(words)

        with open(output_file, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
        print (f"Word count saved to {output_file}")
    except Exception as e:
        print(f"Error processing text data: {e}")
def process_csv_data(input_file, output_file):
    # Calculate the average length of words in the input file
    try:
        df = pd.read_csv(input_file)
        word_lengths = df['word'].str.len()
        avg_word_length = word_lengths.mean()
        with open(output_file, 'w') as file:
            file.write(f"Average word length: {avg_word_length}\n")
        print(f"Average word length saved to {output_file}")
    except Exception as e:
        print(f"Error processing csv data: {e}")

def process_excel_data(input_file, output_file):
    # Calculate the average length of words in the input file
    try:
        df = pd.read_excel(input_file)
        word_lengths = df['word'].str.len()
        avg_word_length = word_lengths.mean()
        with open(output_file, 'w') as file:
            file.write(f"Average word length: {avg_word_length}\n")
        print(f"Average word length saved to {output_file}")
    except Exception as e:
        print(f"Error processing excel data: {e}")

def process_json_data(input_file, output_file):
    # Calculate the average length of words in the input file
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        word_lengths = [len(word) for word in data]
        avg_word_length = sum(word_lengths) / len(word_lengths)
        with open(output_file, 'w') as file:
            file.write(f"Average word length: {avg_word_length}\n")
        print(f"Average word length saved to {output_file}")
    except Exception as e:
        print(f"Error processing json data: {e}")

#Main Function - Implement process functions and call main function
def main():
    """Main functions to implement a main() function to test the folder creation functions and demonstrate the use of imported modules ."""

    print("Welcome to the Module 03 Data Analytics skills competance demonstration")

# URLs for different data types   
url_text = "https://www.gutenberg.org/files/1342/1342-0.txt"
url_csv = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_excel = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_json = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

# Folder and file names for different data types
txt_folder_name = 'data/text'
csv_folder_name = 'data/csv'
excel_folder_name = 'data/excel'
json_folder_name = 'data/json'

folder_name = "data"
txt_filename = "text_data.txt"
csv_filename = "csv_data.csv"
excel_filename = "excel_data.xlsx"
json_filename = "json_data.json"

# Fetch and write data for all types
fetch_and_write_text_data(txt_folder_name, txt_filename, url_text)
fetch_and_write_csv_data(csv_folder_name, csv_filename, url_csv)
fetch_and_write_excel_data(excel_folder_name, excel_filename, url_excel)
fetch_and_write_json_data(json_folder_name, json_filename, url_json)

# Process data and generate output
# Process text data
process_txt_data(txt_filename, "output_text.txt")

# Process CSV data
process_csv_data(csv_filename, "output_csv.txt")

# Process Excel data
process_excel_data(excel_filename, "output_excel.txt")

# Process JSON data
process_json_data(json_filename, "output_json.txt")

# Conditional Script Execution

if __name__ == "__main__":
    main()


            
       





