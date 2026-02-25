"""
Générateur d'illustrations stylisées pour le livre "Max et Mila"
Version 1: BD enfants avec dialogues en bulles
Version 2: Style réaliste adulte
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# =========================
# CONFIGURATION
# =========================

SIZE_PX = 2362
DPI = 300
OUTPUT_KIDS = "illustrations_kids"
OUTPUT_ADULT = "illustrations_adult"

os.makedirs(OUTPUT_KIDS, exist_ok=True)
os.makedirs(OUTPUT_ADULT, exist_ok=True)

# Couleurs
COLORS = {
    'sky_light': '#87CEEB',
    'sky_dark': '#4A90E2',
    'ocean': '#1E90FF',
    'sand': '#F4A460',
    'forest': '#228B22',
    'jungle': '#2D5016',
    'white': '#FFFFFF',
    'black': '#000000',
    'yellow': '#FFD700',
    'red': '#FF6347',
    'green': '#32CD32',
    'orange': '#FF8C00'
}

# =========================
# POLICES
# =========================

def get_font(size, bold=False):
    try:
        font_name = "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except:
        return ImageFont.load_default()

# =========================
# FORMES DE BASE (ENFANTS)
# =========================

def draw_circle(draw, x, y, r, fill, outline='black', width=3):
    """Dessine un cercle"""
    draw.ellipse([x-r, y-r, x+r, y+r], fill=fill, outline=outline, width=width)

def draw_rect_rounded(draw, x1, y1, x2, y2, radius=50, fill='white', outline='black', width=3):
    """Dessine un rectangle arrondi"""
    points = [
        (x1+radius, y1), (x2-radius, y1), (x2, y1), (x2, y1+radius),
        (x2, y2-radius), (x2, y2), (x2-radius, y2), (x1+radius, y2),
        (x1, y2), (x1, y2-radius), (x1, y1+radius), (x1, y1)
    ]
    draw.polygon(points, fill=fill, outline=outline)
    if width > 0:
        draw.polygon(points, fill=None, outline=outline, width=width)

def draw_dialogue_bubble(draw, x, y, text, width=600, height=300, fill='white'):
    """Dessine une bulle de dialogue"""
    draw_rect_rounded(draw, x-width//2, y-height//2, x+width//2, y+height//2, 
                      radius=40, fill=fill, outline='black', width=5)
    
    # Petit triangle pointeur
    triangle = [(x, y+height//2+20), (x-40, y+height//2+60), (x+40, y+height//2+60)]
    draw.polygon(triangle, fill=fill, outline='black')
    draw.line([triangle[0], triangle[1]], fill='black', width=5)
    draw.line([triangle[0], triangle[2]], fill='black', width=5)

def draw_character_simple(draw, x, y, name, color):
    """Dessine un personnage simple (enfant BD)"""
    # Tête
    draw_circle(draw, x, y-200, 80, color, 'black', 5)
    
    # Yeux
    draw_circle(draw, x-30, y-220, 15, 'white', 'black', 2)
    draw_circle(draw, x+30, y-220, 15, 'white', 'black', 2)
    draw_circle(draw, x-30, y-220, 8, 'black')
    draw_circle(draw, x+30, y-220, 8, 'black')
    
    # Bouche
    draw.arc([x-25, y-200, x+25, y-170], 0, 180, fill='black', width=5)
    
    # Corps
    draw.rectangle([x-40, y-120, x+40, y], fill=color, outline='black', width=4)
    
    # Bras
    draw.line([x-40, y-80, x-120, y-60], fill=color, width=20)
    draw.line([x+40, y-80, x+120, y-60], fill=color, width=20)
    
    # Jambes
    draw.line([x-20, y, x-20, y+80], fill='#8B4513', width=25)
    draw.line([x+20, y, x+20, y+80], fill='#8B4513', width=25)

# =========================
# ÉLÉMENTS DE PAYSAGE
# =========================

def draw_sky(draw, gradient_top, gradient_bottom):
    """Dessine un ciel avec dégradé"""
    # Version simplifiée: deux couleurs
    draw.rectangle([0, 0, SIZE_PX, SIZE_PX//2], fill=gradient_top)

def draw_ocean(draw, color=COLORS['ocean']):
    """Dessine l'océan"""
    y_start = SIZE_PX // 2
    draw.rectangle([0, y_start, SIZE_PX, SIZE_PX], fill=color)
    
    # Vagues
    for i in range(0, SIZE_PX, 300):
        draw.ellipse([i, y_start-50, i+200, y_start+50], outline='white', width=8)

