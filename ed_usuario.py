from tkinter import *
from tkinter import ttk
from conecta_bd import *

def manipula_usuarios():

    pantalla_user = Toplevel()
    pantalla_user.geometry("900x400")
    pantalla_user.config(bg="light sky blue")
    pantalla_user.title("Catalogo Usuarios")

    str_nombre = StringVar()
    str_user = StringVar()
    str_pass = StringVar()

    datos = ()

    # -------------------------
    # TREEVIEW
    # -------------------------
    marco = Frame(pantalla_user)
    marco.place(x=20,y=150)

    ver_sb = ttk.Scrollbar(marco, orient="vertical")
    ver_sb.pack(side=RIGHT, fill=Y)

    tabla = ttk.Treeview(
        marco,
        columns=("col1","col2","col3"),
        yscrollcommand=ver_sb.set
    )

    tabla.column("#0", width=100)
    tabla.column("col1", width=200)
    tabla.column("col2", width=200)
    tabla.column("col3", width=200)

    tabla.heading("#0", text="ID")
    tabla.heading("col1", text="Nombre")
    tabla.heading("col2", text="Usuario")
    tabla.heading("col3", text="Password")

    tabla.pack()

    ver_sb.config(command=tabla.yview)

    # -------------------------
    # RECUPERAR
    # -------------------------
    def recupera_db():

        for record in tabla.get_children():
            tabla.delete(record)

        usuarios = tabla_usuarios()

        for usu in usuarios:

            tabla.insert(
                parent="",
                index="end",
                iid=usu[0],
                text=str(usu[0]),
                values=(
                    str(usu[1]),
                    str(usu[2]),
                    str(usu[3])
                )
            )

    # -------------------------
    # AGREGAR
    # -------------------------
    def agrega_usuario():

        inserta_usuario(
            str_nombre.get(),
            str_user.get(),
            str_pass.get()
        )

        recupera_db()

    # -------------------------
    # BORRAR
    # -------------------------
    def borrar_usuario():

        ab = tabla.selection()[0]

        borra_usuario(ab)

        recupera_db()

    # -------------------------
    # SELECCIONAR
    # -------------------------
    def seleccionar_usuario():

        nonlocal datos

        ab = tabla.selection()[0]

        datos = selec_usuario(ab)

        str_nombre.set(datos[1])
        str_user.set(datos[2])
        str_pass.set(datos[3])

    # -------------------------
    # MODIFICAR
    # -------------------------
    def modificar_usuario():

        ab = tabla.selection()[0]

        modif_usuario(
            ab,
            str_nombre.get(),
            str_user.get(),
            str_pass.get()
        )

        recupera_db()

    recupera_db()

    # -------------------------
    # LABELS
    # -------------------------
    Label(pantalla_user,text="Nombre",bg="light sky blue").place(x=20,y=20)
    Label(pantalla_user,text="Usuario",bg="light sky blue").place(x=20,y=60)
    Label(pantalla_user,text="Password",bg="light sky blue").place(x=20,y=100)

    # -------------------------
    # ENTRYS
    # -------------------------
    Entry(pantalla_user,textvariable=str_nombre,width=40).place(x=100,y=20)
    Entry(pantalla_user,textvariable=str_user,width=40).place(x=100,y=60)
    Entry(pantalla_user,textvariable=str_pass,width=40).place(x=100,y=100)

    # -------------------------
    # BOTONES
    # -------------------------
    Button(
        pantalla_user,
        text="Agregar",
        command=agrega_usuario,
        bg="green",
        fg="white"
    ).place(x=500,y=20)

    Button(
        pantalla_user,
        text="Modificar",
        command=modificar_usuario,
        bg="blue",
        fg="white"
    ).place(x=500,y=60)

    Button(
        pantalla_user,
        text="Eliminar",
        command=borrar_usuario,
        bg="red",
        fg="white"
    ).place(x=500,y=100)

    Button(
        pantalla_user,
        text="Seleccionar",
        command=seleccionar_usuario,
        bg="black",
        fg="white"
    ).place(x=600,y=20)