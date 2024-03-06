---
title: Choix d'une série télévisée
---

# Sélectionnez une série télévisée

```js
const shows = FileAttachment("data/shows.csv").csv({ typed: true });
```

Nombre de séries télévisées: ${shows.length - 1}

${Inputs.table(shows)}
