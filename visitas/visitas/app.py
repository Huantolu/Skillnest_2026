from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    if 'contador' not in session:
        session['contador'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0
    session['contador'] += 1

    return render_template(
        'index.html',
        visitas = session['contador'],
        reinicios = session['reinicios']
    )

@app.route ('/sumar_dos', methods = ['POST'])
def sumar_dos():
    session['contador'] += 2
    return redirect('/')

@app.route('/sumar_personalizado', methods = ['POST'])
def sumar_personalizado():
    numero = int(request.form['numero'])
    session['contador'] += numero
    return redirect('/')

@app.route('/reiniciar', methods = ['POST'])
def reiniciar():
    session['contador'] = 0
    session['reinicios'] += 1
    return redirect('/')

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)