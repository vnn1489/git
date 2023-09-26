import subprocess
import requests
import os

username = 'vnn1489'
url = f"https://api.github.com/users/{username}/repos"

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
            os.chdir(f"{os.getcwd()}/{repository['name']}")

            git_branch_command = "git branch -r | grep -v '\->' | sed 's,\x1B\[[0-9;]*[a-zA-Z],,g' | while read remote; do git branch --track \"${remote#origin/}\" \"$remote\"; done"
            git_fetch_command = "git fetch --all"
            git_pull_command = "git pull --all"

            try:
                # Run the Git commands one by one
                subprocess.run(git_branch_command, shell=True, check=True)
                subprocess.run(git_fetch_command, shell=True, check=True)
                subprocess.run(git_pull_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

            previous_directory = os.path.dirname(os.getcwd())
            os.chdir(previous_directory)
           
        except Exception as e:
            print(f"AN ERROR OCCURRED: {str(e)}")
    print(f"CLONED ALL REPOSITORIES")