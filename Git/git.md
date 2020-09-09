# Introduction to Git & Github

## Import a repository to a local folder

* git clone *REPOSITORY*

   > clone a repository


## Create a new branch & edit

**Create**
1. git branch *BRANCH-NAME*

   > create a branch
   
2. git push --set-upstream origin *BRANCH-NAME*

   > push the branch
   
3. git checkout *BRANCH-NAME*
   
   > switch to this new branch

**Edit**
1. git add *FILE-NAME*

   > stage or update a file

2. git commit -m "*MESSAGE*"
3. git push


## Merge to master branch

1. git checkout master

   > switch to master branch

2. git merge *BRANCH-NAME*
3. git push
4. git branch -d *BRANCH-NAME**

   > delete locally the branch (after merge & push**


## Add an existing repository to Github

**Set up**
1. Remove any binary files from the repository
2. In the local environment create a **.gitignore** file

   > indicates which files & directories to ignore when there is a commit

3. Create on Github a repository

**Add**
1. git init 

   > initialize the directory as a Git repository
   
2. git remote add origin *REPOSITORY*

   > provid the SSH or HTTPS link of the Github repository

3. git add -A
4. git commit -m "*MESSAGE*"
5. git branch -M master 
6. git push -u origin master

   > push the files I have locally to the remote on Github


## SSH - best pratice

**Set up SSH**

1. ssh-keygen

   > put this command into a terminal
   > enter a *NAME* then a *PASSWORD* (optional)
   > generate 2 SSH key - one private and another one public (*NAME*.pub)

2. Add the public key to github : settings -> SSH and GPG keys -> New SSH key

**Use SSH**

1. eval `ssh-agent`
2. ssh-add ~/*NAME*

   > *NAME* is the private SSH key file


## Setup credentials - if not using ssh

1. git config credential.helper store
2. git push *REPOSITORY*
3. git config --global credential.helper 'cache --timeout 7200'

   > setup for 2 hours (7200s)


## Git add command

* git add -A : stages all changes
* git add . : stages new files and modification, without deletion
* git add -u : stages modification and deletion, without new files
