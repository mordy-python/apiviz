from flask import Flask, render_template, url_for, redirect
import covid
import movies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/apis/covid')
def covidAPI():
    resp = covid.get_covid_data()
    return render_template("covid.html", resp=resp)


@app.route('/apis/movies')
def moviesHome():
    return render_template('moviesHome.html')


@app.route('/apis/movies/<category>')
def moviesAPI(category):
    if category == 'action':
        result = movies.get_action()
        results = []
        for item in result[:10]:
            if '(' in item['title']:
                item['title'], junk = item['title'].split('(')
                del(junk)
            results.append(item)
        return render_template('movies.html', res=results, category='Action Movies')
    elif category == 'comedy':
        result = movies.get_comedy()
        results = []
        for item in result[:10]:
            if '(' in item['title']:
                item['title'], junk = item['title'].split('(')
                del(junk)
            results.append(item)
        return render_template('movies.html', res=results, category='Comedy Movies')
    elif category == 'kids_and_family':
        result = movies.get_kids_and_family()
        results = []
        for item in result[:10]:
            if '(' in item['title']:
                item['title'], junk = item['title'].split('(')
                del(junk)
            results.append(item)
        return render_template('movies.html', res=results, category='Kids and Family Movies')
    elif category == 'most_popular':
        result = movies.get_most_popular()
        results = []
        for item in result[:10]:
            if '(' in item['title']:
                item['title'], junk = item['title'].split('(')
                del(junk)
            results.append(item)
        return render_template('movies.html', res=results, category='Popular')

    else:
        return redirect(url_for('moviesHome'))


if __name__ == '__main__':
    app.run(debug=True)
