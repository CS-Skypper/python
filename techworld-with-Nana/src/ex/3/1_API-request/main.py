"""
How to make an API Call with Python to GitLab
  1. Make an HTTP Request
  2. Get an HTTP Response

  --------------
  Possible idea: make an app that creates a new repository on your GitLab account
  --------------

- An Application talking to an other is done using API Requests
  - Both App must have APIs

- In Python to make request it is required to use an HTTP Library, like requests
"""

"""
This app will request all the project from an user repository
"""

import requests

# google the GitLab API Base-URL on their Doc
# response = requests.get("https://gitlab.com/api/v4/users/skypper/projects")
response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.text) # with the .text attribute it returns a String of a List of Dictionaries
# print(response.json())
# print(type(response.json()))
# print(response.json()[0])
# print(type(response.json()[0]))
my_projects = response.json()

# extract project_name and project_url
for project in my_projects: 
  print(f"Project Name: {project['name']}\n Project URL: {project['http_url_to_repo']}\n")
