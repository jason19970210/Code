# GitHub

### Contents
+ #### [Command Lines](#Command_Lines)
		+ ##### [Large File Support](#github_lfs)
	+ #### [GitHub Pages](#GitHub_Pages)



<a name="Command_Lines" />

### Command Lines
+   git
	> Get help of git command

+   git init
	> 

+   git clone `https`
	> Add the repository to the local

+   git \s
	> get status

+   git add `file name`  
    git add .  
    > add all changed file to Staging Area,  also as `$ git add --all`

+   git commit -m "`commit`"  
    git commit -am "`commit`"
    > give description / Comment to the file
  
+   git push  
	> Upload the file in `Staging Area`

    git push origin master  
    > 

    git push origin `branch name`  
    > 

    git push --set-upstream origin `branch name`  
    > 
    
    git push -f  
    > Force Push,  also as `$ git push --force`

    git push -u origin master  
    > 

+   git pull  
    pull = git fetch + git merge
    > Update local version from GitHub
    
+   git log  
	> Show all the commits overtime

    git log -p -2
    > 顯示每個更新之間差別的內容, 限制為只輸出最後兩個更新

    git log --stat
    > 檢視每個更新的簡略統計資訊

    git log --oneline
    > 
    
+   git checkout -b `branch name`  
	> create a new branch and switch to it

    git checkout `branch name`
    > Change the branch to the other one

+   git branch  
	> Show the branches

    git branch `branch name`  
    git branch -D `branch name`  
    git branch --delete `branch name`  

+ 	git remote  
	git remote add origin  
    git remote rm origin  
    git remote -v  

+   git stash  
    git stash save  
    git stash apply  
    git stash drop

+   git config user.name
	> Check user name  

    git config user.email
    > Check user email

+   git config --global user.name `user name`  
    git config --global user.email `user email`  

<a name="github_lfs" />

### Large File Support

- Installation
	- Web [Download Page](https://git-lfs.github.com)
	- Homebrew : `$ brew install git-lfs`
- Steps
	1. `$ git lfs install`
	2. Select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.
		> `git lfs track "*.psd"`
	3. Make sure .gitattributes is tracked
		> `git add .gitattributes`
	4. - `git add *.psd`
	- `git comit -m ""`
	- `git push origin master`


<a name="GitHub_Pages" />

### GitHub Pages
+ static page like HTML as well
+ Dont support `PHP`, `ASP`, ` .htacess`, `FTP Server`
+ Can be UPLOADED by GIT ONLY
+ GitHub Pages will be PUBLIC

    ### Steps  
	+ set project name to `username.github.io`  
    + set up an empty REPO  
    + add a HTML file name `index.html`  

	```html
	<!DOCTYPE html>
		<html>
		   	<head>
				<meta charset="utf-8">
					<title>Hi, GitHub</title>
			</head>
			<body>
				<h1>...</h1>
			</body>
		</html>
	```
	+ git add index.html  
	+ git commit -m "add index"
	+ git push


### Reference
+ Git Push：https://gitbook.tw/chapters/github/push-to-github.html
+ Git 管控：https://gitbook.tw/chapters/using-git/add-to-git.html
+ Git Ignore：https://www.gitignore.io/
