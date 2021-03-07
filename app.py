from flask import Flask, render_template
import covid
import movies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/apis/covid')
def covidAPI():
    resp = covid.get_covid()
    return render_template("covid.html", resp=resp)


@app.route('/apis/movies')
def moviesAPI():
    results = movies.get_most_popular()
    for result in results:
        result['title'], season = result['title'].split(':')
    return render_template('movies.html', res=results, season=season)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
