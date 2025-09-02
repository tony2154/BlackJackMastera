
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


LOG_FOLDER = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_FOLDER, exist_ok=True)


CARD_TEMPLATES_DIR = os.path.join(BASE_DIR, "utils", "data", "card_templates")


STARTING_BALANCE = 100       # tu apuesta inicial
MIN_BET = 20                 # apuesta mínima
MAX_BET = 100                # apuesta máxima

BET_ALERT_THRESHOLD = 3      # umbral para alertas de apuestas


GAME_REGION = (100, 200, 800, 600)

# ---------------------------------------------------
# Umbral para detección de cartas
# ---------------------------------------------------
TEMPLATE_THRESHOLD = 0.75  # coincidencia mínima para template matching

# ---------------------------------------------------
# Valores de cartas para conteo Hi-Lo
# ---------------------------------------------------
CARD_VALUES = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

# AUTO REGION
GAME_REGION = (652, 972, 47, 0)

# AUTO REGION
GAME_REGION = (1088, 1003, 23, 4)

# AUTO REGION
GAME_REGION = (944, 982, 358, 3)
