---
title: Choix d'un film
---

# Sélectionnez un film

```js
const movies = FileAttachment("data/movies.csv").csv({ typed: true });
```

Entrez le nom d'un film:

```js
const query = view(Inputs.text());
```

```js
import { DuckDBClient } from "npm:@observablehq/duckdb";
const db = DuckDBClient.of({ movies: movies });
```

```js
const results = db.query(`SELECT * FROM movies WHERE movies.title ILIKE ?`, [
  `${query}%`,
]);
```

${Inputs.table(results)}
