# api.py
# hold functions for querying the GitHub API

import requests

from repos.exceptions import GitHubApiException
from repos.models import GitHubRepo

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars):
    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.
    """
    # .strip() to clear it of leading and trailing whitespace
    query = " ".join(f"language:{language.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query


def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    # print(parameters) optional
    response = requests.get(GITHUB_API_URL, params=parameters)

    # if the status_code does not equal 200, raise to throw the GitHubAPIException
    if response.status_code != 200:
        raise GitHubApiException(response.status_code)

    response_json = response.json()
    items = response_json["items"]

    # instead of returning items directly from the response json,
    # use a list comprehension to create and return a list of GitHubRepo objects
    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]
