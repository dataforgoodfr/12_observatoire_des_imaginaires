Observatoire des imaginaires
================


## Installing with poetry

### Prerequisites:

1. Python (≥ `3.10`) installed on your system.
2. Ensure you have `poetry` installed. If not, you can install them using `pip`.

```bash
pip install poetry
```

### Steps:

1. **Clone the GitHub Repository:**

   Clone the GitHub repository you want to install locally using the `git clone` command.

   ```bash
   git clone https://github.com/dataforgoodfr/12_observatoire_des_imaginaires.git
   ```

2. **Navigate to the Repository Directory:**

   Use the `cd` command to navigate into the repository directory.

   ```bash
   cd 12_observatoire_des_imaginaires/
   ```

3. **Configure `poetry` to create a Virtual Environment inside the project:**

   Ensure that poetry will create a `.venv` directory into the project with the command:

   ```bash
   poetry config virtualenvs.in-project true
   ```

4. **Install Project Dependencies using `poetry`:**

   Use `poetry` to install the project dependencies.

   ```bash
   poetry install
   ```

   This will read the `pyproject.toml` file in the repository and install all the dependencies specified.

5. **Activate the Virtual Environment:**

   Activate the virtual environment to work within its isolated environment.

   On Unix or MacOS:

   ```bash
   poetry shell
   ```

6. **Run & edit notebooks**:

   ```bash
   jupyter notebook
   ```

## Download datasets from kaggle 

If you want to use kaggle to download datasets, please make sure to have api's credentials in ~/.kaggle/kaggle.json.

How to get .json with kaggle api's credentials : [here](https://github.com/Kaggle/kaggle-api#api-credentials)

Once you have setup your venv with poetry, you can use commands in the Makefile to download tmdb datasets from kaggle :

```bash
make download-tmdb-movies-dataset
make download-full-tmdb-tv-shows-dataset
```


Alternatively you can download directly the datasets from kaggle website :
- [tmdb-movies-dataset](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies)
- [full-tmdb-tv-shows-dataset](https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows)

## Website to select a specific movie or TV show

The [site-observable](https://github.com/dataforgoodfr/12_observatoire_des_imaginaires/tree/main/site-observable) directory contains
an observable framework site that collect film and movie data from the above datasets on kaggle and filters the datasets according
to the following rules in order to reduced the size of the data present on the generated web site.  This site provides a search UI
allow a user to select a specific movie or TV show.  The user can then click on the link for their selection to kick off the
questionnaire on tally andis destined to be embedded in an iframe in the main Observatoire des Imaginaires web site.

Movies:
- filter out adult movies
- filter out movies released more that two years ago

TV Shows:
- filter out adult shows

The web site is currently hosted on the [Observable hosting platform](https://observablehq.com/) and is available at the following URL:

https://observatoire-des-imaginaires.observablehq.cloud/questionnaire

## Run precommit-hook locally

[Install precommits](https://pre-commit.com/)


    pre-commit run --all-files 
 

## Use Tox to test your code

    tox -vv
