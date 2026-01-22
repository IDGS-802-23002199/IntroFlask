from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS-802-Flask"
    lista=['Pedro','Juan','Luis','Ana']
    return render_template('index.html',titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/hola')
def hola():
    return "hola, Hola!"

@app.route('/user/<string:user>')
def user(user):
    return "Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<string:username>')
def username(id, username):
    return "ID: {} Username: {}".format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1,n2):
    return "la suma es: {}".format(n1+n2)

@app.route("/default/")
@app.route("/default/<string:name>")
def default(name="pedro"):
    return "Hola, {}".format(name)

@app.route("/operas")
def operas():
    return '''
            <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="name">apaterno:</label>
            <input type="text" id="name" name="name" required>
            </form>
            '''
            
@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    res = None
    n1 = n2 = operacion = None

    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            res = n1 + n2
        elif operacion == "resta":
            res = n1 - n2
        elif operacion == "multiplicacion":
            res = n1 * n2
        elif operacion == "division":
            if n2 != 0:
                res = n1 / n2
            else:
                res = "Error: división entre cero"

    return render_template(
        "operasBas.html",
        n1=n1,
        n2=n2,
        res=res,
        operacion=operacion
    )

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    return f"la suma es: {float(n1)+float(n2)}"

if __name__ == '__main__':
    app.run(debug=True)