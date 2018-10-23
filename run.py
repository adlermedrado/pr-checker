import json

from pr_checker.client import Client


repo_list = [
    {'org': 'adlermedrado', 'repo': 'abbr'}
]


client = Client()

for repo in repo_list:
    pull_request = client.request(repo.get('org'), repo.get('repo'))
    print(pull_request.text)
