"""
Script professionnel pour améliorer les illustrations pour Amazon KDP
Qualité print : 300 DPI, 2560x2560 pixels minimum
"""

from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

# Configuration Amazon KDP
DPI = 300
SIZE_AMAZON = 2560  # Minimum recommandé pour Amazon KDP
OUTPUT_QUALITY = 100  # Qualité JPG maximale

class AmazonKDPEnhancer:
    """Améliore les images pour qualité professionnelle Amazon KDP"""
    
    def __init__(self, target_size=SIZE_AMAZON, dpi=DPI):
        self.target_size = target_size
        self.dpi = dpi
        
    def enhance_image(self, input_path, output_path, format='PNG'):
        """
        Améliore une image pour qualité professionnelle
        
        Args:
            input_path: Chemin image source
            output_path: Chemin image destination
            format: 'PNG' ou 'JPEG'
        """
        print(f"📸 Traitement: {os.path.basename(input_path)}")
        
        # Charger l'image
        img = Image.open(input_path)
        
        # 1. Redimensionnement haute qualité (LANCZOS = meilleur algorithme)
        if img.size[0] != self.target_size or img.size[1] != self.target_size:
            print(f"   ↗️  Redimensionnement {img.size} → {self.target_size}x{self.target_size}")
            img = img.resize((self.target_size, self.target_size), Image.LANCZOS)
        
        # 2. Conversion en RGB si nécessaire
        if img.mode != 'RGB':
            print(f"   🎨 Conversion {img.mode} → RGB")
            img = img.convert('RGB')
        
        # 3. Amélioration de la netteté (sharpness)
        print("   ✨ Amélioration netteté")
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)  # Augmente la netteté de 50%
        
        # 4. Amélioration des couleurs (saturation)
        print("   🌈 Amélioration couleurs")
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.2)  # Augmente la saturation de 20%
        
        # 5. Amélioration du contraste
        print("   ⚫⚪ Amélioration contraste")
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.1)  # Augmente le contraste de 10%
        
        # 6. Légère amélioration de la luminosité si sombre
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.05)  # Légère augmentation
        
        # 7. Filtre anti-aliasing léger
        print("   🔄 Anti-aliasing")
        img = img.filter(ImageFilter.SMOOTH)
        
        # 8. Sauvegarde avec paramètres optimaux
        print(f"   💾 Sauvegarde en {format}")
        if format.upper() == 'PNG':
            img.save(output_path, 'PNG', dpi=(self.dpi, self.dpi), optimize=True)
        else:
            img.save(output_path, 'JPEG', dpi=(self.dpi, self.dpi), 
                    quality=OUTPUT_QUALITY, optimize=True, subsampling=0)
        
        # Afficher taille fichier
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"   ✅ Terminé! Taille: {size_mb:.2f} MB\n")
        
        return img
    
    def batch_enhance(self, input_dir, output_dir, format='PNG'):
        """
        Traite tous les fichiers d'un dossier
        
        Args:
            input_dir: Dossier source
            output_dir: Dossier destination
            format: 'PNG' ou 'JPEG'
        """
        os.makedirs(output_dir, exist_ok=True)
        
        print("\n" + "="*60)
        print("   AMÉLIORATION QUALITÉ PROFESSIONNELLE AMAZON KDP")
        print("="*60)
        print(f"📁 Source: {input_dir}")
        print(f"📁 Destination: {output_dir}")
        print(f"📐 Résolution: {self.target_size}x{self.target_size} @ {self.dpi} DPI")
        print(f"📄 Format: {format}")
        print("="*60 + "\n")
        
        # Trouver toutes les images
        extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        files = [f for f in os.listdir(input_dir) 
                if os.path.splitext(f)[1].lower() in extensions]
        
        if not files:
            print("❌ Aucune image trouvée!")
            return
        
        print(f"🖼️  {len(files)} images trouvées\n")
        
        # Traiter chaque image
        total_size = 0
        for i, filename in enumerate(files, 1):
            input_path = os.path.join(input_dir, filename)
            
            # Changer extension si besoin
            name_without_ext = os.path.splitext(filename)[0]
            if format.upper() == 'PNG':
                output_filename = name_without_ext + '.png'
            else:
                output_filename = name_without_ext + '.jpg'
            
            output_path = os.path.join(output_dir, output_filename)
            
            print(f"[{i}/{len(files)}] {filename}")
            try:
                self.enhance_image(input_path, output_path, format)
                total_size += os.path.getsize(output_path)
            except Exception as e:
                print(f"   ❌ Erreur: {e}\n")
        
        # Résumé
        print("\n" + "="*60)
        print("   ✅ TRAITEMENT TERMINÉ")
        print("="*60)
        print(f"📊 {len(files)} images traitées")
        print(f"💾 Taille totale: {total_size / (1024*1024):.2f} MB")
        print(f"📁 Dossier: {output_dir}")
        print("="*60 + "\n")


