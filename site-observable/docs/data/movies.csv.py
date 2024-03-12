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

    # Add a column with the tally URL
    df["tally_url"] = df.apply(
        lambda row: f"""https://tally.so/r/wQ5Og8?original_title={row["original_title"]}&production_year={row["release_date"][0:4]}&production_countries={row["production_countries"]}&genres={row["genres"]}""",
        axis=1,
    )

    # Select the columns we want
    df = df[["id", "title", "original_title", "tally_url"]]

    print(df.to_csv(index=False))
