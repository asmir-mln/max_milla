# 🚀 Démarrage Rapide - Max et Mila

## ⚡ Lancement du serveur

### Option 1 : Fichier Batch (Recommandé)
Double-cliquez sur : **`start_server.bat`**

Ce fichier va :
- ✅ Démarrer Apache automatiquement
- ✅ Vérifier que le serveur fonctionne
- ✅ Ouvrir l'interface web dans votre navigateur

### Option 2 : XAMPP Control Panel
1. Ouvrir `C:\xampp\xampp-control.exe`
2. Cliquer sur **Start** à côté de "Apache"
3. Aller sur http://localhost/max_mila_livre/api_test.html

---

## 🛑 Arrêt du serveur

Double-cliquez sur : **`stop_server.bat`**

---

## 🌐 URLs Importantes

| Page | URL |
|------|-----|
| 🎨 Interface API | http://localhost/max_mila_livre/api_test.html |
| 📚 Visualiseur de livres | http://localhost/max_mila_livre/books.html |
| 📖 Documentation API | http://localhost/max_mila_livre/api.php |
| 🏠 Page d'accueil | http://localhost/max_mila_livre/ |

---

## ❌ Résolution de problèmes

### Erreur : ERR_CONNECTION_REFUSED

**Solution** : Le serveur Apache n'est pas démarré
1. Double-cliquez sur `start_server.bat`
2. OU ouvrez XAMPP Control Panel et démarrez Apache

### Erreur : Port 80 déjà utilisé

**Solution** : Un autre programme utilise le port 80 (Skype, IIS, etc.)
1. Fermez les programmes qui utilisent le port 80
2. OU modifiez le port dans `C:\xampp\apache\conf\httpd.conf`

### Page blanche ou erreur 404

**Solution** : Vérifiez que les fichiers sont bien dans XAMPP
```
C:\xampp\htdocs\max_mila_livre\
├── api.php
├── api_test.html
├── books.html
└── assets\img\
```

---

## 📁 Commandes Utiles

### Vérifier si Apache fonctionne
```powershell
Get-Process -Name "httpd" -ErrorAction SilentlyContinue
```

### Copier les nouvelles illustrations vers XAMPP
```powershell
Copy-Item "illustrations_kids\*" "C:\xampp\htdocs\max_mila_livre\assets\img\kids\" -Force
Copy-Item "illustrations_adult\*" "C:\xampp\htdocs\max_mila_livre\assets\img\adult\" -Force
```

### Générer de nouvelles illustrations
```powershell
.\.venv\Scripts\python.exe generate_realistic_api.py
```

---

## 🎯 Workflow Complet

1. **Démarrer le serveur**
   ```
   Double-clic sur start_server.bat
   ```

2. **Générer des illustrations** (si besoin)
   ```powershell
   .\.venv\Scripts\Activate.ps1
   python generate_realistic_api.py
   ```

3. **Copier vers XAMPP** (si nouvelles images)
   ```powershell
   Copy-Item "illustrations_*\*" "C:\xampp\htdocs\max_mila_livre\assets\img\*\" -Force -Recurse
   ```

4. **Accéder à l'interface**
   - Ouvrir http://localhost/max_mila_livre/api_test.html
   - Cliquer sur "Charger les statistiques"
   - Consulter la galerie d'images

5. **Arrêter le serveur** (quand vous avez terminé)
   ```
   Double-clic sur stop_server.bat
   ```

---

## 📋 Checklist de Vérification

Avant de commencer, vérifiez :

- [ ] XAMPP est installé dans `C:\xampp\`
- [ ] Python 3.14 avec environnement virtuel `.venv\`
- [ ] Bibliothèques Python installées (Pillow, reportlab)
- [ ] Fichiers copiés dans `C:\xampp\htdocs\max_mila_livre\`
- [ ] Port 80 disponible (aucun autre serveur web actif)

---

## 🆘 Support

Si vous rencontrez des problèmes :

1. **Vérifier les logs Apache** : `C:\xampp\apache\logs\error.log`
2. **Tester l'API directement** : http://localhost/max_mila_livre/api.php
3. **Redémarrer XAMPP** : `stop_server.bat` puis `start_server.bat`
4. **Vérifier les permissions** des dossiers dans `htdocs`

---

## 📝 Version

- **Version** : 1.0.0
- **Date** : 25 février 2026
- **Auteur** : Asmir MLN
