import time
from turtle import Turtle, Screen
import pandas as pd

IMAGE_PATH = "02-intermediate/25-Day-Pandas/Argentina_Project/map.gif"
CSV_PATH = "02-intermediate/25-Day-Pandas/Argentina_Project/provincias_argentinas.csv"

# -- Screen Configuration --
sc = Screen()
sc.bgpic(IMAGE_PATH)
sc.setup(860, 1175)
sc.title("Provincias Argentinas")

# -- Data-frame Initialize --
df = pd.read_csv(CSV_PATH)
df["provincia"] = df.provincia.str.lower()

# -- Writer config --
writer = Turtle()
writer.penup()
writer.color("black")
writer.hideturtle()

# -- Game Config --
game_on = True
correct_count = 0
answered_provincias = []

while correct_count < 50:
    provincia = sc.textinput(f"{correct_count}/23 provincias", "What's another provincia? (type 'Exit' to stop)")
    if provincia is None:
        break
    provincia_lower = provincia.strip().lower()
    if provincia_lower == "exit":
        break
    if provincia_lower == "":
        continue
    if provincia_lower in answered_provincias:
        continue

    result = df[df.provincia == provincia_lower]
    if not result.empty:
        row = result.iloc[0]
        try:
            x_cor = int(row.x)
            y_cor = int(row.y)
        except Exception:
            x_cor = float(row.x)
            y_cor = float(row.y)
        writer.goto(x_cor, y_cor)
        writer.write(row.provincia.title(), align="center", font=("Arial", 8, "normal"))
        answered_provincias.append(provincia_lower)
        correct_count += 1

sc.mainloop()