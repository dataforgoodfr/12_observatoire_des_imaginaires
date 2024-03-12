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
const results = db.query(`SELECT * FROM shows WHERE shows.name ILIKE ?`, [
  `${query}%`,
]);
```

```js
import { html } from "npm:htl";
```

Séries sélectionnées (${results.length} résultat(s)):

${results.length <=20 ? results.forEach((show) => display(html`<a href="${show["tally_url"]}">
${show["name"]}
</a><br />`)) : ""}

</div>

<input type="button" value="Menu Principal" onClick="window.location.href='../'" />
