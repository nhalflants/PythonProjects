# Streamlit Todo Web App

Context: PyCharm, Python 3.10, Streamlit

## Setup

- Create a `requirement.txt` file by running `pip freeze > requirements.txt` to generate the file listing the python libraries. This file should be uploaded to the server where the web app will be hosted so that server knows the python third party packages that need to be installed in order to run the web app correctly.
- In the terminal, go to project directory folder and run web app `streamlit run web.py --server.baseUrlPath=/todo_webapp` to run app.
- Create `.gitignore` file. Ignore `venv` folder and hidden `.idea` files
- Upload the project to GitHub
  - Go to GitHub account > New repository > Copy the URL to the project (link to repository)
  - "Enable version control" > git in PyCharm
  - Go to "Manage remotes" and add copied URL 
  - Add files to Git : Select files > Right click "Git" > "Add"
  - Commit "Initial commit"
- Synchronize GitHub with the server where we're hosting our web app.
- Go to the terminal and run the web app.
- Go to local host and select menu button and go to deploy this app

## Screenshot

![Todo Web App](https://github.com/nhalflants/PythonProjects/blob/master/todo_webapp/screenshot%20app.png?raw=true)

Source : Todo web app from https://www.udemy.com/course/the-python-mega-course
