from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
#-----Aux-----#
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
#-----Create Database-----#
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
#-----Configure Form-----#
class CreatePostForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Author", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    smbt = SubmitField(label="Submit Post")
    
#-----Configue Table-----#
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    results = db.session.execute(db.select(BlogPost))
    all_posts = results.scalars().all()
    return render_template("index.html", all_posts=all_posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_post():
    new_blog_form = CreatePostForm()
    if new_blog_form.validate_on_submit():
        current_date = date.today()
        new_post = BlogPost(
            title=new_blog_form.title.data,
            subtitle=new_blog_form.subtitle.data,
            date= current_date.strftime("%B %d %Y"),
            body=new_blog_form.body.data,
            author=new_blog_form.author.data,
            img_url=new_blog_form.img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=new_blog_form, edit_most=False)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET','POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        updated_post = db.get_or_404(BlogPost, post_id)
        updated_post.title = edit_form.title.data
        updated_post.subtitle = edit_form.subtitle.data
        updated_post.img_url = edit_form.img_url.data
        updated_post.author = edit_form.author.data
        updated_post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=edit_form, edit_mode=True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>', methods=['GET','DELETE'])
def delete_post(post_id):
    post_to_del = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_del)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
