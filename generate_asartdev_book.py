from PIL import Image, ImageDraw, ImageFont
from reportlab.platypus import SimpleDocTemplate, Image as RLImage, PageBreak
from reportlab.lib.units import cm
import os

# ==========================
# CONFIGURATION
# ==========================

SIZE_PX = 2362  # 20x20 cm en 300 DPI
PDF_NAME = "Max_Mila_BD_Complete_AsArtDev_20x20.pdf"

MODEL_IMAGE = "Max Mila et le trésor magique.png"
LOGO_INPUT = "logo.JPG"

# ==========================
# OUTILS
# ==========================

def load_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def create_canvas():
    return Image.new("RGB", (SIZE_PX, SIZE_PX), "white")

def add_bubble(draw, text, box):
    font = load_font(70)
    draw.ellipse(box, fill="white", outline="black", width=8)

    x = box[0] + 60
    y = box[1] + 80
    draw.text((x, y), text, fill="black", font=font)

def resize_model():
    img = Image.open(MODEL_IMAGE)
    img = img.resize((2000, 1400))
    return img

# ==========================
# LOGO PROPRE
# ==========================

logo = Image.open(LOGO_INPUT)
logo = logo.resize((800,800))
logo.save("logo.png", dpi=(300,300))

# ==========================
# COUVERTURE
# ==========================

cover = create_canvas()
model_img = resize_model()

cover.paste(model_img, (181, 200))

draw_cover = ImageDraw.Draw(cover)
font_title = load_font(120)

draw_cover.text((400, 50), "MAX MILA", fill="gold", font=font_title)
draw_cover.text((400, 180), "ET LE PERROQUET", fill="gold", font=font_title)

logo_small = logo.resize((250,250))
cover.paste(logo_small, (1050, 2000), logo_small)

cover.save("cover_front.png", dpi=(300,300))

# ==========================
# HISTOIRE ÉTIRÉE (12 pages)
# ==========================

story = [
"Je me souviens de mes 8 ans...",
"Les journées étaient difficiles à la maison.",
"Je rêvais d'aventure pour fuir mes peurs.",
"Un jour, un perroquet étrange est apparu.",
"Il cria : MON TRÉSOR !",
"Il disait que j'étais plus fort que je pensais.",
"Nous avons imaginé des îles lointaines.",
"Des pirates, des trésors cachés...",
"Chaque peur devenait un défi.",
"Chaque défi devenait courage.",
"Le vrai trésor n'était pas l'or.",
"C'était la force qui grandissait en moi."
]

# ==========================
# GENERATION PAGES BD
# ==========================

for i in range(12):
    page = create_canvas()

    model_img = resize_model()
    page.paste(model_img, (181, 200))

    draw = ImageDraw.Draw(page)

    add_bubble(draw, story[i], (400, 1700, 1960, 2200))

    page.save(f"page{i+1}.png", dpi=(300,300))

# ==========================
# GENERATION PDF
# ==========================

doc = SimpleDocTemplate(
    PDF_NAME,
    pagesize=(20*cm, 20*cm)
)

elements = []

elements.append(RLImage("cover_front.png", width=20*cm, height=20*cm))
elements.append(PageBreak())

for i in range(12):
    elements.append(RLImage(f"page{i+1}.png", width=20*cm, height=20*cm))
    elements.append(PageBreak())

doc.build(elements)

print("Livre BD complet 12 pages généré avec ton style et ton logo.")