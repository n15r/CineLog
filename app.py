import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from models import db, Movie
from forms import RateMovieForm, FindMovieForm

from dotenv import load_dotenv

load_dotenv()

FLASK_APP_KEY = os.environ.get("FLASK_APP_KEY")
MOVIE_DB_API_KEY = os.environ.get("MOVIE_DB_API_KEY")
API_KEY = os.environ.get("API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_KEY')
Bootstrap5(app)


# -----------------Configure DB-------------------------
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///movies-project.db"
db.init_app(app)


with app.app_context():
    db.create_all()

MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
#MOVIE_DB_BEARER_TOKEN = os.environ.get("MOVIE_DB_API_KEY")
MOVIE_DB_BEARER_TOKEN = os.environ.get("MOVIE_DB_BEARER_TOKEN")
API_KEY = os.environ.get("API_KEY")




@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

# New Add Route
@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        print(f"You entered {movie_title}")

        #-----API config---
        url = "https://api.themoviedb.org/3/search/movie"
        headers = {
             "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_BEARER_TOKEN}"        }

        params = {
            "query": movie_title,
            "include_adult": True,
            "language": "en-US",


        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        result_list = data.get("results")


        print(data)


        return render_template("select.html", options=result_list)


    return render_template("add.html", form=form)

# Adding the Update functionality / Patch Request
@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


# Adding the Delete functionality / Delete Request
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


# Fetch request
@app.route("/find", methods=["GET", "POST"])
def find_movie():

    movie_api_id = int(request.args.get("id"))
    if movie_api_id:
        movie_DB_url = "https://api.themoviedb.org/3/movie"
        movie_API_url = f"{movie_DB_url}/{movie_api_id}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_BEARER_TOKEN}"
        }


        response = requests.get(movie_API_url, headers=headers)
        data = response.json()
        print(f"API Data: {data}")

        poster_path =data["poster_path"]
        BASE_URL_IMG = 'https://image.tmdb.org/t/p/w500/' + poster_path

        print(data["original_title"], data["release_date"][:4], data["overview"], BASE_URL_IMG)

        new_movie = Movie(
            title=data["original_title"],
            year=int(data["release_date"][:4]),
            description= data["overview"],
            img_url= BASE_URL_IMG
        )
        db.session.add(new_movie)
        db.session.commit()

        print(new_movie.id)


        return redirect(url_for("rate_movie", id=new_movie.id))
    return render_template("add.html")








if __name__ == '__main__':
    app.run(debug=True)
