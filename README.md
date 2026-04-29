# hwrs564b_course_materials
Course materials for the spring analysis class

## Table of Contents
- [1.0 Intial Setup](#10-intial-setup)
- [2.0 Setup to work with code spaces through your local vscode](#20-setup-to-work-with-code-spaces-through-your-local-vscode)
  - [2.1 Install the VS Code codespaces extension](#21-install-the-vs-code-codespaces-extension)
  - [2.2 Sign into GitHub to autorize usage](#22-sign-into-github-to-autorize-usage)
  - [2.3 Connect to your existing codespace](#23-connect-to-your-existing-codespace)  
- [3.0 Other useful things to do](#30-other-useful-things-to-do)
  - [3.1 Adding a python package to your enviroment](#31-adding-a-python-package-to-your-enviroment)

## 1.0 Intial Setup
Students should all create their own fork of this repo.  Forking a repository creates a personal copy where you can make changes without affecting the main repo. 

In the top-right corner of the repository page, click the **Fork** button. When pompted set:

```
owner = HWRS564-hydrogeologic-analysis
name = hwrs564b_course_materials_<yourUserID>
```

Once this is created you can clone the repository locally or open through codespaces on GitHub

## 2.0 Setup to work with code spaces through your local vscode
### 2.1 Install the VS Code codespaces extension 
1. Open VS Code
2. Click the Extensions icon in the sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for "GitHub Codespaces"
4. Click **Install** on the official "GitHub Codespaces" extension by GitHub

### 2.2 Sign into GitHub to autorize usage 
1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type: `Codespaces: Sign In`
3. Click **Allow** when prompted to sign in
4. Complete the authentication in your browser
5. Authorize VS Code to access your GitHub account

### 2.3 Connect to your existing codespace
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type: `Codespaces: Connect to Codespace`
3. Select your codespace from the list
4. VS Code will connect and open it


## 3.0 Other useful things to do

### 3.1 Adding a python package to your enviroment
Open a terminal window, activate the enviroment you would like to add the pacage to and then conda install or pip install the package. 
```bash
conda env list
conda activate hwrs564b
conda install [package name]
# If conda install doesn't work try pip install
conda list
``` 
