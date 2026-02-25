# Max et Mila et le Perroquet Mystérieux

## 📖 Description
Livre pour enfants bilingue généré avec illustrations IA professionnelles, optimisé pour publication Amazon KDP.

**Deux versions** :
- 🎨 **Version Enfants (4-10 ans)** : Style BD coloré avec bulles de dialogue
- 📚 **Version Adulte** : Style littéraire élégant et sophistiqué

## ✨ Fonctionnalités

- ✅ Génération de PDF haute qualité (300 DPI)
- ✅ Illustrations réalistes avec Stable Diffusion
- ✅ API REST pour gestion des images
- ✅ Interface web de visualisation
- ✅ Scripts d'optimisation pour Amazon KDP (2560×2560 px)
- ✅ 12 pages + couvertures recto/verso

## 🎨 Génération d'Illustrations

### Option 1 : Stable Diffusion (Recommandé)
```bash
# Installation automatique
.\install_stable_diffusion.bat

# Lancement
.\launch_stable_diffusion.bat
```

### Option 2 : Leonardo.ai
- 150 images gratuites/jour
- https://leonardo.ai

### Option 3 : Amélioration d'images existantes
```bash
python enhance_for_amazon.py
```

## 🚀 Installation

### Prérequis
- Python 3.14+
- Git
- XAMPP (pour l'API web)
- FFmpeg (optionnel)

### Installation rapide
```bash
# Cloner le repo
git clone https://github.com/VOTRE_USERNAME/max-mila-livre.git
cd max-mila-livre

# Créer environnement virtuel
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Installer dépendances
pip install -r requirements.txt
```

## 📦 Structure du Projet

```
max-mila-livre/
├── illustrations_kids/          # Images version enfants
├── illustrations_adult/         # Images version adultes
├── output/                      # PDFs générés
├── livre_format_3/             # Module génération PDF
├── C:\xampp\htdocs\max_mila_livre/  # Interface web
│   ├── api.php                 # API REST
│   ├── api_test.html          # Interface test API
│   ├── books.html             # Visualiseur de livres
│   └── assets/img/            # Images web
├── generate_illustrations.py   # Générateur illustrations
├── generate_final_books.py    # Assembleur PDF final
├── enhance_for_amazon.py      # Optimisation Amazon KDP
├── install_stable_diffusion.bat
├── launch_stable_diffusion.bat
└── README.md
```

## 🎯 Usage

### 1. Générer les illustrations

#### Avec Stable Diffusion
```bash
.\launch_stable_diffusion.bat
# Utiliser les prompts du GUIDE_STABLE_DIFFUSION.md
```

#### Avec le script Python
```bash
python generate_illustrations.py
```

### 2. Créer les couvertures
```bash
python create_covers.py
```

### 3. Optimiser pour Amazon KDP
```bash
python enhance_for_amazon.py
# Choisir option 3 (les deux versions)
```

### 4. Générer les PDFs finaux
```bash
python generate_final_books.py
```

### 5. Lancer l'interface web
```bash
# Démarrer Apache
.\start_server.bat

# Ouvrir dans le navigateur
# http://localhost/max_mila_livre/api_test.html
```

## 📚 API REST

### Endpoints disponibles

```http
# Liste des images
GET /api.php?endpoint=list&edition=kids

# Récupérer une image
GET /api.php?endpoint=get&edition=kids&page=page01

# Informations image
GET /api.php?endpoint=info&edition=kids&page=page01

# Statistiques
GET /api.php?endpoint=stats

# Générer nouvelles illustrations
POST /api.php?endpoint=generate
```

### Exemple JavaScript
```javascript
// Lister les images
fetch('http://localhost/max_mila_livre/api.php?endpoint=list')
    .then(res => res.json())
    .then(data => console.log(data));
```

## 📖 Histoire (12 Pages)

1. Max rêve d'aventure sur la plage
2. Un perroquet mystérieux apparaît
3. "MON TRÉSOR !" crie-t-il
4. Découverte d'une île magique
5. Un bateau pirate surgit
6. Max a peur face à l'inconnu
7. Mila lui rappelle son courage
8. Le coffre au trésor brille
9. Le danger approche
10. Max trouve son courage
11. Le trésor n'est pas de l'or
12. Le vrai trésor est en lui

## 🎨 Prompts Stable Diffusion

Voir le fichier `GUIDE_STABLE_DIFFUSION.md` pour les 12 prompts prêts à l'emploi.

**Exemple Page 1** :
```
children's book illustration, young boy standing on tropical beach, 
looking at horizon, dreamy expression, colorful sky, adventure theme, 
vibrant colors, professional quality, 4k, detailed
```

## 📐 Spécifications Amazon KDP

- **Résolution** : 2560×2560 pixels minimum
- **DPI** : 300
- **Format** : PNG ou JPEG haute qualité
- **Profil couleur** : sRGB
- **Taille fichier** : < 50 MB par image

## 🛠️ Scripts Utiles

| Script | Description |
|--------|-------------|
| `start_server.bat` | Démarre Apache (XAMPP) |
| `stop_server.bat` | Arrête Apache |
| `install_stable_diffusion.bat` | Installe Stable Diffusion WebUI |
| `launch_stable_diffusion.bat` | Lance Stable Diffusion |
| `generate_illustrations.py` | Génère illustrations Python |
| `enhance_for_amazon.py` | Optimise pour Amazon KDP |
| `generate_final_books.py` | Assemble les PDFs finaux |

## 📊 Résultats

### PDFs Générés
- `Max_Mila_Kids_BD.pdf` (1.02 MB, 14 pages)
- `Max_Mila_Adult_Edition.pdf` (0.82 MB, 14 pages)

### Statistiques
- 28 illustrations totales (14 enfants + 14 adultes)
- Résolution : 2362×2362 @ 300 DPI
- Format A4 : 20×20 cm
- Qualité print professionnelle

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Asmir MLN**
- Projet : Max et Mila et le Perroquet Mystérieux
- Date : Février 2026

## 🙏 Remerciements

- Stable Diffusion WebUI (AUTOMATIC1111)
- ReportLab pour génération PDF
- Pillow pour traitement d'images
- Leonardo.ai pour alternative IA

## 📞 Support

Pour toute question ou problème :
1. Consulter `GUIDE_STABLE_DIFFUSION.md`
2. Consulter `OPTIONS_PRO_AMAZON.md`
3. Consulter `DEMARRAGE_RAPIDE.md`
4. Ouvrir une issue sur GitHub

---

⭐ **N'oubliez pas de mettre une étoile si ce projet vous aide !** ⭐
