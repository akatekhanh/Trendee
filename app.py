# This file contains an example Flask-User application.
# To keep the example simple, we are applying some unusual techniques:
# - Placing everything in one file
# - Using class-based configuration (instead of file-based configuration)
# - Using string-based templates (instead of file-based templates)
import json
from flask import Flask, render_template_string, request, jsonify, render_template, session, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_user import login_required, UserManager, UserMixin, current_user


# Class-based application configuration
class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = '@SECr3RtKEYY8782!@#1'

    # Flask-MongoEngine settings
    MONGODB_SETTINGS = {
        'db': 'db_trendee',
        'host': 'mongodb://localhost:27017/db_trendee'
    }

    # Flask-User settings
    USER_APP_NAME = "Trendee"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_REQUIRE_RETYPE_PASSWORD = True    # Simplify register form


def create_app():
    """ Flask application factory """

    # Setup Flask and load app.config
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    # Setup Flask-MongoEngine
    db = MongoEngine(app)

    # Define the User document.
    # NB: Make sure to add flask_user UserMixin !!!
    class User(db.Document, UserMixin):
        active = db.BooleanField(default=True)

        # User authentication information
        username = db.StringField(default='')
        password = db.StringField()

        # User information
        first_name = db.StringField(default='')
        last_name = db.StringField(default='')
        email = db.StringField(default='')
        # Relationships
        roles = db.ListField(db.StringField(), default=[])

    class Comment(db.Document):
        id_belong = db.StringField()
        id_user = db.StringField()
        content = db.StringField(default='')

    class Hashtag(db.Document):
        name = db.StringField()
        score = db.IntField()

    # class HashtagFacebook(Hashtag):

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)
    # user_manager_1 = UserManager(app, db, Comment)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        try:
            current_user.username
        except:
            return redirect('/user/sign-in')
        return redirect(url_for('get_newsfeeds'))
        # return render_template_string("""
        #     {% extends "flask_user_layout.html" %}
        #     {% block content %}
        #         <h2>Home page</h2>
        #         <p><a href={{ url_for('user.register') }}>Register</a></p>
        #         <p><a href={{ url_for('user.login') }}>Sign in</a></p>
        #         <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
        #         <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
        #         <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
        #     {% endblock %}
        #     """)

        # The Members page is only accessible to authenticated users via the @login_required decorator
    @app.route('/members')
    @login_required    # User must be authenticated
    def member_page():
        # String-based templates
        return render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
                <h2>Members page</h2>
                <p><a href={{ url_for('user.register') }}>Register</a></p>
                <p><a href={{ url_for('user.login') }}>Sign in</a></p>
                <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
                <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
                <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
            {% endblock %}
            """)

    @app.route('/user', methods=['GET'])
    @login_required
    def query_records():
        name = request.args.get('username')
        users = User.objects(username=name).first()
        if not users:
            return jsonify({'error': 'data not found'})
        else:
            del users.password
            return jsonify(users.to_json())

    @app.route('/login', methods=['POST'])
    def login():
        return render_template('login.html')

    @app.route('/newsfeeds_trending')
    def get_newsfeeds_trending():
        return render_template('newsfeeds_trending.html') 

    @app.route('/newsfeeds')
    def get_newsfeeds():
        with open('api/data/trending/news.json', 'r') as file:
            data = json.load(file)

        # data = json.dumps(data)
        result = data['results']
        # for item in result:
        #     hours = item['published_date_diff']
        #     title = item['title']
        #     print(item['author_details'])
        return render_template('newsfeeds.html', data=result)

    @app.route('/detail')
    def get_detail():
        return render_template('detail.html')

   

    # @app.route('/user/<str:username>', methods=['GET'])
    # def query_records():
    #     user = User.objects(username=username).first()
    #     if not user:
    #         return jsonify({'error': 'data not found'})
    #     else:
    #         return jsonify(user.to_json())

    # @app.route('/user', methods=['PUT'])
    # def create_record():
    #     record = json.loads(request.data)
    #     user = User(first_name=record['first_name'],
    #                 last_name=record['last_name'],
    #                 email=record['email'])
    #     user.save()
    #     return jsonify(user.to_json())

    # @app.route('/', methods=['POST'])
    # def update_record():
    #     record = json.loads(request.data)
    #     user = User.objects(name=record['name']).first()
    #     if not user:
    #         return jsonify({'error': 'data not found'})
    #     else:
    #         user.update(email=record['email'])
    #     return jsonify(user.to_json())

    # @app.route('/', methods=['DELETE'])
    # def delete_record():
    #     record = json.loads(request.data)
    #     user = User.objects(name=record['name']).first()
    #     if not user:
    #         return jsonify({'error': 'data not found'})
    #     else:
    #         user.delete()
    #     return jsonify(user.to_json())

    return app


# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
