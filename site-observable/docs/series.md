---
title: Choix d'une série télévisée
---

# Sélectionnez une série télévisée

```js
const shows = FileAttachment("data/shows.csv").csv({ typed: true });
```

Entrez le nom d'une série télévisée:

```js
const query = view(Inputs.text());
```

```js
import { DuckDBClient } from "npm:@observablehq/duckdb";
const db = DuckDBClient.of({ shows: shows });
```

```js
const results = db.query(
  `SELECT * FROM shows WHERE shows.name ILIKE ? or shows.original_name ILIKE ?`,
  [`${query}%`, `${query}%`]
);
```

${Inputs.table(results)}
