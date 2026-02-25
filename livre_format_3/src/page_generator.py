"""
Générateur de pages pour le livre Format 3
"""

from PIL import Image, ImageDraw, ImageFont
import config

def load_font(size, fallback=True):
    """Charge une police TrueType ou utilise la police par défaut"""
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        if fallback:
            return ImageFont.load_default()
        return None

def create_blank_page(width=config.PAGE_SIZE_PX, height=config.PAGE_SIZE_PX, color=config.BG_COLOR):
    """Crée une page blanche vierge"""
    return Image.new("RGB", (width, height), color)

def add_title(page, title, y_position=100):
    """Ajoute un titre sur la page"""
    draw = ImageDraw.Draw(page)
    font = load_font(config.TITLE_FONT_SIZE)
    
    # Centrer le texte horizontalement
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    x = (config.PAGE_SIZE_PX - text_width) // 2
    
    draw.text((x, y_position), title, fill=config.TEXT_COLOR, font=font)

def add_illustration(page, img_path, x=181, y=200):
    """Ajoute une illustration sur la page"""
    try:
        illustration = Image.open(img_path).resize((2000, 1400))
        page.paste(illustration, (x, y))
    except Exception as e:
        print(f"Erreur lors du chargement de l'illustration: {e}")

def add_text_box(page, text, y_position=1800, bg_color=None, text_color=config.TEXT_COLOR):
    """Ajoute une boîte de texte sur la page"""
    draw = ImageDraw.Draw(page)
    font = load_font(config.TEXT_FONT_SIZE)
    
    # Fond optionnel
    if bg_color:
        draw.rectangle((0, y_position, config.PAGE_SIZE_PX, config.PAGE_SIZE_PX), fill=bg_color)
    
    # Texte centré
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (config.PAGE_SIZE_PX - text_width) // 2
    
    draw.text((x, y_position + 50), text, fill=text_color, font=font)

def add_footer(page, footer_text="Asmir MLN"):
    """Ajoute une signature en bas de page"""
    draw = ImageDraw.Draw(page)
    font = load_font(config.FOOTER_FONT_SIZE)
    
    draw.text((config.PAGE_SIZE_PX - 500, config.PAGE_SIZE_PX - 150),
              footer_text, fill=config.TEXT_COLOR, font=font)

def add_decorative_line(page, y_position=1750, color=config.ACCENT_COLOR, thickness=3):
    """Ajoute une ligne décorative"""
    draw = ImageDraw.Draw(page)
    draw.rectangle((200, y_position, config.PAGE_SIZE_PX - 200, y_position + thickness),
                   fill=color)

def generate_page(text_content, illustration_path=None, page_number=1):
    """Génère une page complète avec contenu"""
    page = create_blank_page()
    
    # Ajouter illustration si disponible
    if illustration_path:
        add_illustration(page, illustration_path)
    
    # Ajouter ligne décorative
    add_decorative_line(page, y_position=1750)
    
    # Ajouter le texte
    add_text_box(page, text_content, y_position=1800, bg_color="#f5e6c8")
    
    # Ajouter numéro de page
    add_footer(page, f"Page {page_number} - Asmir MLN")
    
    return page

def save_page(page, filename, dpi=config.DPI):
    """Sauvegarde une page en tant qu'image PNG"""
    page.save(filename, dpi=(dpi, dpi))

def generate_all_pages(stories, output_dir="output"):
    """Génère toutes les pages du livre"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    page_files = []
    for i, story in enumerate(stories, 1):
        page = generate_page(story, page_number=i)
        filename = f"{output_dir}/page_{i:02d}.png"
        save_page(page, filename)
        page_files.append(filename)
        print(f"Page {i} générée: {filename}")
    
    return page_files
