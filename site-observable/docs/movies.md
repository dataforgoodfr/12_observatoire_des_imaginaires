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

```js
import { html } from "npm:htl";
```

Films sélectionnés (${results.length} résultat(s)):

${results.length <=20 ? results.forEach((movie) => display(html`<a href="${movie["tally_url"]}">
${movie["title"]}
</a><br />`)) : ""}

</div>

<input type="button" value="Menu Principal" onClick="window.location.href='./'" />
