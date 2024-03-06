import os
import tempfile

import pandas as pd

with tempfile.TemporaryDirectory() as temp_dir:
    os.chdir(temp_dir)

    os.system(
        "kaggle datasets download -d asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows",
    )
    os.system("unzip full-tmdb-tv-shows-dataset-2023-150k-shows.zip")

    df = pd.read_csv("TMDB_tv_dataset_v3.csv")
    df_first_ten_rows = df.head(10)
    print(df_first_ten_rows.to_csv(index=False))
