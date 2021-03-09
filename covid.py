import requests
import plotly.express as px

headers = {
    'x-rapidapi-key': "74e1fb5b7fmsh14d2a74da2e8e9fp1f9f86jsnd99d8e3ec5d9",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}


def grape(confirmed, recovered, deaths):
    data = {
        "data": [
            {
                'x': [
                    '',
                    'Confirmed Cases',
                    'Recovered Cases',
                    'Deaths'
                ],
                'y': [
                    '1,000,000',
                    confirmed,
                    recovered,
                    deaths
                ],
                'type':'bar',
            }
        ]
    }
    fig = px.bar(data, x=data['data']
                 [0]['x'], y=data['data'][0]['y'])
    fig.write_image('static/graph.svg')


def get_covid_data():
    response = requests.request(
        "GET", "https://covid-19-data.p.rapidapi.com/totals", headers=headers)
    response = response.json()[0]
    confirmed = response['confirmed']
    recovered = response['recovered']
    deaths = response['deaths']
    lastUpdate = response['lastUpdate'].split('T')[0]
    confirmed = '{:,}'.format(confirmed)
    recovered = '{:,}'.format(recovered)
    deaths = '{:,}'.format(deaths)
    grape(confirmed, recovered, deaths)
    return confirmed, recovered, deaths, lastUpdate
get_covid_data()