# imports

from flask import Flask, jsonify, request
from waitress import serve
import requests
import json
from config import secret

app = Flask(__name__)


@app.route('/')
def main():
    '''
    Connection Check for Service
    '''
    return 'Connection Successful!'


@app.route('/api/movie/search', methods=['GET'])
def search_movie():
    '''
    This method will search the movie name from the text you entered
    '''
    url = 'https://imdb8.p.rapidapi.com/auto-complete'
    querystring = {'q': request.args.get('q')}
    headers = {
        'x-rapidapi-key': secret['key'],
        'x-rapidapi-host': 'imdb8.p.rapidapi.com'
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    response = response.json()
    return jsonify({
        'code': 200,
        'message': 'Data fetched successfully!',
        'data': response['d']
    })


@app.route('/api/movie/search/bygenre', methods=['GET'])
def search_movie_by_genre():
    '''
    This method will search movie(s) by genre
    '''
    url = 'https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre'
    querystring = {'genre': request.args.get('genre')}
    headers = {
        'x-rapidapi-key': secret['key'],
        'x-rapidapi-host': 'imdb8.p.rapidapi.com'
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    response = response.json()
    return jsonify({
        'code': 200,
        'message': 'Data fetched successfully!',
        'data': response
    })


@app.route('/api/movie/get/details', methods=['POST'])
def get_movie_details():
    '''
    This method will get movie details of the passed title as
    request body
    '''
    body = json.loads(request.data)
    body = body['title_codes']
    print(body)
    final_response = []
    url = 'https://imdb8.p.rapidapi.com/title/get-details'
    headers = {
        'x-rapidapi-key': secret['key'],
        'x-rapidapi-host': 'imdb8.p.rapidapi.com'
    }
    for title in body:
        querystring = {'tconst': title}
        print(querystring)
        response = requests.get(url=url, headers=headers, params=querystring)
        final_response.append(response.json())
    return jsonify({
        'code': 200,
        'message': 'Data fetched successfully!',
        'data': final_response
    })


@app.route('/api/movie/get/top-rated-movies', methods=['GET'])
def get_top_rated_movies():
    '''
    This method will get list of top 250 rated movies rated by imdb
    '''
    url = 'https://imdb8.p.rapidapi.com/title/get-top-rated-movies'
    headers = {
        'x-rapidapi-key': secret['key'],
        'x-rapidapi-host': 'imdb8.p.rapidapi.com'
    }
    response = requests.get(url=url, headers=headers)
    response = response.json()
    return jsonify({
        'code': 200,
        'message': 'Data fetched successfully!',
        'data': response
    })


@app.route('/api/movie/get/top-rated-tv-shows', methods=['GET'])
def get_top_rated_tv_shows():
    '''
    This method will get list of top 250 rated tv shows rated by imdb
    '''
    url = 'https://imdb8.p.rapidapi.com/title/get-top-rated-tv-shows'
    headers = {
        'x-rapidapi-key': secret['key'],
        'x-rapidapi-host': 'imdb8.p.rapidapi.com'
    }
    response = requests.get(url=url, headers=headers)
    response = response.json()
    return jsonify({
        'code': 200,
        'message': 'Data fetched successfully!',
        'data': response
    })


# __main__
if __name__ == '__main__':
    serve(app, port=5000)
