---
title: Choix d'une série télévisée
---

# Choisir une série télévisée

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

${results.length} séries trouvées:

${results.length > 0 ? results.slice(0, 20).forEach((show) => display(html`<a href="${show["tally_url"]}">
${show["name"]}
</a><br />`)) : display(html`Désolé, cette série n'est pas répertoriée dans notre base. <a href="https://tally.so/r/wQ5Og8">Aller au questionnaire</a>`)}

</div>

<a href="./">Retour</a>
