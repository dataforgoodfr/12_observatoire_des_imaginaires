---
title: Choix d'une série télévisée
---

# Choisir une série télévisée

```js
const tallyUrl = "https://tally.so/r/w48jMo";
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

${results.length} séries trouvées:

```js
if (results.length > 0) {
  results
    .slice(0, 20)
    .forEach(({ id, name, original_name, production_countries }) => {
      const url = `${tallyUrl}?id=${id}&original_name=${original_name}&production_countries=${production_countries}`;
      display(html`<a href="${url}"> ${name} </a><br />`);
    });
} else {
  display(
    html`Désolé, cette série n'est pas répertoriée dans notre base.
      <a href="${tallyUrl}">Aller au questionnaire</a>`
  );
}
```

</div>

<a href="./">Retour</a>
