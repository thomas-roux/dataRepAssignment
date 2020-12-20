#Import modules
from flask import Flask, url_for, request, redirect, abort, jsonify
from FilmDao import filmDao
from SeriesDao import seriesDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#Direct to root
@app.route('/')
def index():
    return "hello"

#Returns all films on server
@app.route('/films')
def getAll():
    return jsonify(filmDao.getAll())

#Returns films with specific id
@app.route('/films/<int:id>')
def findById(id):
    return jsonify(filmDao.findById(id))

#Posts new film entry to server
@app.route('/films', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    film = {
        #"id": request.json["id"],
        "Title": request.json["Title"],
        "Year": request.json["Year"],
        "Genre": request.json["Genre"],
        "Director": request.json["Director"],
        "Language": request.json["Language"],
        "Runtime": request.json["Runtime"],
        "IFCO": request.json["IFCO"]
    }
    return jsonify(filmDao.create(film))

#Updates film entry on server
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    foundFilm = filmDao.findById(id)
    if foundFilm == 0:
        return jsonify({}), 404

    currentFilm = foundFilm

    if 'Title' in request.json:
        currentFilm['Title'] = request.json['Title']
    if 'Year' in request.json:
        currentFilm['Year'] = request.json['Year']
    if 'Genre' in request.json:
        currentFilm['Genre'] = request.json['Genre']
    if 'Director' in request.json:
        currentFilm['Director'] = request.json['Director']
    if 'Language' in request.json:
        currentFilm['Language'] = request.json['Language']
    if 'Runtime' in request.json:
        currentFilm['Runtime'] = request.json['Runtime']
    if 'IFCO' in request.json:
        currentFilm['IFCO'] = request.json['IFCO']

    filmDao.update(currentFilm, id)
    return jsonify(currentFilm)

#Deletes film entry from server db
@app.route('/films/<int:id>', methods=['DELETE'])
def delete(id):
    filmDao.delete(id)
    return jsonify({"done":True})

'''Series server'''
#Returns all series on server
@app.route('/series')
def getAllSeries():
    return jsonify(seriesDao.getAll())

#Returns series with specific id
@app.route('/series/<int:id>')
def findSeriesById(id):
    return jsonify(seriesDao.findById(id))

#Posts new series on server
@app.route('/series', methods=['POST'])
def createSeries():
    if not request.json:
        abort(400)
    series = {
        #"id": request.json["id"],
        "Title": request.json["Title"],
        "Started": request.json["Started"],
        "Ended": request.json["Ended"],
        "Genre": request.json["Genre"],
        "Language": request.json["Language"],
        "Seasons": request.json["Seasons"],
        "Episodes": request.json["Episodes"]
    }
    return jsonify(seriesDao.create(series))

#Updates series on server
@app.route('/series/<int:id>', methods=['PUT'])
def updateSeries(id):
    foundSeries = seriesDao.findById(id)
    if foundSeries == 0:
        return jsonify({}), 404

    currentSeries = foundSeries

    if 'Title' in request.json:
        currentSeries['Title'] = request.json['Title']
    if 'Started' in request.json:
        currentSeries['Started'] = request.json['Started']
    if 'Ended' in request.json:
        currentSeries['Ended'] = request.json['Ended']
    if 'Genre' in request.json:
        currentSeries['Genre'] = request.json['Genre']
    if 'Language' in request.json:
        currentSeries['Language'] = request.json['Language']
    if 'Seasons' in request.json:
        currentSeries['Seasons'] = request.json['Seasons']
    if 'Episodes' in request.json:
        currentSeries['Episodes'] = request.json['Episodes']

    seriesDao.update(currentSeries, id)
    return jsonify(currentSeries)

#Deletes series on server with specific id
@app.route('/series/<int:id>', methods=['DELETE'])
def deleteSeries(id):
    seriesDao.delete(id)
    return jsonify({"done":True})

#Runs programe when called
if __name__ == "__main__":
    app.run(debug=True)