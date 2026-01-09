from flask import Flask

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

if __name__ == '__main__':
    app.run(debug=True)