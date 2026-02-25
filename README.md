# Max Milla

**Marque : AsArt'sDev**

Projet de création de livres pour enfants — développement de contenus KDP (Kindle Direct Publishing) au format PDF et MP4.

## Structure du projet

```
max_milla/
├── src/                  # Contenu source des livres
│   ├── textes/           # Textes et histoires
│   └── illustrations/    # Illustrations et images
├── assets/               # Ressources partagées (polices, couleurs, logos)
├── output/               # Fichiers générés (PDF, MP4) — non versionnés
└── README.md
```

## Formats de sortie

- **PDF** — livres imprimables et numériques pour KDP
- **MP4** — versions vidéo animées des livres

## Pour commencer

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/asmir-mln/max_milla.git
   ```
2. Placez vos fichiers sources dans `src/textes/` et `src/illustrations/`.
3. Les fichiers générés (PDF, MP4) sont à placer dans `output/` (ignoré par git).

## Licence

Voir [LICENSE](LICENSE).
