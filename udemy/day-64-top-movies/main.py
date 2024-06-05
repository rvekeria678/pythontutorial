from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

#-----Constants-----#
DATABASE_URL = 'sqlite:///movies.db'
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
    if edit_form.validate_on_submit():
        return redirect(url_for("home"))
    
    movie_id = request.args.get('id')
    movie_to_edit = db.get_or_404(Movie, movie_id)
    return render_template('edit.html', movie=movie_to_edit, form=edit_form)

@app.route('/delete')
def delete():
    pass
#-----Server Driver-----#
if __name__ == '__main__':
    app.run(debug=True)
