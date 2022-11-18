from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/tabla_obra')
def tabla_obra():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obra, descripcion, autor, lugar_elab, valor, ubicacion from tabla_pintura order by id')
    datos = cursor.fetchall()
    return render_template("tabla_obra.html", nombre_obra = datos)



@app.route('/fdetalle/<string:id>', methods=['GET'])
def fdetalle(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obra, descripcion, autor, lugar_elab, valor, ubicacion from tabla_pintura where id = %s', (id))
    dato = cursor.fetchall()
    return render_template("fdetalle.html", nombre_obra=dato[0], dat=dato[0])

##

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obra, descripcion, autor, lugar_elab, valor, ubicacion from tabla_pintura where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", nombre_obra=dato[0])


@app.route('/editar_obra/<string:id>',methods=['POST'])
def editar_nombre_obra(id):
    if request.method == 'POST':

        nombre_obra=request.form['nombre_obra']
        descripcion=request.form['descripcion']
        autor=request.form['autor']
        lugar_elab=request.form['lugar_elab']
        valor=request.form['valor']
        ubicacion=request.form['ubicacion']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('update tabla_pintura set nombre_obra=%s, descripcion=%s, autor=%s, lugar_elab=%s, valor=%s, ubicacion=%s where id=%s', (nombre_obra,descripcion,autor,lugar_elab,valor,ubicacion,id))
        conn.commit()
    return redirect(url_for('tabla_obra'))



@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('delete from tabla_pintura where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tabla_obra'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/agrega_obra', methods=['POST'])
def agrega_obra():
    if request.method == 'POST':

        nombre_obra = request.form['nombre_obra']
        descripcion = request.form['descripcion']
        autor = request.form['autor']
        lugar_elab = request.form['lugar_elab']
        valor = request.form['valor']
        ubicacion = request.form['ubicacion']


        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('insert into tabla_pintura (nombre_obra,descripcion,autor,lugar_elab,valor,ubicacion) values (%s, %s, %s, %s, %s, %s)',(nombre_obra, descripcion, autor, lugar_elab, valor, ubicacion))
        conn.commit()
    return redirect(url_for('tabla_obra'))

#Clientes
@app.route('/clientes')
def clientes():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombreCliente, apellido, telefono, email, obraInteres, direccion from cliente order by id')
    datos = cursor.fetchall()
    return render_template("clientes.html", nombre_clientes  = datos)

@app.route('/agrega_cliente', methods=['POST'])
def agrega_cliente():
    if request.method == 'POST':

        nombreC = request.form['nombreC']
        apellido = request.form['apellido']
        tel = request.form['tel']
        email = request.form['email']
        obraIn = request.form['obraIn']
        dir = request.form['dir']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombreCliente, apellido, telefono, email, obraInteres, direccion) values (%s, %s, %s, %s, %s, %s)',(nombreC, apellido, tel, email, obraIn, dir))
        conn.commit()
    return redirect(url_for('tablaCliente'))


@app.route('/Cdetalle/<string:id>', methods=['GET'])
def Cdetalle(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombreCliente, apellido, telefono, email, obraInteres, direccion from cliente where id = %s', (id))
    dato = cursor.fetchall()
    return render_template("clientesD.html", cliente=dato[0], dat=dato[0])

@app.route('/editarC/<string:id>')
def editarC(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombreCliente, apellido, telefono, email, obraInteres, direccion from cliente where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("clienteEd.html", cliente=dato[0])


@app.route('/CeditarF/<string:id>',methods=['POST'])
def CeditarF(id):
    if request.method == 'POST':
        nombreC = request.form['nombreC']
        apellido = request.form['apellido']
        tel = request.form['tel']
        email = request.form['email']
        obraIn = request.form['obraIn']
        dir = request.form['dir']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('update cliente set nombreCliente=%s, apellido=%s, telefono=%s, email=%s, obraInteres=%s, direccion=%s where id=%s', (nombreC,apellido,tel,email,obraIn,dir,id))
        conn.commit()
    return redirect(url_for('tablaCliente'))

@app.route('/tablaCliente')
def tablaCliente():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('select id, nombreCliente, apellido, telefono, email, obraInteres, direccion from cliente order by id')
    datos = cursor.fetchall()
    return render_template("tablaCli.html", cliente = datos)

@app.route('/Cborrar/<string:id>')
def Cborrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('delete from cliente where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tablaCliente'))


################tabla_subasta




@app.route('/formulario_subasta')
def formulario_subasta():
    return render_template("formulario_subasta.html")


@app.route('/tabla_subasta')
def tabla_subasta():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')#cambiar la base de datos
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obr, nombre, valor, hora_inicio, hora_fin, autor, juez from tabla_subasta order by id')
    datos = cursor.fetchall()
    return render_template("tabla_subasta.html", nombre_obr = datos)


@app.route('/fdetalle_subasta/<string:id>', methods=['GET'])
def fdetalle_subasta(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')#cambiar la base de datos
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obr, nombre, valor, hora_inicio, hora_fin, autor, juez from tabla_subasta where id = %s', (id))
    dato = cursor.fetchall()

    return render_template("fdetalle_subasta.html", nombre_obr=dato[0], dat=dato[0])



@app.route('/editar3/<string:id>')
def editar3(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte') #cambiar la base de datos
    cursor = conn.cursor()
    cursor.execute('select id, nombre_obr, nombre, valor, hora_inicio, hora_fin, autor, juez from tabla_subasta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar_subasta.html", nombre_obr=dato[0])


@app.route('/editar_subasta/<string:id>',methods=['POST'])
def editar_subasta(id):
    if request.method == 'POST':

        nombre_obr=request.form['nombre_obra']
        nombre=request.form['nombre']
        valor=request.form['valor']
        hora_inicio=request.form['hora_inicio']
        hora_fin=request.form['hora_fin']
        autor=request.form['autor']
        juez=request.form['juez']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('update tabla_subasta set nombre_obr=%s, nombre=%s, valor=%s, hora_inicio=%s, hora_fin=%s, autor=%s, juez=%s where id=%s', (nombre_obr,nombre,valor,hora_inicio,hora_fin,autor,juez,id))
        conn.commit()
    return redirect(url_for('tabla_subasta'))



@app.route('/borrar3/<string:id>')
def borrar3(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
    cursor = conn.cursor()
    cursor.execute('delete from tabla_subasta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tabla_subasta'))



@app.route('/agrega_subasta', methods=['POST'])
def agrega_subasta():
    if request.method == 'POST':

        nombre_obr=request.form['nombre_obra']
        nombre=request.form['nombre']
        valor=request.form['valor']
        hora_inicio=request.form['hora_inicio']
        hora_fin=request.form['hora_fin']
        autor=request.form['autor']
        juez=request.form['juez']



        conn = pymysql.connect(host='localhost', user='root', passwd='', db='arte')
        cursor = conn.cursor()
        cursor.execute('insert into tabla_subasta (nombre_obr, nombre, valor, hora_inicio, hora_fin, autor, juez) values (%s, %s, %s, %s, %s, %s, %s)',(nombre_obr,nombre,valor,hora_inicio,hora_fin,autor,juez))
        conn.commit()
    return redirect(url_for('tabla_subasta'))









if __name__ == "__main__":
    app.run(debug=True)
