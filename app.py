from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ""

    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Ao menos um tipo de caractere deve ser selecionado para gerar a senha.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = None
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 12))
        maiusculas = "maiusculas" in request.form
        minusculas = "minusculas" in request.form
        numeros = "numeros" in request.form
        simbolos = "simbolos" in request.form
        
        senha_gerada = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)

    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)
