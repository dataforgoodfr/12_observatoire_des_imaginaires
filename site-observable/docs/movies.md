---
title: Choix d'un film
---

# Sélectionnez un film

```js
import { DuckDBClient } from "npm:@observablehq/duckdb";
const db = DuckDBClient.of({
  movies: FileAttachment("data/movies.csv").csv({ typed: true }),
});
```

```js
const totalCount = db.queryRow("SELECT count() AS count FROM movies");
```

Nombre de films: ${totalCount.count - 1}

```js
const rows = db.query("select * from movies limit 10");
```

${Inputs.table(rows)}
