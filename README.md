Observatoire des imagiaires
================


# Requirements

If you want to use kaggle to download datasets, please make sure to have api's credentials in ~/.kaggle/kaggle.json.
How to get .json with kaggle api's credentials : [here](https://github.com/Kaggle/kaggle-api#api-credentials)

Once you have setup your venv with poetry, you can use commands in the Makefile to download tmdb datasets from kaggle.


## Use a venv 

    python3 -m venv name-of-your-venv

    source name-of-your-venv/bin/activate


## Utiliser Poetry

[Installer Poetry](https://python-poetry.org/docs/):

    python3 -m pip install "poetry==1.4.0"

Installer les dépendances:

    poetry install

Ajouter une dépendance:

    poetry add pandas

Mettre à jour les dépendances:

    poetry update

## Utiliser Jupyter Notebook

    jupyter notebook

and check your browser !

## Lancer les precommit-hook localement

[Installer les precommit](https://pre-commit.com/)


    pre-commit run --all-files 
 

## Utiliser Tox pour tester votre code

    tox -vv