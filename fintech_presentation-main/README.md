# Demo of Fintech Idea
This repo contains bare-bones implementation of the very simple Fintech business - issuing loans to private individuals.
This idea is based on the [Lending Club](https://www.kaggle.com/wordsforthewise/lending-club) data from Kaggle.

## Implementation
The repo contains 4 services:
1. [Streamlit UI](https://www.streamlit.io/) where customers fill their application
2. Statistical Model (Regression) running on [FastAPI](https://fastapi.tiangolo.com/)
3. Postgres Database that stores requests and responses
4. [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) to analyse the data

## How to run it on the laptop?
First, based on the operating system, install [Docker](https://www.docker.com/). After that, next steps are:
1. Download data from [Kaggle](https://www.kaggle.com/wordsforthewise/lending-club)
2. Clone the repo
3. Go to _model_ folder
4. Place the download data from (1)
5. Use run **model_building.ipynb** to build the model (logistic regression) and save the artifacts
6. In the root folder of the project, create empty folder "data". Here we will store Postgres data
7. Go back up to the root folder. In the terminal run `docker-compose up -d` - this will build required containers and spin up the application
8. After the build step is finished (if everything went well) you should be able to see the app:

- localhost:2222 -> streamlit UI
- localhost:1111 -> fastAPI serving the model
- localhost:4444 -> postgres (this will not open in browser)
- localhost:3333 -> jupyterLab instance (password: secret_stuff)

9. To analyse the data / checkout moddel API, use **explose.ipynb** notebook in the project root folder. Make sure to open it from Jupyter that has been spun up by docker-compose, else you won't be able to easily connect to API or Database.

## Potential problems
If you are running Windows, most probably Jupyter won't map the root folder.

Based on OS, you may need to change "localhost" to "0.0.0.0". 
