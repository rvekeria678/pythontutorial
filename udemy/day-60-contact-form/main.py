from flask import Flask, render_template, request
import requests, smtplib, os
from dotenv import load_dotenv

load_dotenv()

#----Constants----#
PORT = 587
TIMEOUT = 120
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def recieve_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    msg = request.form['message']

    with smtplib.SMTP('smtp.gmail.com', port=PORT, timeout=TIMEOUT) as conn:
        conn.starttls()
        conn.login(user=os.environ.get("RECIPIENT") , password=os.environ.get("PASSWORD"))
        conn.sendmail(from_addr=email, to_addrs=os.environ.get("RECIPIENT"), msg=f"Subject:Blog Contact: {name}\n\n{msg}\n\nPhone | {phone}")

    print(name,email,phone,msg)

    return "<h1>Successfully sent your message.</h1>"

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)