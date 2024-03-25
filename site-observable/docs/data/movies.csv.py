import os
import tempfile
from datetime import datetime, timedelta

import pandas as pd

with tempfile.TemporaryDirectory() as temp_dir:
    os.chdir(temp_dir)

    os.system(
        "kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies >&2",
    )
    os.system("unzip tmdb-movies-dataset-2023-930k-movies.zip >&2")

    df = pd.read_csv("TMDB_movie_dataset_v11.csv", parse_dates=["release_date"])

    # Remove adult movies
    df = df[df["adult"] == False]  # noqa: E712

    # Calculate the date for the past two years
    years_ago = datetime.now() - timedelta(days=365 * 2)
    start_date = years_ago.replace(month=1, day=1)

    # Filter the dataframe based on the start date
    df["tally_url"] = df.apply(
        lambda row: (
            f"""https://tally.so/r/wQ5Og8"""
            f"""?original_title={row["original_title"]}"""
            f"""&production_year={row["production_year"]}"""
            f"""&production_countries={row["production_countries"]}"""
            f"""&genres={row["genres"]}"""
        ),
        axis=1,
    )

    # Select the columns we want
    df = df[["id", "title", "tally_url"]]

    print(df.to_csv(index=False))
