from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo = titulo, listado = listado)

@app.route('/calculos', methods=['GET','POST'])
def calculos():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        opc = request.form['operacion']
        if opc == 'suma':
            res = int(numero1) + int(numero2)

        if opc == 'resta':
            res = int(numero1) - int(numero2)

        if opc == 'multiplicacion':
            res = int(numero1) * int(numero2)

        if opc == 'division':
            res = int(numero1) / int(numero2)

        return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)
    return render_template('calculos.html')

@app.route('/distancia', methods=['GET','POST'])
def distancia():
    if request.method == 'POST':
        x1 = request.form['x1']
        y1 = request.form['y1']
        x2 = request.form['x2']
        y2 = request.form['y2']

        fx1 = float(x1)
        fy1 = float(y1)
        fx2 = float(x2)
        fy2 = float(y2)

        dx = fx2 - fx1
        dy = fy2 - fy1

        res = math.sqrt(dx**2 + dy**2)

        return render_template('distancia.html', res=res, x1=x1, y1=y1, x2=x2, y2=y2)
    return render_template('distancia.html')

@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    email=""
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
        
    return render_template('Alumnos.html', form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)


@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:num>')
def about(num):
    return f"El numero es: {num}"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID {} nombre: {}".format(id,username);

@app.route('/suma/<float:n1>/<float:n2>')
def func1(n1,n2):
    return "lasuma es: {}".format(n1,n2);


@app.route('/default')
@app.route('/default/<string:dft>')
def func2(dft='sss'):
    return "El valor de dft es: "+ dft


@app.route('/prueba')
def func3():
    return '''
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
            <title>Pagina de prueba </title>
        </head>
        <body>
            <h1>Hola esta es una pagina de prueba</h1>
            <p> Esta pagina es para probar el retorno de HTML en Flask</p>
        </body>
    </html>
'''

if __name__ == '__main__':
    app.run(debug=True)