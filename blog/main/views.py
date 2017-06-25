# coding:utf-8

from flask import render_template, current_app, request
from . import main
from ..models import  Role, User, Post

# views
@main.route('/')
def index():
    # 暂时从数据库获取
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)


@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', post_id, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['BLOG_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('post.html', post=post,pagination=pagination)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')
