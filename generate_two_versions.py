from PIL import Image, ImageDraw, ImageFont
from reportlab.platypus import SimpleDocTemplate, Image as RLImage, PageBreak
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import os

# =========================
# CONFIGURATION
# =========================

DPI = 300
SIZE_CM = 20
SIZE_PX = 2362

ILLUSTRATION = "illustration.png"
LOGO = "logo.png"

PDF_V1 = "Max_Mila_Version1_BD.pdf"
PDF_V3 = "Max_Mila_Version3_Album.pdf"

# =========================
# OUTILS
# =========================

def font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def create_canvas():
    return Image.new("RGB", (SIZE_PX, SIZE_PX), "white")

def save_page(img, name):
    img.save(name, dpi=(300,300))

def add_logo_top(page):
    logo = Image.open(LOGO).resize((200,200))
    page.paste(logo, (SIZE_PX//2 - 100, 50), logo)

def add_signature(draw):
    draw.text((SIZE_PX - 500, SIZE_PX - 150),
              "Asmir MLN",
              fill="black",
              font=font(50))

# =========================
# HISTOIRE 12 PAGES
# =========================

story_short = [
"Je rêvais d'aventure...",
"Un perroquet mystérieux apparut.",
"MON TRÉSOR !",
"Une île magique nous attendait.",
"Un bateau pirate surgit.",
"J'avais peur.",
"Mais Mila croyait en moi.",
"Le coffre brillait.",
"Le danger approchait.",
"Je devais être courageux.",
"Le vrai trésor n'était pas l'or.",
"Il était en moi."
]

story_long = [
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
# VERSION 1 – BD 1 CASE
# =========================

def generate_version1():

    for i in range(12):
        page = create_canvas()
        illu = Image.open(ILLUSTRATION).resize((2000,1400))
        page.paste(illu, (181,200))

        draw = ImageDraw.Draw(page)

        draw.ellipse((400,1700,1960,2200), fill="white", outline="black", width=8)
        draw.text((500,1800), story_short[i], fill="black", font=font(60))

        add_signature(draw)
        save_page(page, f"v1_page{i+1}.png")

    # PDF
    doc = SimpleDocTemplate(PDF_V1, pagesize=letter)
    elements = []

    for i in range(12):
        elements.append(RLImage(f"v1_page{i+1}.png", width=19*cm, height=19*cm))
        elements.append(PageBreak())

    doc.build(elements)

# =========================
# VERSION 3 – ALBUM TEXTE BAS
# =========================

def generate_version3():

    for i in range(12):
        page = create_canvas()
        illu = Image.open(ILLUSTRATION).resize((2000,1600))
        page.paste(illu, (181,100))

        draw = ImageDraw.Draw(page)

        draw.rectangle((0,1800,SIZE_PX,2362), fill="#f5e6c8")
        draw.text((200,1900), story_long[i], fill="black", font=font(60))

        add_signature(draw)
        save_page(page, f"v3_page{i+1}.png")

    # PDF
    doc = SimpleDocTemplate(PDF_V3, pagesize=letter)
    elements = []

    for i in range(12):
        elements.append(RLImage(f"v3_page{i+1}.png", width=19*cm, height=19*cm))
        elements.append(PageBreak())

    doc.build(elements)

# =========================
# EXECUTION
# =========================

generate_version1()
generate_version3()

print("Les deux livres ont été générés avec succès.")