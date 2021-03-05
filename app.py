from flask import Flask, render_template
import covid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apis/covid')
def covidAPI():
    resp = covid.get_covid_data()
    dateUpdated, timeUpdated = resp['lastUpdate'].split('T')
    timeUpdated, plus = timeUpdated.split('+')
    del(plus) # delete the plus variable
    return render_template("index.html", resp=resp, dateUpdated=dateUpdated, timeUpdated=timeUpdated)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
