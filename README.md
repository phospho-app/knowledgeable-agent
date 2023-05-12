# phospho agent template

This is a template of a phospho agent. You need to upload the folder with the name `agent`.

You can find the documentation of phospho at [docs.phospho.app](https://docs.phospho.app) .

# Requirements

You need to have a valid phospho account to be able to deploy your agent. You can signup [here](https://phospho.app).

# Quickstart 

Clone this repo :
```
$ git clone {repo_url}
```

Write your code in the `interface.py` functions.

If needed, update the `requirements.txt` with :
```
$ pip freeze > requirements.txt
```

Chose a `project_name` for your project, and upload the folder with the name `agent` to phopsho. It should be up and running in a few minutes. Your user can access it at `app.phospho.app/{project_name}`