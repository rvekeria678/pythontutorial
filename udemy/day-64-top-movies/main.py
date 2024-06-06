from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests, os

#-----Constants-----#
DATABASE_URL = 'sqlite:///movies.db'
TMDB_URL = 'https://api.themoviedb.org/3/search/movie'
load_dotenv()
#-----Aux-----#
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
class Base(DeclarativeBase):pass
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)
#-----Models-----#
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
#-----Forms-----#
class EditForm(FlaskForm):
    rating = IntegerField(label="Your Rating out of 10 e.g. 7.5",
                          validators=[DataRequired()])
    review = StringField(label="Your Review",
                         validators=[DataRequired()])
    sbmt = SubmitField(label="Done")
class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title")
    sbmt = SubmitField(label="Add Movie")
#-----Create DB-----#
with app.app_context():
    db.create_all()
#-----Routes-----#
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    if edit_form.validate_on_submit() and request.method == 'POST':
        movie_id = request.args.get('id')
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.review = edit_form.review.data
        movie_to_update.rating = edit_form.rating.data
        db.session.commit()
        return redirect(url_for("home"))
    
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template('edit.html', movie=movie_selected, form=edit_form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        tmdb_params = {
            "query": add_form.movie_title.data,
            "api_key": os.environ.get('TMDB_API_KEY')
        }
        response = requests.get(url=TMDB_URL, params=tmdb_params)
        results = response.json()

        print(results)
        #return redirect(url_for('select'))
    return render_template('add.html', form=add_form)

@app.route('/select')
def select():

    return render_template('select.html')

#-----Server Driver-----#
if __name__ == '__main__':
    app.run(debug=True)
