import requests


headers = {
    'x-rapidapi-key': "74e1fb5b7fmsh14d2a74da2e8e9fp1f9f86jsnd99d8e3ec5d9",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}


def get_covid_data():
    response = requests.request(
        "GET", "https://covid-19-data.p.rapidapi.com/totals", headers=headers)
    return response.json()[0]
