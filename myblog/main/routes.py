from flask import render_template, request, Blueprint
from myblog.models import Post
from .requests import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    newquotes=get_quote()
    quote = newquotes['quote']
    author = newquotes['author']
    return render_template('about.html', title='About', quote=quote, author=author)
