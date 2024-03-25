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
    df = df[df["release_date"] >= start_date]

    # Add a column with the production_year based on the release_date
    df["production_year"] = df["release_date"].dt.year

    # Select the columns we want
    df = df[
        ["id", "title", "original_title", "production_year", "production_countries", "genres"]
    ]

    print(df.to_csv(index=False))
