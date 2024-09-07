from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>En esta pagina podras ver unos cuantos datos interesantes de fútbol!</h1>
    <a href="/random_fact">¡Ver un hecho al azar!</a>
    """
@app.route("/random_fact")
def random_fact():
    facts_list = [
        "La competición de fútbol más antigua del mundo es la FA Cup inglesa fundada por C.W. Alcock en 1872.",
        "En China, los primeros balones de fútbol se fabricaban con ropa cosida que se rellenaba con basura.",
        "El idolo de Endrick (el nuevo jugador del Real Madrid) es el legendario Bobby Charlton.",
        "Sabes que Di Esteffano es el unico jugador en ganar un super balon de oro.",
        "Sabias que Messi es mejor que Cristiano 💀."
    ]
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)