def draw_island(draw, cx, cy, size):
    """Dessine une île"""
    # Terre
    draw_circle(draw, cx, cy, size, COLORS['sand'], 'black', 8)
    
    # Palmier
    # Tronc
    draw.rectangle([cx-30, cy-size+50, cx+30, cy+100], fill='#8B4513', outline='black', width=3)
    # Feuilles
    draw_circle(draw, cx-100, cy-size+100, 60, COLORS['green'], 'black', 4)
    draw_circle(draw, cx+100, cy-size+100, 60, COLORS['green'], 'black', 4)
    draw_circle(draw, cx, cy-size, 60, COLORS['green'], 'black', 4)

def draw_boat(draw, x, y, size):
    """Dessine un bateau pirate"""
    # Coque
    points = [(x-size, y), (x+size, y), (x+size//2, y+size//2), (x-size//2, y+size//2)]
    draw.polygon(points, fill='#8B4513', outline='black', width=5)
    
    # Mât
    draw.line([x, y-size//2, x, y-size*2], fill='#654321', width=15)
    
    # Voile avec skull
    draw.polygon([(x, y-size*2), (x-size, y-size), (x, y)], fill='black', outline='white', width=3)
    draw_circle(draw, x-size//2, y-size, 30, COLORS['white'], COLORS['black'], 3)

def draw_chest(draw, x, y, size):
    """Dessine un coffre au trésor"""
    # Coffre
    draw.rectangle([x-size, y-size//2, x+size, y+size//2], fill='#DAA520', outline='black', width=8)
    
    # Couvercle
    draw.polygon([(x-size, y-size//2), (x+size, y-size//2), 
                  (x+size, y-size), (x-size, y-size)], 
                fill='#B8860B', outline='black', width=5)
    
    # Pièces d'or
    for i in range(-3, 4):
        draw_circle(draw, x+i*30, y, 15, COLORS['yellow'], 'black', 2)

def draw_parrot(draw, x, y, size):
    """Dessine un perroquet"""
    # Corps
    draw_circle(draw, x, y, size//2, COLORS['red'], 'black', 5)
    
    # Tête
    draw_circle(draw, x+size, y-size//2, size//2, COLORS['orange'], 'black', 5)
    
    # Oeil
    draw_circle(draw, x+size+10, y-size//2, 15, 'white', 'black', 2)
    draw_circle(draw, x+size+10, y-size//2, 8, 'black')
    
    # Bec
    draw.polygon([(x+size+40, y-size//2), (x+size+80, y-size//2-20), 
                  (x+size+80, y-size//2+20)], fill=COLORS['yellow'], outline='black', width=3)
    
    # Ailes
    draw.ellipse([x-size, y-size, x, y+size], fill=COLORS['red'], outline='black', width=3)

# =========================
# ILLUSTRATIONS ENFANTS (BD)
# =========================

story_kids_images = [
    {
        'title': 'Je rêvais d\'aventure...',
        'dialogue': 'Max: Je rêve d\'aventure!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_character_simple(draw, 700, 1200, '#FF69B4', 'yellow'),  # Max
            draw_character_simple(draw, 1700, 1200, '#FFB6C1', 'pink'),   # Mila
        )
    },
    {
        'title': 'Un perroquet mystérieux apparut.',
        'dialogue': 'Perroquet: Ahoy!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_dark']),
            draw_parrot(draw, 1200, 600, 150),
            draw_character_simple(draw, 400, 1200, '#FF69B4', 'yellow'),
            draw_character_simple(draw, 1900, 1200, '#FFB6C1', 'pink'),
        )
    },
    {
        'title': 'MON TRÉSOR !',
        'dialogue': 'Perroquet: MON TRÉSOR!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_parrot(draw, 1200, 500, 120),
            draw_chest(draw, 1200, 1400, 200),
        )
    },
    {
        'title': 'Une île magique nous attendait.',
        'dialogue': 'Max: C\'est magnifique!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX//2], fill=COLORS['sky_light']),
            draw.rectangle([0, SIZE_PX//2, SIZE_PX, SIZE_PX], fill=COLORS['ocean']),
            draw_island(draw, SIZE_PX//2, SIZE_PX//2, 400),
        )
    },
    {
        'title': 'Un bateau pirate surgit.',
        'dialogue': 'Max: Oh non!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX//2], fill=COLORS['sky_dark']),
            draw.rectangle([0, SIZE_PX//2, SIZE_PX, SIZE_PX], fill=COLORS['ocean']),
            draw_boat(draw, 300, SIZE_PX//2+100, 150),
            draw_island(draw, 1600, SIZE_PX//2, 300),
        )
    },
    {
        'title': 'J\'avais peur.',
        'dialogue': 'Max: Panique!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_boat(draw, 600, 800, 200),
            draw_character_simple(draw, 1700, 1200, '#FF69B4', 'yellow'),
        )
    },
    {
        'title': 'Mais Mila croyait en moi.',
        'dialogue': 'Mila: Tu peux le faire!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_character_simple(draw, 600, 1200, '#FF69B4', 'yellow'),
            draw_character_simple(draw, 1700, 1200, '#FFB6C1', 'pink'),
        )
    },
    {
        'title': 'Le coffre brillait.',
        'dialogue': 'Mila: Regarde!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX//2], fill=COLORS['sky_light']),
            draw.rectangle([0, SIZE_PX//2, SIZE_PX, SIZE_PX], fill=COLORS['sand']),
            draw_chest(draw, SIZE_PX//2, SIZE_PX//2+400, 250),
        )
    },
    {
        'title': 'Le danger approchait.',
        'dialogue': 'Max: Attention!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_boat(draw, 1700, 400, 180),
            draw_character_simple(draw, 600, 1200, '#FF69B4', 'yellow'),
        )
    },
    {
        'title': 'Je devais être courageux.',
        'dialogue': 'Max: Je vais essayer!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_character_simple(draw, SIZE_PX//2, 1200, '#FF69B4', 'yellow'),
        )
    },
    {
        'title': 'Le vrai trésor n\'était pas l\'or.',
        'dialogue': 'Mila: Le trésor c\'est nous!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_character_simple(draw, 600, 1200, '#FF69B4', 'yellow'),
            draw_character_simple(draw, 1700, 1200, '#FFB6C1', 'pink'),
        )
    },
    {
        'title': 'Il était en moi.',
        'dialogue': 'Max: Le courage!',
        'draw': lambda draw: (
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light']),
            draw_character_simple(draw, SIZE_PX//2, 1200, '#FF69B4', 'yellow'),
        )
    }
]

# =========================
# GÉNÉRATION DES ILLUSTRATIONS ENFANTS
# =========================

def generate_kids_illustrations():
    """Génère les illustrations style BD pour enfants"""
    print("\n" + "="*70)
    print("🎨 GÉNÉRATION DES ILLUSTRATIONS BD (4-10 ans)")
    print("="*70 + "\n")
    
    for i, scene in enumerate(story_kids_images, 1):
        img = Image.new('RGB', (SIZE_PX, SIZE_PX), 'white')
        draw = ImageDraw.Draw(img)
        
        # Dessiner la scène
        if callable(scene['draw']):
            scene['draw'](draw)
        
        # Ajouter le titre
        title_font = get_font(120, bold=True)
        draw.text((100, 100), scene['title'], fill='black', font=title_font)
        
        # Ajouter la bulle de dialogue
        dialogue_font = get_font(80)
        bubble_y = SIZE_PX - 400
        draw_dialogue_bubble(draw, SIZE_PX//2, bubble_y, scene['dialogue'], 
                           width=1200, height=300, fill=COLORS['white'])
        
        # Texte du dialogue
        text_lines = scene['dialogue'].split(':')
        for line_idx, line in enumerate(text_lines):
            line_y = bubble_y - 80 + (line_idx * 100)
            draw.text((SIZE_PX//2 - 400, line_y), line.strip(), 
                     fill='black', font=dialogue_font, anchor='lm')
        
        # Signature
        sig_font = get_font(60)
        draw.text((SIZE_PX - 600, SIZE_PX - 150), "Asmir MLN", 
                 fill='gray', font=sig_font)
        
        # Sauvegarder
        filename = f"{OUTPUT_KIDS}/page_{i:02d}.png"
        img.save(filename, dpi=(DPI, DPI))
        print(f"✓ Page {i}: {scene['title'][:40]}... ({filename})")
    
    print(f"\n✅ {len(story_kids_images)} illustrations BD créées!")

# =========================
# ILLUSTRATIONS ADULTE (RÉALISTE)
# =========================

def generate_adult_illustrations():
    """Génère les illustrations style réaliste pour adultes"""
    print("\n" + "="*70)
    print("🎨 GÉNÉRATION DES ILLUSTRATIONS RÉALISTE (ADULTE)")
    print("="*70 + "\n")
    
    story_adult = [
        "Max regardait l'horizon en rêvant d'aventure.",
        "Un perroquet coloré descendit du ciel.",
        "Ses cris résonnaient: MON TRÉSOR!",
        "Ils découvrirent une île mystérieuse.",
        "Un navire pirate apparaissait.",
        "L'inconnu envahissait Max.",
        "L'amitié de Mila le rassurait.",
        "Le coffre brillait sous le soleil.",
        "Le danger s'approchait.",
        "Max trouva le courage.",
        "Le trésor était intérieur.",
        "La victoire était collective."
    ]
    
    for i, text in enumerate(story_adult, 1):
        img = Image.new('RGB', (SIZE_PX, SIZE_PX), COLORS['white'])
        draw = ImageDraw.Draw(img)
        
        # Fond dégradé simple
        if i <= 4:  # Premières pages: ciel et nuages
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill=COLORS['sky_light'])
        elif i <= 8:  # Milieu: île et océan
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX//2], fill=COLORS['sky_light'])
            draw.rectangle([0, SIZE_PX//2, SIZE_PX, SIZE_PX], fill=COLORS['ocean'])
        else:  # Fin: apaisement
            draw.rectangle([0, 0, SIZE_PX, SIZE_PX], fill='#FFE4B5')
        
        # Ajouter du texte littéraire
        text_font = get_font(100)
        lines = text.split()
        
        # Centrer et placer le texte
        y_pos = SIZE_PX//3
        for idx, word in enumerate(lines):
            x_pos = SIZE_PX//2 - len(word)*30
            draw.text((x_pos, y_pos + idx*150), word, fill='#333333', font=text_font)
        
        # Décoration: ligne de séparation
        draw.rectangle([SIZE_PX//4, SIZE_PX//2-10, 3*SIZE_PX//4, SIZE_PX//2+10], 
                      fill='#D4AF37')
        
        # Signature
        sig_font = get_font(60)
        draw.text((SIZE_PX - 600, SIZE_PX - 150), "Asmir MLN - 2026", 
                 fill='#666666', font=sig_font)
        
        # Sauvegarder
        filename = f"{OUTPUT_ADULT}/page_{i:02d}.png"
        img.save(filename, dpi=(DPI, DPI))
        print(f"✓ Page {i}: {text[:50]}... ({filename})")
    
    print(f"\n✅ {len(story_adult)} illustrations réalistes créées!")

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    print("\n📚 GÉNÉRATEUR D'ILLUSTRATIONS - MAX ET MILA")
    
    # Générer les deux versions
    generate_kids_illustrations()
    generate_adult_illustrations()
    
    print("\n" + "="*70)
    print("✅ TOUS LES FICHIERS ONT ÉTÉ GÉNÉRÉS!")
    print("="*70)
    print(f"\n📁 Version enfants (BD): {OUTPUT_KIDS}/")
    print(f"📁 Version adulte (Réaliste): {OUTPUT_ADULT}/")
