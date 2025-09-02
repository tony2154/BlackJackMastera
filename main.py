import sys
import os
import time
from PyQt5.QtWidgets import QApplication
from utils.capture import capture_table
from utils.card_detector import detect_cards, compute_hilo
from utils.ui_overlay import OverlayWidget
from config import LOG_FOLDER


try:
    from config import BET_ALERT_THRESHOLD
except ImportError:
    BET_ALERT_THRESHOLD = 3


os.makedirs(LOG_FOLDER, exist_ok=True)

def decide_advice(running_count, min_bet=20, max_bet=100):
    """Regla simple de apuestas basada en running_count."""
    if running_count >= 5:
        return f"🔥 Cuenta alta ({running_count}) — Aumentar apuesta"
    elif running_count >= 3:
        return f"▲ Cuenta favorable ({running_count}) — Subir apuesta moderada"
    elif running_count <= -4:
        return f"⚠️ Cuenta muy baja ({running_count}) — Reducir apuesta"
    else:
        return f"🔹 Cuenta neutral ({running_count}) — Jugar normal"

def main_loop(app, overlay):
    running_count = 0
    last_save = time.time()

    while True:
        frame = capture_table()
        detected = detect_cards(frame)
        delta = compute_hilo(detected)
        running_count += delta

        advice = decide_advice(running_count)
        overlay.update(running_count, advice, detected)

        # Guardado periódico de logs
        if time.time() - last_save > 5:
            log_path = os.path.join(LOG_FOLDER, f"log_{int(time.time())}.txt")
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"{time.ctime()}  Count={running_count}  Detected={detected}\n")
            last_save = time.time()

        # Procesar eventos Qt
        app.processEvents()
        time.sleep(0.5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWidget()
    overlay.move(40, 40)  # mover a esquina superior izquierda, ajusta si quieres
    overlay.show()
    try:
        main_loop(app, overlay)
    except KeyboardInterrupt:
        print("Saliendo...")
        sys.exit(0)
