from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3

#-----Constants-----#
DATABASE_URL = 'sqlite:///books.db'
#-----Aux-----#
app = Flask(__name__)
class Base(DeclarativeBase):pass
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)
#-----Models-----#
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    def as_dict(self):
        return {
            col.name: getattr(self, col.name)
        }

    def __repr__(self) -> str:
        return f'<Book {self.title}>'
#-----Create Database-----#
with app.app_context():
    db.create_all()
#-----Routes-----#
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)
# Add Book to Library
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")
# Edit Book Rating
@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)
# Delete Book from Library
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

#-----Server Start-----#
if __name__ == "__main__":
    app.run(debug=True)