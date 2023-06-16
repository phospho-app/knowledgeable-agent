# knowledgeable agent

This is an exemple of an agent you can deploy using phospho. It will answer questions based on the knowledge it has in the document you provided it. You need to upload the folder with the name `agent`.

You can find the documentation of phospho at [docs.phospho.app](https://docs.phospho.app) .

## Version

This template is compatible with phospho version `0.4`, as it now use the `session_id`.

## Requirements

This code was tested using python 3.11.

You need to have a valid phospho account to be able to deploy your agent. You can signup [here](https://phospho.app).

You need to have a valid Pinecone account to be able to use this agent. You can signup [here](https://pinecone.io). (We choose a dimension fo 1536 and used cosine similarity as metric)

You need to have a valid OpenAI account to be able to use this agent. You can signup [here](https://openai.com).

## Quickstart 

Clone this repo :
```
$ git clone {repo_url}
```

Navigate to the `agent` folder :
```
$ cd agent
```

Install the requirements :
```
$ pip install -r requirements.txt
```

Put the text you want the agent to have as knowledge in the `tmp/text.txt` file.

Setup the nescessary environment variables in the `agent/.env` file :
```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
PINECONE_ENV=YOUR_PINECONE_ENV
PINECONE_INDEX_NAME=YOUR_PINECONE_INDEX_NAME
```

Generate the embedings :
```
$ python embed.py
```
You should know have the embedings stored in Pinecone. You can check in Pinecone console.

Optionally, you can test the agent locally :
```
$ python retrieve.py
```

Update the `info.json` file with the name of your agent and a description.

Deploy to phospho. Go to your account, create a new project and uplaod the `agent` folder. It should be up and running in a few minutes. Your user can access it at `app.phospho.app/{project_name}`