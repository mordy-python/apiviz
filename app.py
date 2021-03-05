from flask import Flask, render_template
import covid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apis/covid')
def covidAPI():
    resp = covid.get_covid()
    return render_template("covid.html", resp=resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
