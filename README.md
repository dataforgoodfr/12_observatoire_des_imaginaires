Observatoire des imagiaires
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

## Run precommit-hook locally

[Install precommits](https://pre-commit.com/)


    pre-commit run --all-files 
 

## Use Tox to test your code

    tox -vv