import requests
import json

from app.static.models import gitmodelsmodule


class githubexp:
    def __init__(self):
        self.github_token = "48b1d63830d6af7bc12c204b0c24db61ef4cf431"
        self.base_url = "https://api.github.com"
        self.git_urls = None

    def getAccessToAccount(self):
        r = requests.get(self.base_url, auth=('lakshmanraob@gmail.com', 'laksh2682'))
        print(r.status_code)
        print(r.headers['content-type'])
        return r.content

    def authenticateWithToken(self):
        token = "token " + self.github_token
        headers = {"Authorization": token}
        r = requests.get(self.base_url, headers=headers)

        if r.status_code == 200:
            self.git_urls = json.loads(r.content.decode("utf-8"), object_hook=self.getGitUrl)
            print(self.git_urls.current_user_authorizations_html_url)
            return self.getReposList()
            # return self.git_urls['current_user_url']
        else:
            return r.content

    # Dictionary to Object conversion method
    def getGitUrl(self, d):
        gitUrls = gitmodelsmodule.gitUrl()
        gitUrls.__dict__.update(d)
        return gitUrls

    """Gives the Repo list """

    def getReposList(self):
        if self.git_urls:
            token = "token " + self.github_token
            headers = {"Authorization": token}
            r = requests.get(self.base_url + "/user/repos", headers=headers)
            """"List of repos display will happen from here"""
            reposList = json.loads(r.content.decode("utf-8"))
            for repo in reposList:
                # print(repo['name'])
                gitrepoObj = gitmodelsmodule.gitrepo(repo)
                if gitrepoObj.name == "MyFireBaseProject":
                    # print(gitrepoObj.name)
                    gitOwner = gitmodelsmodule.gitrepoowner(gitrepoObj.owner)
                    self.getBranchList(owner=None, reponame=None, repo_url=gitrepoObj.url)
                    print(gitOwner)
            return r.content

    """Gives you the Number of branches available for the given repo"""

    def getBranchList(self, owner, reponame, repo_url):
        token = "token " + self.github_token
        headers = {"Authorization": token}
        if repo_url:
            branches_url = repo_url + "/branches"
        else:
            branches_url = self.base_url + "/repos/" + owner + "/" + reponame + "/branches"
        r = requests.get(branches_url, headers=headers)
        print(reponame)
        print(r.content)
        print("-----------------")
        return r.content
