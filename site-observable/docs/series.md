---
title: Choix d'une série télévisée
---

# Sélectionnez une série télévisée

```js
const shows = FileAttachment("data/shows.csv").csv({ typed: true });
```

Entrez le nom d'un film:

```js
const text = view(Inputs.text());
```

```js
import { DuckDBClient } from "npm:@observablehq/duckdb";
const db = DuckDBClient.of({ shows: shows });
```

```js
const selected = db.query(`SELECT * FROM shows WHERE shows.name ILIKE ?`, [
  `${text}%`,
]);
```

${Inputs.table(selected)}

