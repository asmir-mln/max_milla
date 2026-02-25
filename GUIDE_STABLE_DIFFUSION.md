# 🎨 Guide Rapide - Stable Diffusion pour Max et Mila

## ✅ Installation Terminée !

Stable Diffusion WebUI est maintenant installé dans :
```
C:\Users\Asmir\Desktop\stable-diffusion-webui
```

---

## 🚀 Lancement

### Option 1 : Script automatique
Double-cliquez sur : **`launch_stable_diffusion.bat`**

### Option 2 : Manuel
1. Aller dans : `C:\Users\Asmir\Desktop\stable-diffusion-webui`
2. Double-cliquer sur : `webui-user.bat`
3. Attendre le chargement (10-30 min au 1er lancement)
4. Ouvrir : http://127.0.0.1:7860

---

## 📝 Prompts Prêts à l'Emploi pour Max et Mila

### Page 1 : Max regarde l'horizon
```
children's book illustration, young boy standing on tropical beach, looking at horizon, dreamy expression, colorful sky, adventure theme, vibrant colors, professional quality, 4k, detailed
```

### Page 2 : Perroquet apparaît
```
children's book illustration, colorful parrot flying down from blue sky, tropical setting, vibrant red and green feathers, friendly expression, dynamic pose, children's book style, 4k
```

### Page 3 : "MON TRÉSOR!"
```
children's book illustration, talking parrot with speech bubble saying "MY TREASURE!", comic book style, bright colors, expressive parrot, professional children's book art, detailed feathers
```

### Page 4 : Île mystérieuse
```
children's book illustration, mysterious tropical island with palm trees, hidden secrets, magical atmosphere, colorful vegetation, adventure setting, professional quality
```

### Page 5 : Bateau pirate
```
children's book illustration, old pirate ship in distance on ocean, sailing boat with tattered sails, dramatic but child-friendly, colorful ocean waves, adventure theme
```

### Page 6 : Max a peur
```
children's book illustration, worried young boy, expressing fear but brave, tropical beach setting, emotional closeup, supportive atmosphere, warm colors
```

### Page 7 : Mila encourage Max
```
children's book illustration, two children friends supporting each other, girl encouraging boy, tropical island, friendship theme, warm and positive, colorful
```

### Page 8 : Coffre au trésor
```
children's book illustration, ancient treasure chest shining in sunlight, closed mysterious chest, tropical beach setting, magical glow, detailed and colorful
```

### Page 9 : Danger approche
```
children's book illustration, shadow of danger approaching, suspenseful but child-appropriate, dramatic lighting, tropical island setting, adventure book style
```

### Page 10 : Max courageux
```
children's book illustration, brave young boy standing confidently, determined expression, hero pose, tropical setting, inspiring and positive, vibrant colors
```

### Page 11 : Pas d'or mais...
```
children's book illustration, open treasure chest revealing no gold, unexpected discovery, wisdom theme, beautiful colors, tropical beach sunset
```

### Page 12 : Le vrai trésor (courage)
```
children's book illustration, young boy discovering inner courage, glowing heart symbol, inspirational moment, magical atmosphere, warm sunset colors, professional children's book art
```

---

## ⚙️ Paramètres Recommandés Amazon KDP

### Dans Stable Diffusion :

**Prompt (en haut)**
- Copiez-collez un des prompts ci-dessus
- Ajoutez : `, high resolution, 300 dpi quality`

**Negative Prompt**
```
ugly, poorly drawn, low quality, blurry, distorted, adult content, scary, gore, violence
```

**Paramètres** :
- **Sampling Method** : DPM++ 2M Karras
- **Sampling Steps** : 30-50
- **Width & Height** : 1024×1024 (ou plus si possible)
- **CFG Scale** : 7-9
- **Batch Size** : 1
- **Batch Count** : 4 (génère 4 variations)

**Après génération** :
1. Clic droit sur l'image → Sauvegarder
2. Renommer : `page01.png`, `page02.png`, etc.
3. Copier dans : `illustrations_kids/` ou `illustrations_adult/`
4. Utiliser `enhance_for_amazon.py` pour optimiser à 2560×2560 @ 300 DPI

