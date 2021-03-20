import json
from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('navbar.html')


@app.route('/newsfeeds')
def news_feed():
    with open('api/data/trending/news.json', 'r') as file:
        data = json.load(file)

        # data = json.dumps(data)
    result = data['results']
    # for item in result:
    #     hours = item['published_date_diff']
    #     title = item['title']
    #     print(item['author_details'])
    return render_template('newsfeeds.html', data=result)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
