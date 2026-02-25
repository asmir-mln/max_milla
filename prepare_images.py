"""
Script de préparation et d'optimisation des images
Convertit les images brutes en différents formats pour web et impression
"""

from PIL import Image
import os
from pathlib import Path
import json

class ImagePreparation:
    """Classe pour préparer et optimiser les images"""
    
    def __init__(self, source_dir="images_raw", output_base="output_images"):
        self.source_dir = source_dir
        self.output_base = output_base
        self.metadata = {}
        
        # Créer les dossiers de sortie
        self.dirs = {
            'original': f"{output_base}/original",
            'web': f"{output_base}/web",
            'print': f"{output_base}/print",
            'thumbnail': f"{output_base}/thumbnail",
            'compressed': f"{output_base}/compressed"
        }
        
        for dir_path in self.dirs.values():
            os.makedirs(dir_path, exist_ok=True)
    
    def get_images(self):
        """Récupère la liste des images"""
        source_path = Path(self.source_dir)
        images = sorted(source_path.glob("*.png"))
        return images
    
    def process_image(self, image_path):
        """Traite une image et crée différentes versions"""
        filename = image_path.name
        print(f"\n📸 Traitement de {filename}...")
        
        try:
            img = Image.open(image_path)
            original_size = img.size
            original_mode = img.mode
            
            # Stockage des métadonnées
            self.metadata[filename] = {
                'original_size': original_size,
                'original_mode': original_mode,
                'original_size_kb': os.path.getsize(image_path) / 1024
            }
            
            # 1. Copier l'original
            self._copy_original(image_path, filename)
            
            # 2. Créer version web (optimisée pour le web)
            self._create_web_version(img, filename)
            
            # 3. Créer version impression (haute qualité)
            self._create_print_version(img, filename)
            
            # 4. Créer thumbnail
            self._create_thumbnail(img, filename)
            
            # 5. Créer version compressée
            self._create_compressed(img, filename)
            
            print(f"✓ {filename} traité avec succès")
            return True
            
        except Exception as e:
            print(f"✗ Erreur lors du traitement de {filename}: {e}")
            return False
    
    def _copy_original(self, source, filename):
        """Copie l'image originale"""
        dest = f"{self.dirs['original']}/{filename}"
        Image.open(source).save(dest, quality=95)
        size_kb = os.path.getsize(dest) / 1024
        print(f"  └─ Original: {size_kb:.1f} KB")
    
    def _create_web_version(self, img, filename):
        """Crée une version optimisée pour le web (1200px, JPEG)"""
        # Calculer nouvelles dimensions en gardant les proportions
        max_size = 1200
        ratio = max_size / max(img.size)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        
        # Redimensionner et convertir en RGB si nécessaire
        web_img = img.resize(new_size, Image.Resampling.LANCZOS)
        if web_img.mode == 'RGBA':
            # Créer fond blanc
            background = Image.new('RGB', new_size, (255, 255, 255))
            background.paste(web_img, mask=web_img.split()[3] if len(web_img.split()) > 3 else None)
            web_img = background
        elif web_img.mode != 'RGB':
            web_img = web_img.convert('RGB')
        
        dest = f"{self.dirs['web']}/{Path(filename).stem}.jpg"
        web_img.save(dest, quality=85, optimize=True)
        size_kb = os.path.getsize(dest) / 1024
        print(f"  └─ Web: {new_size} @ {size_kb:.1f} KB")
        self.metadata[filename]['web_size'] = new_size
    
    def _create_print_version(self, img, filename):
        """Crée une version haute qualité pour l'impression"""
        # Garder la taille originale ou ajouter compression minime
        print_img = img.convert('RGB') if img.mode != 'RGB' else img
        
        dest = f"{self.dirs['print']}/{filename}"
        print_img.save(dest, quality=95)
        size_kb = os.path.getsize(dest) / 1024
        print(f"  └─ Print: {img.size} @ {size_kb:.1f} KB")
    
    def _create_thumbnail(self, img, filename):
        """Crée une vignette (300px)"""
        thumbnail_size = (300, 300)
        thumb = img.copy()
        thumb.thumbnail(thumbnail_size, Image.Resampling.LANCZOS)
        
        # Créer une image carrée avec fond blanc
        square = Image.new('RGB', thumbnail_size, (255, 255, 255))
        pos = ((thumbnail_size[0] - thumb.width) // 2, 
               (thumbnail_size[1] - thumb.height) // 2)
        if thumb.mode == 'RGBA':
            background = Image.new('RGB', thumbnail_size, (255, 255, 255))
            background.paste(thumb, pos, mask=thumb.split()[3])
            square = background
        else:
            thumb_rgb = thumb.convert('RGB') if thumb.mode != 'RGB' else thumb
            square.paste(thumb_rgb, pos)
        
        dest = f"{self.dirs['thumbnail']}/{Path(filename).stem}_thumb.jpg"
        square.save(dest, quality=85, optimize=True)
        size_kb = os.path.getsize(dest) / 1024
        print(f"  └─ Thumbnail: {thumbnail_size} @ {size_kb:.1f} KB")
    
    def _create_compressed(self, img, filename):
        """Crée une version très compressée (pour réseaux lents)"""
        # Réduire à 600px
        compressed_img = img.copy()
        max_size = 600
        ratio = max_size / max(compressed_img.size)
        new_size = (int(compressed_img.width * ratio), 
                   int(compressed_img.height * ratio))
        compressed_img = compressed_img.resize(new_size, Image.Resampling.LANCZOS)
        
        if compressed_img.mode == 'RGBA':
            background = Image.new('RGB', new_size, (255, 255, 255))
            background.paste(compressed_img, 
                            mask=compressed_img.split()[3] if len(compressed_img.split()) > 3 else None)
            compressed_img = background
        elif compressed_img.mode != 'RGB':
            compressed_img = compressed_img.convert('RGB')
        
        dest = f"{self.dirs['compressed']}/{Path(filename).stem}_compressed.jpg"
        compressed_img.save(dest, quality=70, optimize=True)
        size_kb = os.path.getsize(dest) / 1024
        print(f"  └─ Compressed: {new_size} @ {size_kb:.1f} KB")
    
    def generate_metadata(self):
        """Génère un fichier JSON avec les métadonnées"""
        metadata_file = f"{self.output_base}/metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Métadonnées sauvegardées: {metadata_file}")
    
    def generate_html_gallery(self):
        """Génère une galerie HTML pour prévisualiser les images"""
        html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie - Max et Mila</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; background: #f5f5f5; padding: 20px; }
        h1 { text-align: center; margin-bottom: 30px; color: #333; }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .item {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .item:hover { transform: translateY(-5px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
        .item img { width: 100%; height: auto; display: block; }
        .item-info { padding: 15px; }
        .item-info h3 { margin-bottom: 5px; color: #333; }
        .item-info p { font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <h1>📚 Galerie du Livre - Max et Mila et le Perroquet Mystérieux</h1>
    <div class="gallery">
"""
        
        # Ajouter les images
        thumbnail_dir = Path(self.dirs['thumbnail'])
        thumbnails = sorted(thumbnail_dir.glob("*_thumb.jpg"))
        
        for thumb in thumbnails:
            name = thumb.stem.replace('_thumb', '')
            html += f"""        <div class="item">
            <img src="{thumb.relative_to(self.output_base)}" alt="{name}">
            <div class="item-info">
                <h3>{name}</h3>
                <p>Cliquez pour voir en plein écran</p>
            </div>
        </div>
"""
        
        html += """    </div>
</body>
</html>
"""
        
        gallery_file = f"{self.output_base}/gallery.html"
        with open(gallery_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Galerie HTML créée: {gallery_file}")
    
    def run(self):
        """Lance le traitement complet"""
        print("=" * 70)
        print("🖼️  PRÉPARATION ET OPTIMISATION DES IMAGES")
        print("=" * 70)
        
        images = self.get_images()
        
        if not images:
            print(f"✗ Aucune image trouvée dans {self.source_dir}")
            return False
        
        print(f"\n📂 Dossier source: {self.source_dir}")
        print(f"📁 Dossier de sortie: {self.output_base}")
        print(f"🖼️  Nombre d'images: {len(images)}\n")
        
        # Traiter chaque image
        success_count = 0
        for image_path in images:
            if self.process_image(image_path):
                success_count += 1
        
        print(f"\n{'=' * 70}")
        print(f"✓ {success_count}/{len(images)} images traitées avec succès")
        print(f"{'=' * 70}\n")
        
        # Générer métadonnées et galerie
        self.generate_metadata()
        self.generate_html_gallery()
        
        # Afficher le résumé
        print("\n📊 RÉSUMÉ DES DOSSIERS DE SORTIE:")
        for name, path in self.dirs.items():
            if os.path.exists(path):
                files = len(os.listdir(path))
                print(f"  • {name:15} → {files} fichier(s)")
        
        return True


def main():
    """Fonction principale"""
    preparation = ImagePreparation(
        source_dir="images_raw",
        output_base="output_images"
    )
    
    success = preparation.run()
    
    if success:
        print("\n✅ Processus complété avec succès!")
        print("Consultez output_images/gallery.html pour voir les images")
    else:
        print("\n❌ Erreur lors du traitement")


if __name__ == "__main__":
    main()
