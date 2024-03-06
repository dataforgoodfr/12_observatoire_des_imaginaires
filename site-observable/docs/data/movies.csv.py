#!/bin/sh
# temp_dir=$(mktemp -d)
# cd "$temp_dir"
# kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies >&2
# unzip tmdb-movies-dataset-2023-930k-movies.zip >&2
# cat TMDB_movie_dataset_v11.csv

import os
import tempfile

import pandas as pd

with tempfile.TemporaryDirectory() as temp_dir:
    os.chdir(temp_dir)

    os.system(
        "kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies",
    )
    os.system("unzip tmdb-movies-dataset-2023-930k-movies.zip")

    df = pd.read_csv("TMDB_movie_dataset_v11.csv", nrows=100)
    print(df.to_csv(index=False))
