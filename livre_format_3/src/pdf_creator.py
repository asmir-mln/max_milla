"""
Créateur de PDF pour le livre Format 3
"""

from reportlab.platypus import SimpleDocTemplate, Image as RLImage, PageBreak
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import config

def create_pdf(page_files, output_filename=config.PDF_OUTPUT):
    """Crée un PDF à partir des fichiers PNG des pages"""
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []
    
    for page_file in page_files:
        # Ajouter image de page
        elements.append(RLImage(page_file, width=19*cm, height=19*cm))
        # Ajouter saut de page
        elements.append(PageBreak())
    
    # Générer le PDF
    doc.build(elements)
    print(f"\nPDF généré avec succès: {output_filename}")

def merge_pdfs(pdf_files, output_filename="Max_Mila_Complete.pdf"):
    """Fusionne plusieurs fichiers PDF
    
    Note: Nécessite la libraire PyPDF2
    """
    try:
        from PyPDF2 import PdfMerger
        
        merger = PdfMerger()
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        
        merger.write(output_filename)
        merger.close()
        print(f"PDFs fusionnés avec succès: {output_filename}")
    except ImportError:
        print("PyPDF2 non installé. Installez-le avec: pip install PyPDF2")

def get_pdf_info(pdf_filename):
    """Obtient les informations du PDF"""
    import os
    if os.path.exists(pdf_filename):
        size = os.path.getsize(pdf_filename)
        print(f"Fichier: {pdf_filename}")
        print(f"Taille: {size / (1024*1024):.2f} MB")
        return True
    return False
