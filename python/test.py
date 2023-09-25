import os

# Get the current working directory
current_directory = os.getcwd()

print('Current Working Directory:', current_directory)




GIT    git branch -r | grep -v "\->" | sed 's,\x1B\[[0-9;]*[a-zA-Z],,g' | while read remote; do git branch --track '${remote#origin/}' '$remote'; done
GIT    git fetch --all
GIT    git pull --all


import os

# Specify the path of the directory you want to change to
new_directory = '/path/to/your/directory'

# Change the working directory to the specified directory
os.chdir(new_directory)

# Verify the change by getting the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
