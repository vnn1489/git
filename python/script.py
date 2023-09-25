import subprocess
import requests
import os

username = 'vnn1489'
url = f"https://api.github.com/users/{username}/repos"
current_directory = os.getcwd()

# Set the desired headers for the request
headers = {"Accept": "application/vnd.github.v3+json"}

# Make a GET request to the GitHub API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repositories = response.json()

    print(f"STARTING CLONE ALL REPOSITORIES")
    for repository in repositories:
        
        try:
            print(f"CLONING {repository['html_url']}")
            git_clone = f"git clone {repository['html_url']}"
            run_git_clone = subprocess.run(git_clone, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            os.chdir(f"cd \"{current_directory}/{repository['name']}\"")
        
            # run_cd = subprocess.run(cd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            git_branch = "git branch -r | grep -v \"\->\" | sed 's,\x1B\[[0-9;]*[a-zA-Z],,g' | while read remote; do git branch --track '${remote#origin/}' '$remote'; done"
            run_git_branch = subprocess.run(git_branch, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            git_fetch = "git fetch --all"
            run_git_fetch = subprocess.run(git_fetch, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            git_pull = "git pull --all"
            run_git_pull = subprocess.run(git_pull, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            os.chdir(f"cd {current_directory}")
            # cd = f"cd {current_directory}"
            # run_cd = subprocess.run(cd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        except Exception as e:
            print(f"AN ERROR OCCURRED: {str(e)}")
    print(f"CLONED ALL REPOSITORIES")