"""
Script de génération d'illustrations réalistes pour Max et Mila
Utilise plusieurs techniques pour créer des images de qualité professionnelle
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import random
import math

# Configuration
DPI = 300
SIZE_PX = 2362
OUTPUT_KIDS = "illustrations_kids"
OUTPUT_ADULT = "illustrations_adult"

# Palettes de couleurs
PALETTE_KIDS = {
    'sky': ['#87CEEB', '#B0E0E6', '#ADD8E6'],
    'ocean': ['#1E90FF', '#4169E1', '#0000CD'],
    'sun': ['#FFD700', '#FFA500', '#FF8C00'],
    'skin': ['#FFDBAC', '#F1C27D', '#E0AC69'],
    'green': ['#90EE90', '#98FB98', '#7CFC00']
}

PALETTE_ADULT = {
    'sky': ['#4A5568', '#2D3748', '#1A202C'],
    'ocean': ['#2C5F7E', '#1A4D6E', '#0F3B5E'],
    'accent': ['#DAA520', '#B8860B', '#CD853F'],
    'neutral': ['#F5F5DC', '#E8E8D8', '#D3D3C8']
}

# Textes de l'histoire
STORY_TEXTS = [
    "Max regardait l'horizon en rêvant d'aventure.",
    "Un perroquet coloré descendit du ciel et cria.",
    "«Mon trésor ! Mon trésor !» répétait-il.",
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

class RealisticImageGenerator:
    """Générateur d'images avec effets réalistes"""
    
    def __init__(self, style='kids'):
        self.size = SIZE_PX
        self.style = style
        self.palette = PALETTE_KIDS if style == 'kids' else PALETTE_ADULT
        
    def create_canvas(self, base_color='white'):
        """Créer un canvas avec gradient de fond"""
        img = Image.new('RGB', (self.size, self.size), base_color)
        return img
    
    def add_gradient(self, img, color1, color2, direction='vertical'):
        """Ajouter un gradient réaliste"""
        draw = ImageDraw.Draw(img)
        
        if direction == 'vertical':
            for y in range(self.size):
                ratio = y / self.size
                r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
                g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
                b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
                draw.line([(0, y), (self.size, y)], fill=(r, g, b))
        else:
            for x in range(self.size):
                ratio = x / self.size
                r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
                g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
                b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
                draw.line([(x, 0), (x, self.size)], fill=(r, g, b))
        
        return img
    
    def add_texture(self, img, intensity=0.1):
        """Ajouter une texture pour effet réaliste"""
        # Créer un layer de bruit
        pixels = img.load()
        for y in range(self.size):
            for x in range(0, self.size, 3):  # Optimisation : traiter 1 pixel sur 3
                noise = random.randint(-int(255 * intensity), int(255 * intensity))
                if pixels[x, y]:
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (
                        max(0, min(255, r + noise)),
                        max(0, min(255, g + noise)),
                        max(0, min(255, b + noise))
                    )
        return img
    
    def add_soft_shadow(self, img, shape_img, offset=(10, 10)):
        """Ajouter une ombre douce"""
        shadow = Image.new('RGBA', (self.size, self.size), (0, 0, 0, 0))
        shadow.paste(shape_img, offset)
        shadow = shadow.filter(ImageFilter.GaussianBlur(15))
        
        # Réduire l'opacité
        alpha = shadow.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(0.3)
        shadow.putalpha(alpha)
        
        img = img.convert('RGBA')
        img = Image.alpha_composite(img, shadow)
        return img.convert('RGB')
    
    def draw_sky_realistic(self, img, time='day'):
        """Dessiner un ciel réaliste"""
        if time == 'day':
            colors = self.palette['sky']
            img = self.add_gradient(img, colors[0], colors[1])
        elif time == 'sunset':
            img = self.add_gradient(img, '#FF6B6B', '#FFA500')
        
        # Ajouter des nuages
        draw = ImageDraw.Draw(img, 'RGBA')
        for _ in range(random.randint(3, 6)):
            x = random.randint(0, self.size)
            y = random.randint(0, self.size // 2)
            for j in range(3):
                cx = x + j * 60
                draw.ellipse([cx - 80, y - 40, cx + 80, y + 40], 
                           fill=(255, 255, 255, random.randint(100, 180)))
        
        return img
    
    def draw_ocean_realistic(self, img, y_start=None):
        """Dessiner un océan réaliste avec vagues"""
        if y_start is None:
            y_start = self.size // 2
        
        # Gradient océan
        colors = self.palette['ocean']
        for y in range(y_start, self.size):
            ratio = (y - y_start) / (self.size - y_start)
            r = int(int(colors[0][1:3], 16) * (1 - ratio) + int(colors[1][1:3], 16) * ratio)
            g = int(int(colors[0][3:5], 16) * (1 - ratio) + int(colors[1][3:5], 16) * ratio)
            b = int(int(colors[0][5:7], 16) * (1 - ratio) + int(colors[1][5:7], 16) * ratio)
            
            draw = ImageDraw.Draw(img)
            draw.line([(0, y), (self.size, y)], fill=(r, g, b))
        
        # Ajouter des vagues
        draw = ImageDraw.Draw(img, 'RGBA')
        for i in range(5):
            y = y_start + i * 150
            for x in range(0, self.size, 100):
                wave_y = y + int(20 * math.sin(x / 100))
                draw.arc([x - 50, wave_y - 20, x + 50, wave_y + 20], 
                        0, 180, fill=(255, 255, 255, 100), width=3)
        
        return img
    
    def draw_character_advanced(self, img, x, y, name='Max', emotion='happy'):
        """Dessiner un personnage avec plus de détails"""
        draw = ImageDraw.Draw(img, 'RGBA')
        
        skin = '#FFDBAC' if self.style == 'kids' else '#E0AC69'
        
        # Corps (forme plus réaliste)
        body_points = [
            (x, y + 80), (x - 50, y + 120), (x - 60, y + 200),
            (x + 60, y + 200), (x + 50, y + 120)
        ]
        draw.polygon(body_points, fill='#4169E1' if name == 'Max' else '#FF69B4')
        
        # Tête (cercle avec ombrage)
        draw.ellipse([x - 50, y - 50, x + 50, y + 50], fill=skin, outline='#8B4513', width=3)
        
        # Yeux
        if emotion == 'happy':
            draw.ellipse([x - 25, y - 10, x - 10, y + 5], fill='#000000')
            draw.ellipse([x + 10, y - 10, x + 25, y + 5], fill='#000000')
            draw.ellipse([x - 20, y - 5, x - 15, y], fill='#FFFFFF')  # Reflet
            draw.ellipse([x + 15, y - 5, x + 20, y], fill='#FFFFFF')
        elif emotion == 'scared':
            draw.ellipse([x - 30, y - 15, x - 5, y + 10], fill='#000000')
            draw.ellipse([x + 5, y - 15, x + 30, y + 10], fill='#000000')
        
        # Bouche
        if emotion == 'happy':
            draw.arc([x - 20, y + 10, x + 20, y + 30], 0, 180, fill='#8B4513', width=3)
        elif emotion == 'scared':
            draw.ellipse([x - 15, y + 15, x + 15, y + 30], fill='#000000')
        
        # Cheveux
        hair_color = '#654321' if name == 'Max' else '#FFD700'
        for i in range(-40, 50, 20):
            draw.ellipse([x + i - 15, y - 60, x + i + 15, y - 30], fill=hair_color)
        
        # Bras
        draw.rectangle([x - 80, y + 90, x - 60, y + 160], fill=skin)
        draw.rectangle([x + 60, y + 90, x + 80, y + 160], fill=skin)
        
        # Jambes
        draw.rectangle([x - 35, y + 200, x - 15, y + 300], fill='#4169E1' if name == 'Max' else '#FF69B4')
        draw.rectangle([x + 15, y + 200, x + 35, y + 300], fill='#4169E1' if name == 'Max' else '#FF69B4')
        
        return img
    
    def draw_parrot_advanced(self, img, x, y):
        """Dessiner un perroquet détaillé"""
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Corps avec dégradé
        colors = ['#FF0000', '#FF6347', '#FF4500']
        for i, color in enumerate(colors):
            offset = i * 15
            draw.ellipse([x - 60 + offset, y - 40 + offset, x + 60 - offset, y + 80 - offset], 
                        fill=color)
        
        # Tête
        draw.ellipse([x - 40, y - 80, x + 40, y - 20], fill='#FFD700')
        
        # Bec
        beak_points = [(x, y - 40), (x - 25, y - 25), (x, y - 10)]
        draw.polygon(beak_points, fill='#FFA500', outline='#FF8C00', width=2)
        
        # Œil avec détails
        draw.ellipse([x - 20, y - 60, x - 5, y - 45], fill='#000000')
        draw.ellipse([x - 15, y - 57, x - 10, y - 52], fill='#FFFFFF')
        
        # Ailes avec plumes
        wing_colors = ['#00FF00', '#32CD32', '#228B22']
        for i, color in enumerate(wing_colors):
            offset = i * 10
            draw.ellipse([x - 90 + offset, y - 20 + offset, x - 30 + offset, y + 40 - offset], 
                        fill=color)
            draw.ellipse([x + 30 - offset, y - 20 + offset, x + 90 - offset, y + 40 - offset], 
                        fill=color)
        
        # Queue colorée
        tail_colors = ['#FF0000', '#FFD700', '#00FF00', '#0000FF']
        for i, color in enumerate(tail_colors):
            offset = i * 15
            draw.rectangle([x - 20 + offset, y + 80, x - 10 + offset, y + 150], fill=color)
        
        return img
    
    def add_text_bubble(self, img, text, x, y, width=400):
        """Ajouter une bulle de texte style BD"""
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Bulle
        draw.ellipse([x - width//2, y - 80, x + width//2, y + 40], 
                    fill=(255, 255, 255, 230), outline='#000000', width=4)
        
        # Pointe de la bulle
        points = [(x - 20, y + 40), (x, y + 80), (x + 20, y + 40)]
        draw.polygon(points, fill=(255, 255, 255, 230), outline='#000000')
        
        # Texte
        try:
            font = ImageFont.truetype("arial.ttf", 50)
        except:
            font = ImageFont.load_default()
        
        # Centrer le texte
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = x - text_width // 2
        
        draw.text((text_x, y - 50), text, fill='#000000', font=font)
        
        return img
    
    def save_image(self, img, filename, optimize=True):
        """Sauvegarder l'image avec optimisation"""
        img.save(filename, 'PNG', dpi=(DPI, DPI), optimize=optimize)
        print(f"✓ {filename}")


def generate_all_pages():
    """Générer toutes les pages pour les deux versions"""
    
    print("\n" + "="*60)
    print("GÉNÉRATION DES ILLUSTRATIONS RÉALISTES")
    print("="*60)
    
    # Créer les dossiers
    os.makedirs(OUTPUT_KIDS, exist_ok=True)
    os.makedirs(OUTPUT_ADULT, exist_ok=True)
    
    # ========== VERSION ENFANTS (BD STYLE) ==========
    print("\n📚 Génération version ENFANTS (Style BD)...")
    gen_kids = RealisticImageGenerator('kids')
    
    # Page 1: Max regarde l'horizon
    img = gen_kids.create_canvas()
    img = gen_kids.draw_sky_realistic(img, 'day')
    img = gen_kids.draw_ocean_realistic(img, y_start=1400)
    img = gen_kids.draw_character_advanced(img, 600, 1200, 'Max', 'happy')
    gen_kids.save_image(img, os.path.join(OUTPUT_KIDS, 'page01.png'))
    
    # Page 2: Perroquet apparait
    img = gen_kids.create_canvas()
    img = gen_kids.draw_sky_realistic(img, 'day')
    img = gen_kids.draw_parrot_advanced(img, 1200, 600)
    img = gen_kids.draw_character_advanced(img, 600, 1400, 'Max', 'happy')
    gen_kids.save_image(img, os.path.join(OUTPUT_KIDS, 'page02.png'))
    
    # Page 3: "MON TRÉSOR!"
    img = gen_kids.create_canvas()
    img = gen_kids.draw_sky_realistic(img, 'day')
    img = gen_kids.draw_parrot_advanced(img, 1200, 800)
    img = gen_kids.add_text_bubble(img, "MON TRÉSOR!", 1200, 500)
    img = gen_kids.draw_character_advanced(img, 600, 1400, 'Max', 'happy')
    gen_kids.save_image(img, os.path.join(OUTPUT_KIDS, 'page03.png'))
    
    # Pages 4-12: Générer avec variations
    scenes = [
        ('day', 'Max', 'happy', 1000),
        ('day', 'Max', 'happy', 1200),
        ('day', 'Max', 'scared', 1100),
        ('day', 'Mila', 'happy', 1000),
        ('sunset', 'Max', 'happy', 1100),
        ('sunset', 'Max', 'scared', 1200),
        ('day', 'Max', 'happy', 1000),
        ('day', 'Max', 'happy', 1100),
        ('sunset', 'Max', 'happy', 1200)
    ]
    
    for i, (time, char, emotion, ocean_y) in enumerate(scenes, start=4):
        img = gen_kids.create_canvas()
        img = gen_kids.draw_sky_realistic(img, time)
        img = gen_kids.draw_ocean_realistic(img, y_start=ocean_y)
        img = gen_kids.draw_character_advanced(img, 600, 1000, char, emotion)
        if i == 7:  # Ajouter Mila
            img = gen_kids.draw_character_advanced(img, 900, 1000, 'Mila', 'happy')
        gen_kids.save_image(img, os.path.join(OUTPUT_KIDS, f'page{i:02d}.png'))
    
    # ========== VERSION ADULTE (STYLE RÉALISTE) ==========
    print("\n📖 Génération version ADULTE (Style Littéraire)...")
    gen_adult = RealisticImageGenerator('adult')
    
    for i in range(1, 13):
        img = gen_adult.create_canvas()
        
        # Fond artistique
        img = gen_adult.add_gradient(img, '#2C3748', '#4A5568')
        img = gen_adult.add_texture(img, 0.05)
        
        # Zone de texte élégante
        draw = ImageDraw.Draw(img, 'RGBA')
        draw.rectangle([100, 1800, SIZE_PX - 100, 2262], 
                      fill=(245, 245, 220, 200))
        
        # Bordure dorée
        draw.rectangle([100, 1800, SIZE_PX - 100, 2262], 
                      outline='#DAA520', width=5)
        
        # Texte
        try:
            font = ImageFont.truetype("arial.ttf", 55)
        except:
            font = ImageFont.load_default()
        
        text = STORY_TEXTS[i - 1]
        draw.text((200, 1900), text, fill='#2C3E50', font=font)
        
        gen_adult.save_image(img, os.path.join(OUTPUT_ADULT, f'page{i:02d}.png'))
    
    print("\n" + "="*60)
    print("✅ GÉNÉRATION TERMINÉE!")
    print(f"   • 12 pages version ENFANTS dans {OUTPUT_KIDS}/")
    print(f"   • 12 pages version ADULTE dans {OUTPUT_ADULT}/")
    print("="*60 + "\n")


if __name__ == '__main__':
    try:
        generate_all_pages()
    except Exception as e:
        print(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
