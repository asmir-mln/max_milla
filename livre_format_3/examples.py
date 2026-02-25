"""
Exemples d'utilisation avancée du module Livre Format 3
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.page_generator import (
    generate_page, save_page, add_title, create_blank_page,
    add_illustration, add_decorative_line, add_footer
)
from src.pdf_creator import create_pdf

def example_custom_page():
    """Exemple: Créer une page personnalisée"""
    page = create_blank_page()
    
    # Ajouter des éléments personnalisés
    add_title(page, "Page Personnalisée", y_position=100)
    add_decorative_line(page, y_position=200)
    add_footer(page, "Custom Page - Asmir MLN")
    
    save_page(page, "output/custom_page.png")
    print("Page personnalisée créée: output/custom_page.png")

def example_different_styles():
    """Exemple: Plusieurs styles de pages"""
    styles = [
        {"title": "Style 1: Classique", "color": "#ffffff"},
        {"title": "Style 2: Beige", "color": "#f5e6c8"},
        {"title": "Style 3: Crème", "color": "#fffdd0"},
    ]
    
    for i, style in enumerate(styles, 1):
        page = create_blank_page(color=style["color"])
        add_title(page, style["title"], y_position=300)
        save_page(page, f"output/style_{i}.png")
    
    print(f"{len(styles)} styles créés")

def example_batch_generation():
    """Exemple: Générer un lot de 24 pages (deux tomes)"""
    story_tome_1 = [f"Page {i} - Tome 1" for i in range(1, 13)]
    story_tome_2 = [f"Page {i} - Tome 2" for i in range(13, 25)]
    
    from src.page_generator import generate_all_pages
    
    pages_tome_1 = generate_all_pages(story_tome_1, "output/tome_1")
    pages_tome_2 = generate_all_pages(story_tome_2, "output/tome_2")
    
    create_pdf(pages_tome_1, "output/Tome_1.pdf")
    create_pdf(pages_tome_2, "output/Tome_2.pdf")
    
    print("Deux tomes créés avec succès!")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    
    print("EXEMPLES D'UTILISATION AVANCÉE")
    print("=" * 50)
    
    # Décommenter pour exécuter les exemples
    # example_custom_page()
    # example_different_styles()
    # example_batch_generation()
    
    print("\nDécommentez les exemples dans ce fichier pour les exécuter.")
