"""
Script de création des PDFs finaux avec les vraies illustrations
"""

from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Paragraph, PageBreak, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import os

SIZE_PX = 2362
DPI = 300

# =========================
# GÉNÉRATION DES PDFs
# =========================

def generate_pdf_kids():
    """Génère le PDF version enfants (BD)"""
    print("\n" + "="*70)
    print("📚 GÉNÉRATION PDF - VERSION ENFANTS (BD)")
    print("="*70 + "\n")
    
    pdf_file = "output/Max_Mila_Kids_BD.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.3*cm, bottomMargin=0.3*cm)
    elements = []
    
    # Couverture
    cover = os.path.join('illustrations_kids', 'cover.png')
    if os.path.exists(cover):
        elements.append(RLImage(cover, width=18.5*cm, height=18.5*cm))
        elements.append(PageBreak())
        print("✓ Couverture ajoutée")
    
    # Pages de contenu
    for i in range(1, 13):
        page_file = os.path.join('illustrations_kids', f'page_{i:02d}.png')
        if os.path.exists(page_file):
            elements.append(RLImage(page_file, width=18.5*cm, height=18.5*cm))
            elements.append(PageBreak())
            print(f"✓ Page {i} ajoutée")
        else:
            print(f"⚠️  Page {i} non trouvée")
    
    # 4e de couverture
    back_cover = os.path.join('illustrations_kids', 'back_cover.png')
    if os.path.exists(back_cover):
        elements.append(RLImage(back_cover, width=18.5*cm, height=18.5*cm))
        elements.append(PageBreak())
        print("✓ 4e de couverture ajoutée")
    
    # Construire le PDF
    try:
        doc.build(elements)
        size_mb = os.path.getsize(pdf_file) / (1024*1024)
        print(f"\n✅ PDF créé: {pdf_file} ({size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        return False

def generate_pdf_adult():
    """Génère le PDF version adulte (réaliste)"""
    print("\n" + "="*70)
    print("📚 GÉNÉRATION PDF - VERSION ADULTE (RÉALISTE)")
    print("="*70 + "\n")
    
    pdf_file = "output/Max_Mila_Adult_Edition.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.3*cm, bottomMargin=0.3*cm)
    elements = []
    
    # Couverture
    cover = os.path.join('illustrations_adult', 'cover.png')
    if os.path.exists(cover):
        elements.append(RLImage(cover, width=18.5*cm, height=18.5*cm))
        elements.append(PageBreak())
        print("✓ Couverture ajoutée")
    
    # Pages de contenu
    for i in range(1, 13):
        page_file = os.path.join('illustrations_adult', f'page_{i:02d}.png')
        if os.path.exists(page_file):
            elements.append(RLImage(page_file, width=18.5*cm, height=18.5*cm))
            elements.append(PageBreak())
            print(f"✓ Page {i} ajoutée")
        else:
            print(f"⚠️  Page {i} non trouvée")
    
    # 4e de couverture
    back_cover = os.path.join('illustrations_adult', 'back_cover.png')
    if os.path.exists(back_cover):
        elements.append(RLImage(back_cover, width=18.5*cm, height=18.5*cm))
        elements.append(PageBreak())
        print("✓ 4e de couverture ajoutée")
    
    # Construire le PDF
    try:
        doc.build(elements)
        size_mb = os.path.getsize(pdf_file) / (1024*1024)
        print(f"\n✅ PDF créé: {pdf_file} ({size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        return False

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    os.makedirs('output', exist_ok=True)
    
    print("\n" + "="*70)
    print("🎨 GÉNÉRATION DES PDFs AVEC ILLUSTRATIONS COMPLÈTES")
    print("="*70)
    
    success1 = generate_pdf_kids()
    success2 = generate_pdf_adult()
    
    print("\n" + "="*70)
    if success1 and success2:
        print("✅ TOUS LES PDFs ONT ÉTÉ GÉNÉRÉS AVEC SUCCÈS!")
        print("="*70)
        print("\n📖 Fichiers générés:")
        print("  • output/Max_Mila_Kids_BD.pdf (Version enfants, BD colorée)")
        print("  • output/Max_Mila_Adult_Edition.pdf (Version adulte, réaliste)")
        print("\n📚 Chaque livre contient:")
        print("  - Couverture")
        print("  - 12 pages illustrées")
        print("  - 4e de couverture avec résumé")
    else:
        print("❌ Erreur lors de la génération")
        print("="*70)
