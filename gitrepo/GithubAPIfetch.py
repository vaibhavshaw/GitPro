import requests
import json

base_url = 'https://api.github.com'
client_id = 'dbeef31a9063b4cff7c8'
client_secret = '4516aec2bbb6259a7c8547ce2cd645df507501ef'


class GitHubAPIFetch():

    def get_top_M_commit_count(self, repo, M):
        repo_all = []
        for i in range(0, min(len(repo), 5)):
            top_m_contrib_url = repo[i][2]+'?per_page={}&client_id={}&client_secret={}'.format(
                min(M, 5), client_id, client_secret)
            top_m_committees = requests.get(top_m_contrib_url).json()
            repo_m = []
            for j in range(len(top_m_committees)):
                repo_m.append([repo[i][0], top_m_committees[j]['contributions'],
                               top_m_committees[j]['html_url'], repo[i][1]])
            repo_m = sorted(repo_m, reverse=True)
            repo_all.append(repo_m)
            # print(repo_m)
        return repo_all

    def get_top_N_repo(self, organisation, N, M):
        top_repo_url = '{}/orgs/{}/repos?per_page=1000&client_id={}&client_secret={}'.format(
            base_url, organisation, client_id, client_secret)
        top_repo = requests.get(top_repo_url).json()
        repo = []
        for i in range(len(top_repo)):
            repo.append([top_repo[i]['forks_count'], top_repo[i]
                         ['full_name'], top_repo[i]['contributors_url']])
        repo = sorted(repo, reverse=True)
        # print(repo)
        repo = repo[:min(N, 5)]
        # print(repo)
        repo_all = GitHubAPIFetch.get_top_M_commit_count(self, repo, M)
        # print((repo_all))
        return repo, repo_all
