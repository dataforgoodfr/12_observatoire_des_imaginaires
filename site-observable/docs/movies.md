---
title: Choix d'un film
---

# Sélectionnez un film

```js
const movies = FileAttachment("data/movies.csv").csv({ typed: true });
```

Nombre de films: ${movies.length - 1}

${Inputs.table(movies)}
