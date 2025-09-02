import pyautogui
print("Coloca el mouse en la esquina superior izquierda de la mesa y presiona Enter")
input()
x1, y1 = pyautogui.position()
print(f"Top-left = {x1},{y1}")

print("Coloca el mouse en la esquina inferior derecha de la mesa y presiona Enter")
input()
x2, y2 = pyautogui.position()
print(f"Bottom-right = {x2},{y2}")

w = x2 - x1
h = y2 - y1
print("Región:", (x1, y1, w, h))

with open("config.py", "a", encoding="utf-8") as f:
    f.write(f"\n# AUTO REGION\nGAME_REGION = ({x1}, {y1}, {w}, {h})\n")
print("Guardado en config.py (append). Revisa el archivo y ajusta si es necesario.")
