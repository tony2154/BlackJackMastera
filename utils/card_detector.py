import cv2
import os
import numpy as np
from config import TEMPLATE_THRESHOLD, CARD_VALUES

# ---------------------------------------------------
# Configuración de rutas
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "data", "card_templates")  # apunta a utils/data/card_templates

print("Buscando plantillas en:", TEMPLATES_DIR)  # Verifica que la ruta sea correcta

# ---------------------------------------------------
# Cargar plantillas de cartas
# ---------------------------------------------------
def load_templates():
    templates = {}
    for fname in os.listdir(TEMPLATES_DIR):
        if fname.endswith(".png") or fname.endswith(".jpg"):
            path = os.path.join(TEMPLATES_DIR, fname)
            card_name = os.path.splitext(fname)[0]
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                templates[card_name] = img
            else:
                print(f"No se pudo cargar la plantilla: {fname}")
    return templates

CARD_TEMPLATES = load_templates()

# ---------------------------------------------------
# Detectar cartas en una imagen
# ---------------------------------------------------
def detect_cards(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_cards = []

    for name, template in CARD_TEMPLATES.items():
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= TEMPLATE_THRESHOLD)
        for pt in zip(*loc[::-1]):
            detected_cards.append({
                "name": name,
                "position": pt
            })
    return detected_cards

# ---------------------------------------------------
# Calcular valor Hi-Lo (o cualquier otra lógica)
# ---------------------------------------------------
def compute_hilo(cards):
    total = 0
    for card in cards:
        value = CARD_VALUES.get(card["name"], 0)
        if value >= 2 and value <= 6:
            total += 1
        elif value == 10 or value == 11:  # asumiendo que As=11
            total -= 1
    return total

# ---------------------------------------------------
# Prueba rápida
# ---------------------------------------------------
if __name__ == "__main__":
    print(f"Se cargaron {len(CARD_TEMPLATES)} plantillas de cartas.")
