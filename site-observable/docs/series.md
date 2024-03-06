---
title: Choix d'une série télévisée
---

# Sélectionnez une série télévisée

```js
import { DuckDBClient } from "npm:@observablehq/duckdb";
const db = DuckDBClient.of({
  shows: FileAttachment("data/shows.csv").csv({ typed: true }),
});
```

```js
const totalCount = db.queryRow("SELECT count() AS count FROM shows");
```

Nombre de séries télévisées: ${totalCount.count}

```js
const rows = db.query("select * from shows limit 10");
```

${rows}
