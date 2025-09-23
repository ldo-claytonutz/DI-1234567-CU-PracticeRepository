
# Practice with Git & GitHub

## A - Create a new Repository 
1. In Github, at the upper-right corner of any page, select `+`, then click **New repository**.
2. In the **Repository name** box, enter your Reposotiry Name: `DI-1234567-Client-MatterName`
3. Enter a short description on the **Description** box. For example, type "This repository is for practicing GitHub."
4. Set repository security as **Private**.
5. Select **Add a README file**.
6. Click **Create repository**.

## B - Clone an existing Repository 

## 1. Set up the repository
1. Go to the GitHub project page `https://github.com/ldo-claytonutz/DI-1234567-CU-PracticeRepository`
2. Under the **Code** section, copy the HTTPS link.
3. Open **VSCode** at a folder in your local machine.
4. In the Terminal, disable SSL verification (only if necessary): 
    `git config --global http.sslVerify "false"`
   
  	 *Note that Step 4 only need to be done when you first set up your account*
  	
6.	Clone the repository: `git clone <paste the link here>`
7.	Sign in using your browser and authorize GitHub access.
8.	After signing in, go back to VSCode. You are now in the main branch.

## 2. Verify your current branch
1.	Navigate to the project directory (Terminal): `cd <your-project-directory>`
2.	Check your current branch: `git branch`

    You should see *main* highlighted.

## 3. Create a new branch (Your working branch)
1.	Create and switch to a new branch: `git checkout -b <name-of-your-branch>`
2.	Verify you are on the correct branch: `git branch`
3.	Switch between branches: `git checkout <name-of-the-branch>`

## 4. Pull changes from main to your local branch (Do this everytime before starting work)
1.	Switch to the main branch: `git checkout main`
2.	Pull the latest changes: `git pull` 
3.	Switch back to your working branch: `git checkout <your-branch-name>`
4.	If you are in a branch and you SHOULD pull the latest changes from main before making a commit: `git pull origin main`
5.	Merge the latest main changes into your working branch: `git merge main`. 
6. If you encounter a merge conflict: 
    - Press i to enter insert mode.
    - Write a merge message.
    - Press Esc.
    - Type :wq and press Enter to save and exit.

## 5. Make changes and push to GitHub
1.	Modify files as needed.
2.	Stage all changes: `git add .`
3.	Commit changes with a meaningful message: `git commit -m "<describe your changes>"`
4.	Push changes to your branch: `git push -u origin <your-branch-name>`
5.	If the branch has already been pushed before, use: `git push`

## 6. Create Pull Request (PRs):

## 7. Merge changes to main (after PRs being approval)
1.	Once your changes are reviewed and approved, switch to main: `git checkout main`
2.	Pull the latest updates: `git pull` 
3.	Merge your branch into main: `git merge <your-branch-name>`
4.	Push the updated main branch to GitHub: `git push`

## 8. Deleting a Merged Branch (Recommended)
1.	After merging, you can delete your branch locally: `git branch -d <your-branch-name>`
2.	To delete the remote branch on GitHub: `git push origin --delete <your-branch-name>`


## Bonus - Setup venv - virtual environment
1. Create new venv: `python -m venv venv`
2. Activate venv (in Terminal - Command Prompt or Powershell): `.\vevn\Scripts\activate.bat` or `.\vevn\Scripts\activate.ps1`
3. Install requirement packages: `pip install -r requirements.txt`
4. Testing
