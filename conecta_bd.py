import pymysql

def recupera_categorias():
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("select descripcion from categoria")
    categoria=cursor.fetchall()
    conn.close()
    return categoria

def recupera_preguntas(cat):

    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="ignorancia"
    )

    cursor = conn.cursor()

    consulta = """
    SELECT
        p.id_pregunta,
        p.pregunta,
        p.opcion_1,
        p.opcion_2,
        p.opcion_3,
        p.opcion_4,
        p.correcto,
        p.id_categoria
    FROM pregunta p
    INNER JOIN categoria c
        ON p.id_categoria = c.id_categoria
    WHERE c.descripcion = %s
    """

    cursor.execute(consulta, (cat,))
    preguntas = cursor.fetchall()

    conn.close()

    return preguntas


def tabla_categorias():
    conn=pymysql.connect(host="localhost", user="root", passwd="", db="ignorancia")
    cursor = conn.cursor()
    cursor.execute("select id_categoria,descripcion from categoria")
    cats=cursor.fetchall()
    conn.close()
    return cats

def inserta_categoria(descrip):
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("insert into categoria (descripcion) values(%s)", (descrip))
    conn.commit()
    conn.close()


def borra_categoria(ab):
    conn = pymysql.connect(host="localhost", user="root",passwd="", db="ignorancia")
    cursor = conn.cursor()
    cursor.execute("delete from categoria where id_categoria=%s",(ab))
    conn.commit()
    conn.close()

def selec_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('SELECT id_categoria, descripcion FROM categoria WHERE id_categoria = %s', (ab))
	dato=cursor.fetchone()
	return dato

def modif_categoria(ab,descripcion):
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("update categoria set descripcion=%s WHERE id_categoria=%s",(descripcion,ab))
    conn.commit()
    conn.close()

def tabla_preguntas(id):
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("select id_pregunta,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria from pregunta where id_categoria=%s",(id))
    preguntas=cursor.fetchall()
    conn.close()
    return preguntas

def selec_preguntas(ab):

    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="ignorancia"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id_pregunta,
            pregunta,
            opcion_1,
            opcion_2,
            opcion_3,
            opcion_4,
            correcto,
            id_categoria
        FROM pregunta
        WHERE id_pregunta=%s
        """,
        (ab,)
    )

    dato = cursor.fetchone()

    conn.close()

    return dato

def modif_pregunta(ab,datos):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('update pregunta set pregunta=%s,opcion_1=%s,opcion_2=%s,opcion_3=%s,opcion_4=%s,correcto=%s where Id_pregunta=%s',
    (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
	conn.commit()
def borra_pregunta(ab):
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("delete from pregunta where id_pregunta=%s",(ab))
    conn.commit()
    conn.close()

def inserta_pregunta(datos,id):
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("insert into pregunta(pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria)values(%s,%s,%s,%s,%s,%s,%s)",(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
    conn.commit()
    conn.close()

def conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ignorancia"
    )

# -------------------------
# MOSTRAR
# -------------------------
def tabla_usuarios():

    con = conexion()
    cur = con.cursor()

    sql = "SELECT * FROM usuarios"

    cur.execute(sql)

    datos = cur.fetchall()

    con.close()

    return datos

# -------------------------
# INSERTAR
# -------------------------
def inserta_usuario(nombre, usuario, password):

    con = conexion()
    cur = con.cursor()

    sql = """
    INSERT INTO usuarios(nombre,usuario,password)
    VALUES(%s,%s,%s)
    """
    cur.execute(sql,(nombre,usuario,password))

    con.commit()
    con.close()

# -------------------------
# BORRAR
# -------------------------
def borra_usuario(idu):

    con = conexion()
    cur = con.cursor()
    sql = "DELETE FROM usuarios WHERE id_usuario=%s"
    cur.execute(sql,(idu))
    con.commit()
    con.close()

# -------------------------
# SELECCIONAR
# -------------------------
def selec_usuario(idu):
    con = conexion()
    cur = con.cursor()
    sql = "SELECT * FROM usuarios WHERE id_usuario=%s"
    cur.execute(sql,(idu))
    datos = cur.fetchone()
    con.close()

    return datos

# -------------------------
# MODIFICAR
# -------------------------
def modif_usuario(idu,nombre,usuario,password):

    con = conexion()
    cur = con.cursor()

    sql = """
    UPDATE usuarios
    SET nombre=%s,
        usuario=%s,
        password=%s
    WHERE id_usuario=%s
    """

    cur.execute(sql,(nombre,usuario,password,idu))

    con.commit()
    con.close()