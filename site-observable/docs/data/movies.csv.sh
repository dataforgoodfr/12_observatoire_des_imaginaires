#!/bin/sh
temp_dir=$(mktemp -d)
cd "$temp_dir"
kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies >&2
unzip tmdb-movies-dataset-2023-930k-movies.zip >&2
cat TMDB_movie_dataset_v11.csv