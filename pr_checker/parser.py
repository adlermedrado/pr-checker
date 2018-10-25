import math


from datetime import datetime


class Parser:

    def __init__(self, content, org, repo):
        self.content = content
        self.org = org
        self.repo = repo

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def org(self):
        return self._org

    @org.setter
    def org(self, value):
        self._org = value

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, value):
        self._repo = value

    def text(self):
        results = ''
        pull_requests = self.content['data']['repositoryOwner']['repository']['pullRequests']  # noqa
        if pull_requests['edges']:
            for item in pull_requests['edges']:
                today = datetime.now()
                pr_date = datetime.strptime(
                    item['node']['createdAt'],
                    "%Y-%m-%dT%H:%M:%SZ"
                )
                diff_date = today - pr_date
                days = diff_date.days
                hours = math.ceil(diff_date.seconds / 3600)
                results += (
                    f"Org: {self.org} - Repo: {self.repo}"
                    f" - Title: {item['node']['title']}"
                    f" - URL: {item['node']['url']}"
                    f" - Created At: {item['node']['createdAt']}"
                    f" - {days} Days and {hours} hours ago"
                    "\n"
                )
        return results
