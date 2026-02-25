"""
Script principal pour générer le livre Format 3
"""

import sys
import os

# Ajouter le répertoire parent au chemin pour pouvoir importer les modules
sys.path.insert(0, os.path.dirname(__file__))

from src.page_generator import generate_all_pages
from src.pdf_creator import create_pdf, get_pdf_info
import config

# Histoire du livre (12 pages)
STORY = [
    "Max regardait l'horizon en rêvant d'aventure.",
    "Un perroquet coloré descendit du ciel et cria.",
    "\"Mon trésor ! Mon trésor !\" répétait-il.",
    "Ils découvrirent une île mystérieuse pleine de secrets.",
    "Au loin, un vieux navire pirate apparaissait.",
    "Le doute envahit Max face à l'inconnu.",
    "Mila lui rappela sa force intérieure.",
    "Un coffre ancien brillait sous le soleil.",
    "L'ombre du danger planait autour d'eux.",
    "Max trouva enfin le courage d'avancer.",
    "Le trésor n'était pas fait d'or ni de bijoux.",
    "Le vrai trésor était le courage qui grandissait en lui."
]

def main():
    """Fonction principale"""
    print("=" * 60)
    print("GÉNÉRATEUR DE LIVRE - FORMAT 3")
    print("=" * 60)
    
    # Créer le répertoire de sortie
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    
    # Générer toutes les pages
    print("\nGénération des pages...")
    try:
        page_files = generate_all_pages(STORY, output_dir=config.OUTPUT_DIR)
        print(f"✓ {len(page_files)} pages générées.")
    except Exception as e:
        print(f"✗ Erreur lors de la génération des pages: {e}")
        return False
    
    # Créer le PDF
    print("\nCréation du PDF...")
    try:
        create_pdf(page_files, output_filename=config.PDF_OUTPUT)
        print("✓ PDF créé avec succès.")
    except Exception as e:
        print(f"✗ Erreur lors de la création du PDF: {e}")
        return False
    
    # Afficher les informations du fichier
    print("\n" + "=" * 60)
    if get_pdf_info(config.PDF_OUTPUT):
        print("=" * 60)
        print("✓ Processus complété avec succès!")
        return True
    else:
        print("✗ Le fichier PDF n'a pas pu être créé.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
