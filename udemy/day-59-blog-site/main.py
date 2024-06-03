from flask import Flask, render_template
import requests

#----Constants-----#
posts_url = 'https://api.npoint.io/55f977f8b55481b3e6dd'

app = Flask(__name__)

@app.route('/')
def root():
    response = requests.get(posts_url)
    all_posts = response.json()
    print(all_posts)
    return render_template('index.html', all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<id>')
def get_post(id):
    response = requests.get(posts_url)
    all_posts = response.json()
    return render_template('post.html', posts=all_posts, post_id=int(id))

if __name__ == '__main__':
    app.run(debug=True)