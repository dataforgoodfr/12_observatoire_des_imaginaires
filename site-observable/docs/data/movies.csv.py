import os
import tempfile

import pandas as pd

with tempfile.TemporaryDirectory() as temp_dir:
    os.chdir(temp_dir)

    os.system(
        "kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies >&2",
    )
    os.system("unzip tmdb-movies-dataset-2023-930k-movies.zip >&2")

    df = pd.read_csv("TMDB_movie_dataset_v11.csv", nrows=10)
    print(df.to_csv(index=False))
