from Sourcer import Sourcer

def main():
    print('Email Sourcer:\n')
    existing_csv_ind = input('Do you have an existing CSV to fill client email addresses (y/n)? ')
    hunter_api_key = input('Enter hunter.io api key: ')

    if existing_csv_ind == 'y':
        read_path = input('Enter existing CSV path: ')
        write_path = input('Enter path to write filled CSV to (Can be same path to replace): ')
        sourcer = Sourcer(hunter_api_key)
        sourcer.read_client_info_csv(read_path)
        sourcer.write_client_info_csv(write_path)

    elif existing_csv_ind == 'n':
        companies = input('Enter comma separated list of companies to source emails from (no spaces): ')
        num_contacts = int(input('Enter num contacts to source for each company (int): '))
        roles = input('Enter comma separated list of roles (e.g. Data Scientist,Product Manager,etc.)')
        write_path = input('Enter path to write filled CSV to: ')
        sourcer = Sourcer(hunter_api_key)
        sourcer.generate_client_info_df(companies.split(','), roles.split(','), num_contacts)
        sourcer.write_client_info_csv(write_path)
        


    return 0

if __name__ == "__main__":
    main()