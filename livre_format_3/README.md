# Livre Format 3 - Générateur Python

Projet structuré pour générer un troisième format du livre "Max et Mila et le Perroquet Mystérieux".

## Structure du Projet

```
livre_format_3/
├── main.py                 # Script principal
├── config.py              # Configuration du projet
├── src/
│   ├── __init__.py        # Package Python
│   ├── page_generator.py  # Génération des pages individuelles
│   └── pdf_creator.py     # Création du PDF final
├── output/                # Répertoire de sortie (créé automatiquement)
└── README.md              # Ce fichier
```

## Features

- **Génération de pages**: Chaque page contient une illustration et du texte
- **Personnalisation**: Configuration centralisée pour polices, couleurs, dimensions
- **PDF**: Export automatique en format PDF
- **Modularité**: Code organisé en modules réutilisables

## Configuration

Éditer `config.py` pour personnaliser:
- Dimensions des pages
- Chemins des fichiers d'entrée/sortie
- Polices et couleurs
- Tailles de texte

## Modules

### page_generator.py
- `create_blank_page()`: Crée une page vierge
- `add_title()`: Ajoute un titre
- `add_illustration()`: Ajoute une illustration
- `add_text_box()`: Ajoute une boîte de texte
- `generate_page()`: Génère une page complète
- `generate_all_pages()`: Génère toutes les pages

### pdf_creator.py
- `create_pdf()`: Crée un PDF à partir des pages PNG
- `merge_pdfs()`: Fusionne plusieurs PDFs (nécessite PyPDF2)
- `get_pdf_info()`: Affiche les infos du PDF

## Utilisation

```bash
python main.py
```

Le script génère automatiquement:
1. Les fichiers PNG des pages (dans `output/`)
2. Le fichier PDF final (`output/Max_Mila_Version3_Format.pdf`)

## Dépendances

- Pillow (PIL): Traitement d'images
- reportlab: Génération de PDF
- PyPDF2 (optionnel): Fusion de PDFs

```bash
pip install pillow reportlab
pip install PyPDF2  # optionnel
```

## Auteur

Asmir MLN - 2026
