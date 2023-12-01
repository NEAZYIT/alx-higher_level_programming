#!/usr/bin/python3
"""
This script retrieves commits from a user's GitHub repository
"""
import requests
from sys import argv

def main():
    repo_owner = argv[1]
    repo_name = argv[2]
    url = (f'https://api.github.com/repos/'
           f'{repo_owner}/{repo_name}/commits')
    response = requests.get(url)

    commits = response.json()
    sorted_commits = sorted(
        commits,
        key=lambda commit: commit['commit']['author']['date'],
        reverse=True
    )

    for i, commit in enumerate(sorted_commits):
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

        if i == 9:
            break

if __name__ == "__main__":
    main()
