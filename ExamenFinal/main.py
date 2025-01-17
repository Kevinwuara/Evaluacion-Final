from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if edad >= 18 and edad <= 30:
            descuento = 0.15 * total_sin_descuento
        elif edad > 30:
            descuento = 0.25 * total_sin_descuento
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               descuento=descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html', total_sin_descuento=None)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'Juan': 'admin',
        'Pepe': 'user'
    }
    mensaje = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == 'Juan':
                mensaje = f'Bienvenido administrador {nombre}'
            else:
                mensaje = f'Bienvenido usuario {nombre}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)






