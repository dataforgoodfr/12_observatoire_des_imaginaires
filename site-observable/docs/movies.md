---
title: Choix d'un film
---

# Chosir un film

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
const results = db.query(
  `SELECT * FROM movies WHERE movies.title ILIKE ? ORDER BY movies.title`,
  [`${query}%`]
);
```

```js
import { html } from "npm:htl";
```

${results.length} films trouvés:

${results.length > 0 ? results.slice(0,20).forEach((movie) => display(html`<a href="${movie["tally_url"]}">
${movie["title"]}
</a><br />`)) : display(html`Désolé, ce film n'est pas répertorié dans notre base. <a href="https://tally.so/r/wQ5Og8">Aller au questionnaire</a>`)}

</div>

<a href="./">Retour</a>

