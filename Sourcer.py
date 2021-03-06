import numpy as np
import pandas as pd
import requests

#Sourcer Class to handle all sourcing functionality
class Sourcer:
    def __init__(self, hunter_api_key):
        self.hunter_api_key = hunter_api_key 
        self.client_info_df = None

    #Create new client info dataframe using linkedin API
    def generate_client_info_df(self, companies, roles, num_contacts):
        return

    #Read existing client info csv into dataframe
    #Assuming client_info is all filled in except for email address (Columns: First Name, Last Name, Full Name, Company)
    def read_client_info_csv(self, path):
        self.client_info_df = pd.read_csv(path, delimiter=',')
        self.client_info_df = self.client_info_df.dropna(thresh=5) #Remove nan rows with at least 5 non Nan values in columns
        self.fill_emails()

    #Fills emails based on client_info_csv using hunter.io API, mutates existing objects client_info_df
    #Writes only sourced email addresses as CSV to Emails.csv
    def fill_emails(self):

        #Applied function to get email for individual based on company pattern
        def replace_email_format(company, firstName, lastName):
            pattern = email_address_map[company]
            email_address = pattern
            email_address = email_address.replace('{first}', firstName)
            email_address = email_address.replace('{last}', lastName)
            email_address = email_address.replace('{f}', firstName[0:1])
            return email_address

        #Read email address mappings
        email_address_map = {}
        companies = self.client_info_df.Company.unique()
        for company in companies:
            #API call to Hunter.io to get email format
            hunter_resp = requests.get('https://api.hunter.io/v2/domain-search?company=' + company + '&api_key=' + self.hunter_api_key)
            if hunter_resp.status_code != 200:
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            pattern = hunter_resp.json()['data']['pattern'] + '@' + hunter_resp.json()['data']['domain']
            email_address_map[company] = pattern

        # Replace email address column with valid emails
        self.client_info_df['Email Address'] = self.client_info_df.apply(lambda row : replace_email_format(row['Company'], row['First Name'], row['Last Name']), axis=1)
        print(self.client_info_df)

        #Write Email Addresses Only to output CSV
        email_address_df = self.client_info_df['Email Address']
        email_address_df.to_csv('Emails.csv', header=False)

    #Write client info dataframe to output csv for use
    def write_client_info_csv(self, path):
        self.client_info_df.to_csv(path)

    
    