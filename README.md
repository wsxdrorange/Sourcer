# Sourcer

Automatic email sourcing for potential clients using Hunter.io API and LinkedIn Web Scraping. Fill emails on an existing contact CSV or pull new data from Linkedin to generate client emails.

## Usage

```
python3 main.py
```

Two Methods of Usage:
1. Existing CSV
   To fill out Emails in an existing CSV, the input CSV should have the following exact columns correctly completed already: `First Name`, `Last Name`, `Company`. Furthermore, the input CSV should have an `Email Address` column which will be filled after running Sourcer. Your CSV can have other columns however the previous are required for Sourcer to work. No specific naming conventions or path location is necessary since these can be specified at runtime. `sourcing_example.csv` provides a valid example of an existing CSV.
2. LinkedIn Web Scraping
   Alteratively, Sourcer can pull new data off LinkedIn. To generate new sourcing data, specify the companies, positions, and number of contacts you wish to source and a completed CSV will be generated.

### Hunter.io API Key

Because Sourcer uses Hunter.io's API, individual users are required to create an API Key to use (API Requests are throttled). To generate a Hunter.io API Key, visit [Hunter.io](https://www.hunter.io) to create an account. After creating an account, you are able to access your personal API Key and view your Hunter.io API Usage.

## Dependencies

`pip install -r requirements.txt`

Necessary packages: requests