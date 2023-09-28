import subprocess
import requests
import os

username = 'vnn1489'
url = f"https://api.github.com/users/{username}/repos"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repositories = response.json()
    git_branch = "git branch -r | grep -v '\->' | sed 's,\x1B\[[0-9;]*[a-zA-Z],,g' | while read remote; do git branch --track \"${remote#origin/}\" \"$remote\"; done"
    git_fetch = "git fetch --all"
    git_pull = "git pull --all"

    print(f"STARTING CLONE ALL REPOSITORIES")
    for repository in repositories:
        print(f"CLONING {repository['html_url']}")
        try:
            git_clone = f"git clone {repository['html_url']}"
            subprocess.run(git_clone, shell=True, check=True)
            os.chdir(f"{os.getcwd()}/{repository['name']}")

            # ???? CHUA HIEU DOAN TRY EXCEPT NAY LAI KHIEN CHO CAC DIRECTORY KHOONG BI LONG VAO NHAU
            try:
                subprocess.run(git_branch, shell=True, check=True)
                subprocess.run(git_fetch, shell=True, check=True)
                subprocess.run(git_pull, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

            previous_directory = os.path.dirname(os.getcwd())
            os.chdir(previous_directory)
        except Exception as e:
            print(f"AN ERROR OCCURRED: {str(e)}")
    print(f"CLONED ALL REPOSITORIES")