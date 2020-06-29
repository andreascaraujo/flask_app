# models.py
# create a GitHubRepo class to more easily represent the results from the GitHub API search

class GitHubRepo:
    """
    A class used to represent a single GitHub Repository.
    """

    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    # a user-friend way to print the repo information (prints a message with the three repo parameters)
    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."

    # returns the Python code needed to recreate this object:
    def __repr__(self):
        return f"GitHubRepo({self.name}, {self.language}, {self.num_stars})"
