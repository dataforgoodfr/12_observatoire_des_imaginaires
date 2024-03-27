import os
import tempfile

import pandas as pd

with tempfile.TemporaryDirectory() as temp_dir:
    os.chdir(temp_dir)

    os.system(
        "kaggle datasets download -d asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows >&2",
    )
    os.system("unzip full-tmdb-tv-shows-dataset-2023-150k-shows.zip >&2")

    df = pd.read_csv("TMDB_tv_dataset_v3.csv")

    # Remove adult movies
    df = df[df["adult"] == False]  # noqa: E712

    # Select the columns we want
    df = df[["id", "name", "original_name", "production_countries"]]

    print(df.to_csv(index=False))