def create_thumbnail(input_path, output_path, size=512):
    """Crée une miniature optimisée"""
    img = Image.open(input_path)
    img.thumbnail((size, size), Image.LANCZOS)
    img.save(output_path, 'PNG', optimize=True)
    print(f"✅ Miniature créée: {output_path}")


def verify_amazon_requirements(image_path):
    """Vérifie qu'une image respecte les exigences Amazon KDP"""
    img = Image.open(image_path)
    
    print(f"\n📋 Vérification: {os.path.basename(image_path)}")
    print("-" * 50)
    
    issues = []
    
    # Vérifier dimensions
    if img.size[0] < 2560 or img.size[1] < 2560:
        issues.append(f"❌ Dimensions trop petites: {img.size}")
    else:
        print(f"✅ Dimensions: {img.size[0]}x{img.size[1]} pixels")
    
    # Vérifier mode couleur
    if img.mode not in ['RGB', 'RGBA']:
        issues.append(f"❌ Mode couleur invalide: {img.mode}")
    else:
        print(f"✅ Mode couleur: {img.mode}")
    
    # Vérifier DPI (si disponible)
    if hasattr(img, 'info') and 'dpi' in img.info:
        dpi = img.info['dpi']
        if dpi[0] < 300 or dpi[1] < 300:
            issues.append(f"⚠️  DPI faible: {dpi}")
        else:
            print(f"✅ DPI: {dpi[0]}x{dpi[1]}")
    else:
        print("⚠️  DPI non défini dans les métadonnées")
    
    # Vérifier taille fichier
    size_mb = os.path.getsize(image_path) / (1024 * 1024)
    if size_mb > 50:
        issues.append(f"⚠️  Fichier volumineux: {size_mb:.2f} MB")
    else:
        print(f"✅ Taille fichier: {size_mb:.2f} MB")
    
    print("-" * 50)
    
    if issues:
        print("\n⚠️  Problèmes détectés:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✅ Image conforme aux exigences Amazon KDP!")
    
    return len(issues) == 0


# ========== EXEMPLES D'UTILISATION ==========

if __name__ == '__main__':
    enhancer = AmazonKDPEnhancer(target_size=2560, dpi=300)
    
    # Menu interactif
    print("\n" + "="*60)
    print("   🎨 AMÉLIORATION QUALITÉ PROFESSIONNELLE")
    print("   Pour Amazon KDP")
    print("="*60)
    print("\nOptions:")
    print("  1. Améliorer images ENFANTS (illustrations_kids/)")
    print("  2. Améliorer images ADULTES (illustrations_adult/)")
    print("  3. Améliorer les DEUX versions")
    print("  4. Vérifier une image spécifique")
    print("  5. Créer miniatures")
    print("="*60)
    
    choice = input("\nVotre choix (1-5): ").strip()
    
    if choice == '1':
        enhancer.batch_enhance(
            'illustrations_kids',
            'illustrations_kids_amazon',
            format='PNG'
        )
    
    elif choice == '2':
        enhancer.batch_enhance(
            'illustrations_adult',
            'illustrations_adult_amazon',
            format='PNG'
        )
    
    elif choice == '3':
        print("\n📚 Version ENFANTS:")
        enhancer.batch_enhance(
            'illustrations_kids',
            'illustrations_kids_amazon',
            format='PNG'
        )
        
        print("\n📖 Version ADULTES:")
        enhancer.batch_enhance(
            'illustrations_adult',
            'illustrations_adult_amazon',
            format='PNG'
        )
    
    elif choice == '4':
        image_path = input("\nChemin de l'image: ").strip('"')
        if os.path.exists(image_path):
            verify_amazon_requirements(image_path)
        else:
            print("❌ Fichier introuvable!")
    
    elif choice == '5':
        input_dir = input("\nDossier source: ").strip('"')
        output_dir = input("Dossier miniatures: ").strip('"')
        
        if os.path.exists(input_dir):
            os.makedirs(output_dir, exist_ok=True)
            for file in os.listdir(input_dir):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    create_thumbnail(
                        os.path.join(input_dir, file),
                        os.path.join(output_dir, 'thumb_' + file)
                    )
        else:
            print("❌ Dossier introuvable!")
    
    else:
        print("❌ Choix invalide!")
    
    print("\n✅ Terminé!")
    input("\nAppuyez sur Entrée pour quitter...")
