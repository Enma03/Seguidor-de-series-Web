from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    series = [
        {"series_id": 1, "nombre": "JoJo's Bizarre Adventure", "img_path": "img/jojo.webp", "prox_cap": "2025-05-01"},
        {"series_id": 2, "nombre": "Girls und Panzer", "img_path": "img/GirlsP.jpg", "prox_cap": "2025-05-03"},
    ]
    return render_template("index.html", series=series, followed_series=series)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/serie/<int:series_id>")
def serie(series_id):
    if series_id == 1:
        serie = {
            "series_id": 1,
            "nombre": "JoJo's Bizarre Adventure",
            "descripcion": "Las bizarras aventuras de mis compas los Joestar.",
            "cant_cap": 26,
            "prox_cap": "2025-05-01",
            "img_path": "img/jojo.webp"
        }
    elif series_id == 2:
        serie = {
            "series_id": 2,
            "nombre": "Girls und Panzer",
            "descripcion": "Niñas colegialas en tanques de guerra militar.",
            "cant_cap": 12,
            "prox_cap": "2025-05-03",
            "img_path": "img/GirlsP.jpg"
        }
    else:
        serie = {
            "series_id": 0,
            "nombre": "Serie no encontrada",
            "descripcion": "No hay información disponible.",
            "cant_cap": 0,
            "prox_cap": "N/A",
            "img_path": ""
        }

    return render_template("serie.html", serie=serie)

if __name__ == "__main__":
    app.run(debug=True)
