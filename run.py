from pr_checker.client import Client
from pr_checker.parser import Parser


repo_list = [
    {'org': 'adlermedrado', 'repo': 'abbr'},
]


client = Client()

for repo in repo_list:
    pull_request = client.request(repo.get('org'), repo.get('repo'))
    parser = Parser(pull_request.json(), repo.get('org'), repo.get('repo'))
    results = parser.text()

if results:
    print('There are opened PRs:\n' + results)