---

## 🎭 Styles Recommandés

### Pour Version Enfants (4-10 ans)
Ajouter au prompt :
```
, cartoon style, bright colors, friendly characters, cheerful atmosphere, Disney Pixar style
```

### Pour Version Adulte
Ajouter au prompt :
```
, realistic illustration, professional book cover art, elegant style, literary quality, sophisticated colors
```

---

## 📦 Télécharger Modèles Supplémentaires

Pour de meilleurs résultats, téléchargez des modèles spécialisés :

### 1. DreamShaper (Style enfants coloré)
- URL : https://civitai.com/models/4384/dreamshaper
- Télécharger : DreamShaper 8
- Placer dans : `stable-diffusion-webui\models\Stable-diffusion\`

### 2. Realistic Vision (Style réaliste)
- URL : https://civitai.com/models/4201/realistic-vision
- Télécharger : Realistic Vision V5.1
- Placer dans : `stable-diffusion-webui\models\Stable-diffusion\`

### 3. Anything V5 (Style manga/anime)
- URL : https://civitai.com/models/9409/anything
- Télécharger : Anything V5
- Placer dans : `stable-diffusion-webui\models\Stable-diffusion\`

**Après téléchargement** :
1. Copier le fichier `.safetensors` dans le dossier models
2. Redémarrer Stable Diffusion
3. Sélectionner le modèle en haut à gauche de l'interface

---

## 🔧 Workflow Complet

1. **Lancer Stable Diffusion**
   ```
   Double-clic sur: launch_stable_diffusion.bat
   ```

2. **Générer les 12 pages**
   - Utiliser les prompts ci-dessus
   - Générer 4 variations par page
   - Choisir la meilleure

3. **Sauvegarder les images**
   - Renommer : page01.png à page12.png
   - Copier dans : `illustrations_kids/` ou `illustrations_adult/`

4. **Optimiser pour Amazon**
   ```powershell
   python enhance_for_amazon.py
   ```
   - Choisir option 1 (enfants) ou 2 (adultes)
   - Images optimisées dans : `illustrations_kids_amazon/`

5. **Générer les PDFs**
   ```powershell
   python generate_final_books.py
   ```

6. **Vérifier la qualité**
   - Ouvrir les PDFs générés
   - Vérifier résolution, couleurs, netteté
   - Prêt pour Amazon KDP !

---

## 💡 Astuces Pro

### Cohérence des personnages
Pour que Max et Mila aient la même apparence sur toutes les pages :

1. Générer le premier portrait de MaxMax
2. Noter les caractéristiques visibles
3. Ajouter une description précise dans tous les prompts :
   ```
   young boy with brown hair, blue shirt, 8 years old, same character throughout
   ```

### Améliorer la qualité
- **Upscale** : Après génération, cliquez sur "Send to extras" → Upscale 2x
- **Inpainting** : Pour corriger des détails, utilisez l'onglet "Inpaint"
- **ControlNet** : Pour plus de contrôle (extension avancée)

### Gagner du temps
1. Sauvegarder vos prompts favoris dans un fichier texte
2. Utiliser "Prompt styles" dans Stable Diffusion
3. Générer plusieurs variations d'un coup (Batch Count)

---

## 📞 Support

### Problèmes Communs

**"Out of memory"**
- Réduire la résolution : 768×768 au lieu de 1024×1024
- Fermer d'autres applications
- Redémarrer Stable Diffusion

**"Missing model"**
- Le modèle par défaut se télécharge au 1er lancement
- Attendre patiemment (peut prendre 10-30 minutes)
- Vérifier votre connexion internet

**Images de mauvaise qualité**
- Augmenter "Sampling Steps" à 50
- Essayer un autre "Sampling Method"
- Télécharger un modèle spécialisé (DreamShaper)

---

## 🎉 C'est Parti !

Vous êtes maintenant prêt à créer des illustrations professionnelles pour Amazon KDP !

**Prochaine étape** : Double-cliquez sur `launch_stable_diffusion.bat` 🚀
