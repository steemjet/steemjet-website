# Imports
from flask import Flask, render_template, url_for, redirect
from Connection import post_info, info, post_activity
from flask_misaka import Misaka, Markup, make_flags
import misaka
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

# Variables
app = Flask(__name__)
Misaka(app)
app.config['SECRET_KEY'] = "DickeryDockeryDock123991"


# Function
def markdown(text, renderer=None, **options):
    ext, rndr = make_flags(**options)
    if renderer:
        md = misaka.Markdown(renderer, ext)
        result = md(text)
    else:
        result = misaka.html(text, extensions=ext, render_flags=rndr)
    if options.get("smartypants"):
        result = misaka.smartypants(result)
    return Markup(result)


class Upvote(FlaskForm):
    username = StringField('Username')
    vote_weight = StringField('Vote Weight')


class Create(FlaskForm):
    title = StringField("Title")
    content = TextAreaField("Content")
    username = StringField('Username')


def image_link(link):
    text = link
    word = "0x0"
    wordEndIndex = text.index(word) + len(word) + 1
    return link[wordEndIndex:]


# Routing
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/trending")
def trending():
    posts = post_info()
    return render_template("trending.html", posts=posts, link=image_link, str=str)


@app.route("/@<author>/<permalink>", methods=["GET", "POST"])
def blog_post(author, permalink):
    form = Upvote(name="form")
    if form.validate_on_submit():
        username = str(form.username.data)
        vote_weight = str(form.vote_weight.data)
        return redirect(
            "https://v2.steemconnect.com/sign/vote?voter={}&author={}&permlink={}&weight={}".format(username, author,
                                                                                                    permalink,
                                                                                                    vote_weight + str(
                                                                                                        000)))
    return render_template("blogpost.html", post=info("%s/%s" % (author, permalink)), markdown=markdown,
                           link=image_link, form=form)


@app.route("/space-force")
def space_force():
    return render_template("space_force.html")


@app.route("/create-a-post", methods=["GET", "POST"])
def create():
    form = Create(name="form")
    if form.validate_on_submit():
        username = str(form.username.data)
        title = str(form.title.data)
        body = str(form.content.data).replace(' ', '%20')
        lower_case_title = title.lower()
        permalink = lower_case_title.replace(' ', '-')
        return redirect(
            "https://v2.steemconnect.com/sign/comment?author=%s&permlink=%s&body=%s&json_metadata='{ tags: ['steemjet']}'" % (
            username, permalink, body))
    return render_template("create-a-post.html", form=form)


@app.route("/activity")
def activity():
    activity = post_activity()
    return render_template("activity.html", activity=activity, link=image_link, str=str)


# Running The App
if __name__ == "__main__":
    app.run(debug=True)
