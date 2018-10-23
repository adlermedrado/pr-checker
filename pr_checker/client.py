import json
import requests


from .config import GITHUB_ENDPOINT, GITHUB_TOKEN


class Client:
    def request(self, org, repo):
        headers = {'Authorization': f'bearer {GITHUB_TOKEN}'}

        query = """
	{
	  repositoryOwner(login: "ORG") {
	    repository(name: "REPO") {
	      pullRequests(first: 100, states: [OPEN]) {
		edges {
		  node {
		    title
		    state
		    url
		    createdAt
		  }
		}
	      }
	    }
	  }
	}
        """.replace('ORG', org).replace('REPO', repo)

        return requests.post(GITHUB_ENDPOINT, headers=headers, json={'query': query})
