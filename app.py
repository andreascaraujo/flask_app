"""
app.py

A Simple Flask Web Application interface
For viewing popular GitHub Repos sorted by stars using the GitHub Search API.
"""

from flask import Flask, render_template, request

from repos.exceptions import GitHubApiException
from repos.api import repos_with_most_stars

# create the flask app object:
app = Flask(__name__)

# create a list of all the available languages that the user of the app can choose from.
# this helps to keep track of if they're selected or not
available_languages = ["Python", "JavaScript", "Ruby", "Java"]


# a function that gets called when the root url for the website (or /) is required by the user:
@app.route("/", methods=["POST", "GET"])
def index():
    # this signals to Flask that this index() function should be
    # called to handle any GET or POST requests to the URL /.

    if request.method == "GET":
        # display whichever repos were selected last
        # (or all of them if this is the first request)
        selected_languages = available_languages
    elif request.method == "POST":
        # grab the languages variable from the request form
        # and use it to populate our selected_languages list
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    # pass to render_template the list of selected languages, available languages and results:
    return render_template(
        "index.html",
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results
    )


# a custom error handle renders a special website (error.html)
# if we receive a GitHubApiException:
@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template("error.html", message=error)
