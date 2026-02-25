"""
Module principal pour la génération du troisième format de livre
"""

from .page_generator import generate_pages
from .pdf_creator import create_pdf

__version__ = "1.0.0"
__author__ = "Asmir MLN"

__all__ = ["generate_pages", "create_pdf"]
