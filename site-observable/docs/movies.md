---
title: Choix d'un film
---

# Chosir un film

```js
const tallyUrl = "https://tally.so/r/wa6jyb";
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

```js
if (results.length > 0) {
  results
    .slice(0, 20)
    .forEach(
      ({
        id,
        title,
        original_title,
        production_year,
        production_countries,
        genres,
      }) => {
        const url = `${tallyUrl}?id=${id}&original_title=${original_title}&production_year=${production_year}&production_countries=${
          production_countries || ""
        }&genres=${genres || ""}`;
        display(html`<a href="${url}">${title}</a><br />`);
      }
    );
} else {
  display(
    html`Désolé, ce film n'est pas répertorié dans notre base.
      <a href="${tallyUrl}">Aller au questionnaire</a>`
  );
}
```

</div>

<a href="./">Retour</a>
