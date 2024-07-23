@echo off

color a

D:

cd coding

REM Clone repository (replace git@github.com:username/repo.git with your actual repo URL)
git clone git@github.com:iknizzz1807/autoCommit.git

REM Navigate to repository directory
cd autoCommit

REM Make changes (replace with actual commands)
python -u "D:\Coding\Python\generateText.py"

REM Stage changes
git add .

REM Commit changes with a default message
git commit -m "Auto commit"

REM Push changes
git push
pause