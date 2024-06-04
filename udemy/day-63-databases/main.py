from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add")
def add():
    return render_template('add.html')

@app.route('/input', methods=['GET','POST'])
def recieve_data():
    all_books.append({
        "title": request.form['title'],
        "author": request.form['author'],
        "rating": request.form['rating']
    })
    return "You successfull added a book!"

if __name__ == "__main__":
    app.run(debug=True)

