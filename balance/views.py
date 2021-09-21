from balance import app

@app.route("/")
def inicio():
    return "Pagina de inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Pagina de alta de movimiento"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Pagina de borrado de {id}"