import requests


headers = {
    'x-rapidapi-key': "74e1fb5b7fmsh14d2a74da2e8e9fp1f9f86jsnd99d8e3ec5d9",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}


def get_covid_data():
    response = requests.request(
        "GET", "https://covid-19-data.p.rapidapi.com/totals", headers=headers)
    return response.json()[0]


def get_covid():
    resp = requests.get('https://data.cdc.gov/resource/ynw2-4viq.json')
    resp = resp.json()
    all_ages_dead_cov = resp[0]['total_deaths']
    all_ages_dead_pneumonia = resp[0]['pneumonia_deaths']
    zero2seventeen_dead_cov = resp[1]['total_deaths']
    zero2seventeen_dead_pneumonia = resp[1]['pneumonia_deaths']
    eighteen2sixtyfour_dead_cov = resp[2]['total_deaths']
    eighteen2sixtyfour_dead_pneumonia = resp[2]['pneumonia_deaths']
    sixty5plus_dead_cov = resp[3]['total_deaths']
    sixty5plus_dead_pneumonia = resp[3]['pneumonia_deaths']
    return all_ages_dead_cov, all_ages_dead_pneumonia, zero2seventeen_dead_cov, zero2seventeen_dead_pneumonia, eighteen2sixtyfour_dead_cov, eighteen2sixtyfour_dead_pneumonia, sixty5plus_dead_cov, sixty5plus_dead_pneumonia