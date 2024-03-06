#!/bin/sh
temp_dir=$(mktemp -d)
cd "$temp_dir"
kaggle datasets download -d asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows
unzip full-tmdb-tv-shows-dataset-2023-150k-shows.zip >&2
cat TMDB_tv_dataset_v3.csv