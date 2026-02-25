"""
Générateur de PDF du Livre - Max et Mila et le Perroquet Mystérieux
Crée un PDF professionnel avec couverture, texte et images alternées
"""

from reportlab.platypus import (
    SimpleDocTemplate, Image as RLImage, Paragraph, Spacer, 
    PageBreak, Table, TableStyle
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
import os
import sys

# =========================
# CONFIGURATION
# =========================

BOOK_SIZE = 20 * cm
PDF_PATH = "output/Max_Mila_Livre_Final.pdf"
IMAGES_DIR = "images_final"
LOGO_PATH = "logo.png"

# Vérifier que le dossier d'images existe
if not os.path.exists(IMAGES_DIR):
    print(f"❌ Erreur: Le dossier '{IMAGES_DIR}' n'existe pas")
    sys.exit(1)

# Créer le dossier de sortie
os.makedirs("output", exist_ok=True)

# =========================
# HISTOIRE COMPLÈTE (12 pages)
# =========================

STORY_TEXTS = [
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

# =========================
# STYLES
# =========================

# Style pour l'histoire
story_style = ParagraphStyle(
    name='Story',
    fontSize=16,
    leading=22,
    textColor=colors.black,
    alignment=0,  # Alignement à gauche
    spaceAfter=12,
    fontName='Helvetica'
)

# Style pour le titre
title_style = ParagraphStyle(
    name='Title',
    fontSize=24,
    leading=28,
    textColor=colors.HexColor('#333333'),
    alignment=1,  # Centré
    spaceAfter=12,
    fontName='Helvetica-Bold'
)

# Style pour le pied de page
footer_style = ParagraphStyle(
    name='Footer',
    fontSize=12,
    leading=14,
    textColor=colors.HexColor('#666666'),
    alignment=1,  # Centré
    fontName='Helvetica-Oblique'
)

# =========================
# DOCUMENT PDF
# =========================

def create_pdf():
    """Crée et génère le PDF du livre"""
    
    print("=" * 70)
    print("📚 GÉNÉRATION DU PDF - MAX ET MILA")
    print("=" * 70)
    
    # Créer le document
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=(BOOK_SIZE, BOOK_SIZE),
        topMargin=0.3*cm,
        bottomMargin=0.3*cm,
        leftMargin=0.3*cm,
        rightMargin=0.3*cm
    )
    
    elements = []
    
    print(f"\n📄 Format du livre: {BOOK_SIZE/cm:.0f}cm × {BOOK_SIZE/cm:.0f}cm")
    print(f"📁 Dossier d'images: {IMAGES_DIR}/")
    print(f"💾 Fichier de sortie: {PDF_PATH}\n")
    
    # =========================
    # 1. COUVERTURE
    # =========================
    
    print("1️⃣  Ajout de la couverture...")
    cover_path = os.path.join(IMAGES_DIR, "cover.png")
    
    if os.path.exists(cover_path):
        elements.append(RLImage(cover_path, width=18.5*cm, height=18.5*cm))
        elements.append(PageBreak())
        print("   ✓ Couverture ajoutée")
    else:
        print(f"   ⚠️  Couverture non trouvée: {cover_path}")
    
    # =========================
    # 2. PAGES INTÉRIEURES
    # =========================
    
    print(f"\n2️⃣  Ajout des {len(STORY_TEXTS)} pages de contenu...\n")
    
    for i, story_text in enumerate(STORY_TEXTS, 1):
        
        # Page de TEXTE
        try:
            # Ajouter le texte
            elements.append(Spacer(1, 5*cm))
            elements.append(Paragraph(story_text, story_style))
            elements.append(Spacer(1, 8*cm))
            
            # Ajouter le numéro de page
            page_num = Paragraph(f"— Page {i} —", footer_style)
            elements.append(page_num)
            elements.append(PageBreak())
            
        except Exception as e:
            print(f"   ⚠️  Erreur à la page {i}: {e}")
        
        # Page d'IMAGE
        try:
            image_path = os.path.join(IMAGES_DIR, f"page{i:02d}.png")
            
            if os.path.exists(image_path):
                elements.append(RLImage(image_path, width=18.5*cm, height=18.5*cm))
                elements.append(PageBreak())
                print(f"   ✓ Page {i}: texte + image")
            else:
                print(f"   ⚠️  Image non trouvée: {image_path}")
                
        except Exception as e:
            print(f"   ⚠️  Erreur avec l'image page {i}: {e}")
    
    # =========================
    # 3. 4E DE COUVERTURE (Fin)
    # =========================
    
    print(f"\n3️⃣  Ajout de la 4e de couverture...")
    
    try:
        elements.append(Spacer(1, 6*cm))
        elements.append(Paragraph("Une aventure inoubliable", title_style))
        elements.append(Spacer(1, 1*cm))
        elements.append(Paragraph(
            "Découvrez l'histoire magique de Max et Mila à la recherche du trésor mystérieux.",
            story_style
        ))
        elements.append(Spacer(1, 2*cm))
        elements.append(Paragraph("Par Asmir MLN", footer_style))
        elements.append(Spacer(1, 1*cm))
        elements.append(Paragraph("Février 2026", footer_style))
        
        print("   ✓ 4e de couverture ajoutée")
        
    except Exception as e:
        print(f"   ⚠️  Erreur lors de la création de la 4e de couverture: {e}")
    
    # =========================
    # 4. CONSTRUCTION DU PDF
    # =========================
    
    print(f"\n4️⃣  Construction du PDF...")
    
    try:
        doc.build(elements)
        
        # Vérifier le fichier résultant
        if os.path.exists(PDF_PATH):
            file_size = os.path.getsize(PDF_PATH) / (1024 * 1024)
            print(f"   ✓ PDF créé avec succès")
            print(f"   📊 Taille du fichier: {file_size:.2f} MB")
            
            return True
        else:
            print(f"   ❌ Le fichier PDF n'a pas pu être créé")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur lors de la construction du PDF: {e}")
        return False


def main():
    """Fonction principale"""
    
    # Vérifier la disponibilité des images
    if not os.path.exists(IMAGES_DIR):
        print(f"❌ Erreur: Le dossier '{IMAGES_DIR}' n'existe pas")
        print(f"   Exécutez d'abord: python optimize_for_print.py")
        return False
    
    # Créer le PDF
    success = create_pdf()
    
    print("\n" + "=" * 70)
    
    if success:
        print("✅ Livre généré avec succès!")
        print(f"📖 Fichier: {os.path.abspath(PDF_PATH)}")
        print("=" * 70)
        return True
    else:
        print("❌ Erreur lors de la génération du livre")
        print("=" * 70)
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
