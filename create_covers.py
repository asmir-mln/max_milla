"""
Script de création des couvertures et 4e de couvertures
"""

from PIL import Image, ImageDraw, ImageFont
import os

SIZE_PX = 2362
DPI = 300

def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def create_kids_cover():
    """Crée la couverture enfants (BD colorée)"""
    print("🎨 Création de la couverture ENFANTS...")
    
    img = Image.new('RGB', (SIZE_PX, SIZE_PX), '#87CEEB')
    draw = ImageDraw.Draw(img)
    
    # Fond dégradé simple (ciel bleu avec nuages)
    for y in range(SIZE_PX):
        ratio = y / SIZE_PX
        r = int(135 - (135-100) * ratio)
        g = int(206 - (206-150) * ratio)
        b = 235
    
    # Ajouter des formes amusantes
    # Soleil
    draw.ellipse([1800, 200, 2100, 500], fill='#FFD700', outline='#FFA500', width=10)
    
    # Nuages
    draw.ellipse([200, 300, 500, 500], fill='white', outline='lightblue', width=5)
    draw.ellipse([350, 250, 650, 450], fill='white', outline='lightblue', width=5)
    
    # Titre principal
    font_title = get_font(280)
    draw.text((SIZE_PX//2, 700), 'MAX et MILA', fill='#FF1493', font=font_title, anchor='mm', 
             stroke_width=8, stroke_fill='white')
    
    # Sous-titre
    font_sub = get_font(140)
    draw.text((SIZE_PX//2, 1200), 'et le', fill='#333333', font=font_sub, anchor='mm')
    
    # Titre du perroquet
    font_big = get_font(160)
    draw.text((SIZE_PX//2, 1550), 'PERROQUET MYSTÉRIEUX', fill='#FFD700', font=font_big, anchor='mm',
             stroke_width=6, stroke_fill='#FF6347')
    
    # Décoration: ligne dorée
    draw.rectangle([SIZE_PX//4, 1750, 3*SIZE_PX//4, 1800], fill='#FFD700')
    
    # Information du public
    font_info = get_font(100)
    draw.text((SIZE_PX//2, 2050), '📚 Pour enfants 4-10 ans', fill='#333333', font=font_info, anchor='mm')
    
    # Auteur
    font_author = get_font(80)
    draw.text((SIZE_PX - 300, SIZE_PX - 150), 'Asmir MLN', fill='#666666', font=font_author, anchor='rm')
    
    os.makedirs('illustrations_kids', exist_ok=True)
    img.save('illustrations_kids/cover.png', dpi=(DPI, DPI))
    print("✓ Couverture enfants créée: illustrations_kids/cover.png")

def create_kids_back_cover():
    """Crée la 4e de couverture enfants avec résumé"""
    print("📖 Création de la 4e de couverture ENFANTS...")
    
    img = Image.new('RGB', (SIZE_PX, SIZE_PX), '#F0F8FF')
    draw = ImageDraw.Draw(img)
    
    # Bande de couleur en haut
    draw.rectangle([0, 0, SIZE_PX, 400], fill='#FF1493')
    
    # Titre "À propos du livre"
    font_title = get_font(140)
    draw.text((SIZE_PX//2, 200), '📚 À propos', fill='white', font=font_title, anchor='mm')
    
    # Résumé
    resume = """Max et Mila rêvent d'aventure. Un jour, 
un mystérieux perroquet les entraîne 
vers une île secrète remplie de trésors.

Entre pirates, dangers et découvertes, 
nos deux héros vont apprendre une 
belle leçon : le vrai trésor n'est pas 
l'or ou les bijoux...

Le vrai trésor, c'est le COURAGE 
qui vit en chacun de nous!"""
    
    font_resume = get_font(90)
    draw.text((SIZE_PX//2, 1200), resume, fill='#333333', font=font_resume, anchor='mm', 
             align='center', spacing=50)
    
    # Bande de couleur en bas
    draw.rectangle([0, SIZE_PX - 400, SIZE_PX, SIZE_PX], fill='#FFD700')
    
    # Citation inspirante
    font_quote = get_font(100)
    draw.text((SIZE_PX//2, SIZE_PX - 200), '"Crois en toi!"', fill='#333333', 
             font=font_quote, anchor='mm', weight='bold')
    
    os.makedirs('illustrations_kids', exist_ok=True)
    img.save('illustrations_kids/back_cover.png', dpi=(DPI, DPI))
    print("✓ 4e de couverture enfants créée: illustrations_kids/back_cover.png")

def create_adult_cover():
    """Crée la couverture adulte (élégante et réaliste)"""
    print("🎨 Création de la couverture ADULTE...")
    
    img = Image.new('RGB', (SIZE_PX, SIZE_PX), '#F5F5DC')
    draw = ImageDraw.Draw(img)
    
    # Fond élégant
    for y in range(SIZE_PX):
        ratio = y / SIZE_PX
        r = int(245 - (245-210) * ratio)
        g = int(245 - (245-180) * ratio)
        b = int(220 - (220-140) * ratio)
        # Optionnel: appliquer le dégradé (simplifié ici)
    
    # Titre principal
    font_title = get_font(260)
    draw.text((SIZE_PX//2, 700), 'MAX et MILA', fill='#2C3E50', font=font_title, anchor='mm',
             stroke_width=5, stroke_fill='#DAA520')
    
    # Sous-titre poétique
    font_subtitle = get_font(120)
    draw.text((SIZE_PX//2, 1150), 'et le Perroquet Mystérieux', fill='#555555', font=font_subtitle, anchor='mm')
    
    # Accroche
    font_tagline = get_font(100)
    draw.text((SIZE_PX//2, 1600), 'Une quête initiatique de courage et d\'amitié', 
             fill='#777777', font=font_tagline, anchor='mm', style='italic')
    
    # Ligne de séparation dorée
    draw.rectangle([SIZE_PX//4, 1850, 3*SIZE_PX//4, 1900], fill='#DAA520')
    
    # Information
    font_info = get_font(90)
    draw.text((SIZE_PX//2, 2100), 'Édition Complète - Illustrée', fill='#555555', font=font_info, anchor='mm')
    
    # Auteur et date
    font_author = get_font(80)
    draw.text((SIZE_PX//2, SIZE_PX - 200), 'Asmir MLN • 2026', fill='#707070', font=font_author, anchor='mm')
    
    os.makedirs('illustrations_adult', exist_ok=True)
    img.save('illustrations_adult/cover.png', dpi=(DPI, DPI))
    print("✓ Couverture adulte créée: illustrations_adult/cover.png")

def create_adult_back_cover():
    """Crée la 4e de couverture adulte avec résumé"""
    print("📖 Création de la 4e de couverture ADULTE...")
    
    img = Image.new('RGB', (SIZE_PX, SIZE_PX), '#FFFAF0')
    draw = ImageDraw.Draw(img)
    
    # Bande élégante en haut
    draw.rectangle([0, 0, SIZE_PX, 350], fill='#2C3E50')
    
    font_title = get_font(130)
    draw.text((SIZE_PX//2, 175), 'Critique', fill='#DAA520', font=font_title, anchor='mm')
    
    # Résumé littéraire
    resume = """Dans cette aventure poétique et initiatique, 
Max et Mila sont entraînés vers une quête 
qui dépasse largement la recherche d'un 
trésor matériel.

À travers l'île mystérieuse, les menaces 
et les découvertes, les deux protagonistes 
apprennent que le véritable trésor gît en 
eux : le courage de se dépasser et la force 
de l'amitié.

Une méditation sur la croissance, 
l'intrépidité et la conscience de soi."""
    
    font_resume = get_font(85)
    draw.text((SIZE_PX//2, 1200), resume, fill='#333333', font=font_resume, anchor='mm',
             align='center', spacing=45)
    
    # Bande dorée en bas
    draw.rectangle([0, SIZE_PX - 350, SIZE_PX, SIZE_PX], fill='#DAA520')
    
    font_closing = get_font(90)
    draw.text((SIZE_PX//2, SIZE_PX - 175), '« Le courage est en chacun de nous »', 
             fill='#2C3E50', font=font_closing, anchor='mm')
    
    os.makedirs('illustrations_adult', exist_ok=True)
    img.save('illustrations_adult/back_cover.png', dpi=(DPI, DPI))
    print("✓ 4e de couverture adulte créée: illustrations_adult/back_cover.png")

def main():
    print("\n" + "="*70)
    print("🎨 CRÉATION DES COUVERTURES ET 4ES DE COUVERTURE")
    print("="*70 + "\n")
    
    create_kids_cover()
    create_kids_back_cover()
    
    print()
    
    create_adult_cover()
    create_adult_back_cover()
    
    print("\n" + "="*70)
    print("✅ TOUTES LES COUVERTURES ONT ÉTÉ CRÉÉES!")
    print("="*70)
    print("\n📁 Fichiers générés:")
    print("  ENFANTS (BD):")
    print("    • illustrations_kids/cover.png")
    print("    • illustrations_kids/back_cover.png")
    print("\n  ADULTE (Réaliste):")
    print("    • illustrations_adult/cover.png")
    print("    • illustrations_adult/back_cover.png")

if __name__ == "__main__":
    main()
