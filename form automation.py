
import pandas as pd
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials

# Load Excel data
excel_file_path = 'D:\Documents\Book1.xlsx'
data = pd.read_excel(excel_file_path)

# Google Forms details
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSc97nynOdV-Lkv_RNIkg299E6j-7c0WnrBaldDGOyKddyYGIw/formResponse'
form_fields = {
    'Id': 'entry.990718071',
    'First Name': 'entry.1526819227',
    'Rollnumber': 'entry.1787411923',
    'Last Name': 'entry.168361485',
    'Ph.No': 'entry.612173357'
    # Add more fields as necessary
}

# Function to submit a single row to Google Form
def submit_to_google_form(row):
    form_data = {}
    for column, entry_id in form_fields.items():
        form_data[entry_id] = row[column]
    
    response = requests.post(form_url, data=form_data)
    return response

# Iterate over rows and submit data
for index, row in data.iterrows():
    response = submit_to_google_form(row)
    if response.status_code == 200:
        print(f"Successfully submitted row {index + 1}")
    else:
        print(f"Failed to submit row {index + 1}: {response.status_code}")

# End code