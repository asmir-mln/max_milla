"""
Script de redimensionnement et optimisation pour impression
Convertit les images au format final 300 DPI pour impression professionnelle
"""

from PIL import Image
import os
import sys

# Configuration
RAW_FOLDER = "images_raw"
FINAL_FOLDER = "images_final"

# Dimensions : 20cm à 300 DPI = 2362 pixels
SIZE = 2362
DPI = 300

def main():
    """Fonction principale"""
    print("=" * 70)
    print("🖨️  OPTIMISATION POUR IMPRESSION (300 DPI)")
    print("=" * 70)
    print(f"\nFormat de sortie: {SIZE}x{SIZE} pixels @ {DPI} DPI")
    print(f"Dimensions: 20cm x 20cm\n")
    
    # Vérifier que le dossier source existe
    if not os.path.exists(RAW_FOLDER):
        print(f"❌ Erreur: Le dossier '{RAW_FOLDER}' n'existe pas")
        return False
    
    # Créer le dossier de sortie
    os.makedirs(FINAL_FOLDER, exist_ok=True)
    print(f"📂 Dossier de sortie: {FINAL_FOLDER}/\n")
    
    # Récupérer les fichiers PNG
    png_files = [f for f in os.listdir(RAW_FOLDER) if f.lower().endswith(".png")]
    
    if not png_files:
        print(f"⚠️  Aucun fichier PNG trouvé dans '{RAW_FOLDER}'")
        return False
    
    print(f"🖼️  Nombre de fichiers à traiter: {len(png_files)}\n")
    print("Traitement en cours...")
    print("-" * 70)
    
    success_count = 0
    error_count = 0
    
    for i, file in enumerate(sorted(png_files), 1):
        try:
            # Chemins complets
            input_path = os.path.join(RAW_FOLDER, file)
            output_path = os.path.join(FINAL_FOLDER, file)
            
            # Ouvrir l'image
            img = Image.open(input_path)
            original_size = img.size
            
            # Redimensionner à 2362x2362
            img_resized = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
            
            # Sauvegarder avec métadonnées DPI
            img_resized.save(output_path, dpi=(DPI, DPI), quality=95)
            
            file_size = os.path.getsize(output_path) / 1024  # en KB
            
            print(f"✓ [{i:2d}] {file:20} | {original_size} → {SIZE}x{SIZE} | {file_size:7.1f} KB")
            success_count += 1
            
        except Exception as e:
            print(f"✗ [{i:2d}] {file:20} | ❌ Erreur: {str(e)}")
            error_count += 1
    
    print("-" * 70)
    print(f"\n📊 RÉSUMÉ:")
    print(f"  ✓ Succès: {success_count}/{len(png_files)}")
    if error_count > 0:
        print(f"  ✗ Erreurs: {error_count}/{len(png_files)}")
    
    # Vérifier les fichiers de sortie
    output_files = os.listdir(FINAL_FOLDER)
    print(f"  📁 Fichiers générés: {len(output_files)}")
    
    # Calculer la taille totale
    total_size = sum(os.path.getsize(os.path.join(FINAL_FOLDER, f)) for f in output_files) / (1024 * 1024)
    print(f"  💾 Taille totale: {total_size:.2f} MB")
    
    print("\n" + "=" * 70)
    
    if success_count == len(png_files):
        print("✅ Toutes les images sont prêtes pour l'impression!")
        print("=" * 70)
        return True
    else:
        print("⚠️  Certaines images n'ont pas pu être traitées")
        print("=" * 70)
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
