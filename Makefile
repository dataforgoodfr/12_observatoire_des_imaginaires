download-tmdb-movies-dataset:
	mkdir data -p ; cd data ; kaggle datasets download -d asaniczka/tmdb-movies-dataset-2023-930k-movies

download-full-tmdb-tv-shows-dataset:
	mkdir data -p ; cd data ; kaggle datasets download -d asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows
