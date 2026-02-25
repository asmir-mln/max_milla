# 🎨 Max et Mila - API d'Illustrations Réalistes

## 📋 Description

API REST complète pour gérer et générer des illustrations réalistes pour le livre "Max et Mila et le Perroquet Mystérieux".

L'API permet de :
- ✅ Lister toutes les illustrations disponibles
- ✅ Récupérer des images spécifiques
- ✅ Générer de nouvelles illustrations
- ✅ Consulter les statistiques du projet
- ✅ Obtenir des informations détaillées sur chaque image

---

## 🚀 Démarrage Rapide

### Prérequis

- **XAMPP** installé et actif
- **Python 3.14.2** avec environnement virtuel
- **Bibliothèques Python** : Pillow, reportlab

### Installation

1. **Copier les fichiers API dans XAMPP**
   ```bash
   C:\xampp\htdocs\max_mila_livre\
   ├── api.php              # API REST principale
   ├── api_test.html        # Interface de test
   ├── books.html           # Visualiseur de livres
   └── assets/
       └── img/
           ├── kids/        # Images version enfants
           └── adult/       # Images version adultes
   ```

2. **Démarrer XAMPP**
   - Lancer Apache

3. **Accéder à l'interface**
   - Interface de test : http://localhost/max_mila_livre/api_test.html
   - Visualiseur : http://localhost/max_mila_livre/books.html
   - API directe : http://localhost/max_mila_livre/api.php

---

## 📚 Documentation API

### Base URL
```
http://localhost/max_mila_livre/api.php
```

---

### 🔹 **GET** `/api.php?endpoint=list`

Liste toutes les illustrations disponibles.

**Paramètres (optionnels)**
- `edition` : `kids` | `adult` | `all` (défaut: `all`)

**Exemple de requête**
```bash
GET http://localhost/max_mila_livre/api.php?endpoint=list&edition=kids
```

**Réponse**
```json
{
  "success": true,
  "data": {
    "kids": [
      {
        "filename": "page01.png",
        "url": "/max_mila_livre/assets/img/kids/page01.png",
        "size": 524288,
        "modified": 1735190400
      }
    ]
  }
}
```

---

### 🔹 **GET** `/api.php?endpoint=get`

Récupère une image spécifique.

**Paramètres (requis)**
- `edition` : `kids` | `adult`
- `page` : nom du fichier (ex: `page01`, `cover`)

**Exemple de requête**
```bash
GET http://localhost/max_mila_livre/api.php?endpoint=get&edition=kids&page=page01
```

**Réponse**
- Image PNG brute (Content-Type: image/png)

---

### 🔹 **GET** `/api.php?endpoint=info`

Informations détaillées sur une image.

**Paramètres (requis)**
- `edition` : `kids` | `adult`
- `page` : nom du fichier

**Exemple de requête**
```bash
GET http://localhost/max_mila_livre/api.php?endpoint=info&edition=kids&page=page01
```

**Réponse**
```json
{
  "success": true,
  "data": {
    "filename": "page01.png",
    "size": 524288,
    "size_readable": "512.00 KB",
    "modified": "2026-02-25 14:30:00",
    "dimensions": [2362, 2362, 3, "RGB"],
    "mime_type": "image/png"
  }
}
```

---

### 🔹 **POST** `/api.php?endpoint=generate`

Génère de nouvelles illustrations en exécutant le script Python.

**Paramètres (POST)**
- `type` : `kids` | `adult` | `all` (défaut: `all`)
- `style` : `default` | `realistic` (défaut: `default`)

**Exemple de requête**
```javascript
fetch('http://localhost/max_mila_livre/api.php?endpoint=generate', {
    method: 'POST',
    body: new FormData({
        type: 'all',
        style: 'realistic'
    })
});
```

**Réponse**
```json
{
  "success": true,
  "message": "Illustrations générées avec succès",
  "output": "✅ 12 pages générées...",
  "returnCode": 0
}
```

---

### 🔹 **GET** `/api.php?endpoint=stats`

Statistiques globales du projet.

**Exemple de requête**
```bash
GET http://localhost/max_mila_livre/api.php?endpoint=stats
```

**Réponse**
```json
{
  "success": true,
  "data": {
    "kids_count": 14,
    "adult_count": 14,
    "total_images": 28,
    "total_size": 1929216,
    "total_size_readable": "1.84 MB",
    "last_update": "2026-02-25 15:00:00"
  }
}
```

---

### 🔹 **GET** `/api.php` (sans endpoint)

Documentation interactive de l'API.

**Réponse**
```json
{
  "name": "Max et Mila API",
  "version": "1.0.0",
  "description": "API REST pour gérer les illustrations du livre",
  "endpoints": [...]
}
```

---

## 🎨 Script Python - Générateur d'Illustrations

### Fichier : `generate_realistic_api.py`

Ce script génère des illustrations réalistes avec des effets avancés :

**Fonctionnalités**
- ✅ Gradients de couleurs réalistes
- ✅ Textures et bruits pour effet naturel
- ✅ Ombres douces avec flou gaussien
- ✅ Personnages détaillés (yeux, cheveux, vêtements)
- ✅ Perroquet multicolore avec plumes
- ✅ Bulles de texte style BD
- ✅ Scènes d'océan avec vagues
- ✅ Ciel avec nuages animés

**Utilisation**
```bash
# Activer l'environnement virtuel
.\.venv\Scripts\Activate.ps1

# Exécuter le générateur
python generate_realistic_api.py
```

**Sortie**
- 12 images dans `illustrations_kids/` (style BD coloré)
- 12 images dans `illustrations_adult/` (style littéraire élégant)
- Résolution : 2362×2362 pixels @ 300 DPI

---

## 🖥️ Interface Web

### Page de test de l'API : `api_test.html`

Interface complète avec :
- 📊 **Tableau de bord statistiques** en temps réel
- 🖼️ **Galerie d'images** interactive avec modal
- ⚡ **Boutons de génération** pour créer de nouvelles illustrations
- 📚 **Documentation API** intégrée avec tests en un clic

**URL** : http://localhost/max_mila_livre/api_test.html

---

## 🔧 Configuration

### Chemins des fichiers

Modifier dans `api.php` :
```php
define('IMAGES_KIDS_DIR', __DIR__ . '/assets/img/kids/');
define('IMAGES_ADULT_DIR', __DIR__ . '/assets/img/adult/');
```

Modifier dans `generate_realistic_api.py` :
```python
OUTPUT_KIDS = "illustrations_kids"
OUTPUT_ADULT = "illustrations_adult"
DPI = 300
SIZE_PX = 2362
```

---

## 📦 Structure du Projet

```
max_mila_livre/
├── api.php                      # API REST principale
├── api_test.html                # Interface de test
├── books.html                   # Visualiseur de livres
├── index.html                   # Page principale
├── assets/
│   └── img/
│       ├── kids/                # 14 images (cover + 12 pages + back)
│       │   ├── cover.png
│       │   ├── page01.png
│       │   ├── ...
│       │   ├── page12.png
│       │   └── back_cover.png
│       └── adult/               # 14 images (cover + 12 pages + back)
│           ├── cover.png
│           ├── page01.png
│           ├── ...
│           ├── page12.png
│           └── back_cover.png
└── output/
    ├── Max_Mila_Kids_BD.pdf     # PDF 14 pages version enfants
    └── Max_Mila_Adult_Edition.pdf # PDF 14 pages version adulte
```

---

## 🎯 Exemples d'utilisation

### JavaScript (Fetch API)

```javascript
// Lister toutes les images
fetch('http://localhost/max_mila_livre/api.php?endpoint=list')
    .then(res => res.json())
    .then(data => console.log(data));

// Récupérer une image
fetch('http://localhost/max_mila_livre/api.php?endpoint=get&edition=kids&page=page01')
    .then(res => res.blob())
    .then(blob => {
        const img = document.createElement('img');
        img.src = URL.createObjectURL(blob);
        document.body.appendChild(img);
    });

// Générer de nouvelles illustrations
const formData = new FormData();
formData.append('type', 'all');
formData.append('style', 'realistic');

fetch('http://localhost/max_mila_livre/api.php?endpoint=generate', {
    method: 'POST',
    body: formData
})
    .then(res => res.json())
    .then(data => console.log(data));
```

### Python (Requests)

```python
import requests

# Lister les images
response = requests.get('http://localhost/max_mila_livre/api.php?endpoint=list')
print(response.json())

# Télécharger une image
response = requests.get(
    'http://localhost/max_mila_livre/api.php?endpoint=get',
    params={'edition': 'kids', 'page': 'page01'}
)
with open('downloaded_image.png', 'wb') as f:
    f.write(response.content)

# Obtenir les statistiques
response = requests.get('http://localhost/max_mila_livre/api.php?endpoint=stats')
stats = response.json()
print(f"Total d'images: {stats['data']['total_images']}")
```

### cURL

```bash
# Lister les images
curl "http://localhost/max_mila_livre/api.php?endpoint=list&edition=kids"

# Télécharger une image
curl "http://localhost/max_mila_livre/api.php?endpoint=get&edition=kids&page=page01" -o page01.png

# Statistiques
curl "http://localhost/max_mila_livre/api.php?endpoint=stats"

# Générer nouvelles illustrations
curl -X POST "http://localhost/max_mila_livre/api.php?endpoint=generate" \
     -F "type=all" \
     -F "style=realistic"
```

---

## ⚠️ Gestion des erreurs

L'API retourne toujours un objet JSON avec `success: true/false`.

**Exemples d'erreurs**
```json
{
  "success": false,
  "error": "Paramètres manquants: edition et page requis"
}
```

```json
{
  "success": false,
  "error": "Image non trouvée"
}
```

---

## 🔐 Sécurité

**CORS** : L'API accepte les requêtes cross-origin (pour développement local)
```php
header('Access-Control-Allow-Origin: *');
```

**⚠️ Pour la production**, restreindre les origines autorisées :
```php
header('Access-Control-Allow-Origin: https://votre-domaine.com');
```

---

## 📝 Notes de Développement

### Version Enfants (Kids)
- Style BD coloré
- Personnages simplifiés
- Bulles de dialogue
- Couleurs vives (#87CEEB, #FF1493, #FFD700)

### Version Adulte (Adult)
- Style littéraire élégant
- Fonds artistiques avec gradients
- Texte positionné dans zone dédiée
- Couleurs sobres (#2C3E50, #DAA520, #F5F5DC)

---

## 📄 Licence

Projet personnel - Max et Mila © 2026 Asmir MLN

---

## 🆘 Support

Pour toute question ou problème :
1. Vérifier que XAMPP/Apache est actif
2. Vérifier les permissions des dossiers
3. Consulter les logs PHP dans XAMPP
4. Tester l'API via `api_test.html`

---

## 🎉 Crédits

**Auteur** : Asmir MLN  
**Date** : Février 2026  
**Version** : 1.0.0  
**Technologies** : PHP 8.x, Python 3.14, Pillow, ReportLab, HTML5/CSS3/JavaScript
