from pathlib import Path
from turtle import Turtle, Screen
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "map.gif"
CSV_PATH = BASE_DIR / "provincias_argentinas.csv"

# -- Screen Configuration --
sc = Screen()
sc.bgpic(str(IMAGE_PATH))
sc.setup(width=860, height=1175)
sc.title("Provincias Argentinas")

# -- Data-frame Initialize --
df = pd.read_csv(CSV_PATH)
df["provincia_original"] = df["provincia"]
df["provincia"] = df["provincia"].str.strip().str.lower()

# -- Writer config --
writer = Turtle()
writer.penup()
writer.color("black")
writer.hideturtle()

# -- Game Config --
answered_provincias = []
total_provincias = len(df)

while len(answered_provincias) < total_provincias:
    provincia = sc.textinput(
        f"{len(answered_provincias)}/{total_provincias} provincias",
        "What's another provincia? (type 'Exit' to stop)"
    )
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
        writer.write(row.provincia_original, align="center", font=("Arial", 8, "normal"))
        answered_provincias.append(provincia_lower)

sc.mainloop()