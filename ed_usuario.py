from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conecta_bd import *

def manipula_usuarios():

    pantalla_user = Toplevel()
    pantalla_user.geometry("900x450")
    pantalla_user.config(bg="light sky blue")
    pantalla_user.title("Catalogo Usuarios")
    pantalla_user.resizable(False, False)

    str_nombre = StringVar()
    str_user = StringVar()
    str_pass = StringVar()

    # -------------------------
    # TREEVIEW
    # -------------------------
    marco = Frame(pantalla_user, width=850, height=250)
    marco.place(x=20, y=150)

    ver_sb = ttk.Scrollbar(marco, orient="vertical")
    ver_sb.pack(side=RIGHT, fill=Y)

    tabla = ttk.Treeview(
        marco,
        columns=("col1", "col2", "col3"),
        yscrollcommand=ver_sb.set
    )

    tabla.column("#0", width=80)
    tabla.column("col1", width=220)
    tabla.column("col2", width=220)
    tabla.column("col3", width=220)

    tabla.heading("#0", text="ID")
    tabla.heading("col1", text="Nombre")
    tabla.heading("col2", text="Usuario")
    tabla.heading("col3", text="Password")

    tabla.pack(fill=BOTH, expand=True)

    ver_sb.config(command=tabla.yview)

    # -------------------------
    # LIMPIAR CAMPOS
    # -------------------------
    def limpiar():

        str_nombre.set("")
        str_user.set("")
        str_pass.set("")

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

        if (
            str_nombre.get() == "" or
            str_user.get() == "" or
            str_pass.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "Completa todos los campos"
            )

            return

        inserta_usuario(
            str_nombre.get(),
            str_user.get(),
            str_pass.get()
        )

        recupera_db()
        limpiar()

    # -------------------------
    # BORRAR
    # -------------------------
    def borrar_usuario():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Selecciona un usuario"
            )

            return

        ab = seleccion[0]

        borra_usuario(ab)

        recupera_db()
        limpiar()

    # -------------------------
    # SELECCIONAR
    # -------------------------
    def seleccionar_usuario():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Selecciona un usuario"
            )

            return

        ab = seleccion[0]

        datos = selec_usuario(ab)

        str_nombre.set(datos[1])
        str_user.set(datos[2])
        str_pass.set(datos[3])

    # -------------------------
    # MODIFICAR
    # -------------------------
    def modificar_usuario():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Selecciona un usuario"
            )

            return

        ab = seleccion[0]

        modif_usuario(
            ab,
            str_nombre.get(),
            str_user.get(),
            str_pass.get()
        )

        recupera_db()
        limpiar()

    recupera_db()

    # -------------------------
    # LABELS
    # -------------------------
    Label(
        pantalla_user,
        text="Nombre",
        bg="light sky blue",
        font=("Arial", 12)
    ).place(x=20, y=20)

    Label(
        pantalla_user,
        text="Usuario",
        bg="light sky blue",
        font=("Arial", 12)
    ).place(x=20, y=60)

    Label(
        pantalla_user,
        text="Password",
        bg="light sky blue",
        font=("Arial", 12)
    ).place(x=20, y=100)

    # -------------------------
    # ENTRYS
    # -------------------------
    Entry(
        pantalla_user,
        textvariable=str_nombre,
        width=40
    ).place(x=120, y=20)

    Entry(
        pantalla_user,
        textvariable=str_user,
        width=40
    ).place(x=120, y=60)

    Entry(
        pantalla_user,
        textvariable=str_pass,
        width=40
    ).place(x=120, y=100)

    # -------------------------
    # BOTONES
    # -------------------------
    Button(
        pantalla_user,
        text="Agregar",
        command=agrega_usuario,
        bg="green",
        fg="white",
        width=12
    ).place(x=500, y=20)

    Button(
        pantalla_user,
        text="Modificar",
        command=modificar_usuario,
        bg="blue",
        fg="white",
        width=12
    ).place(x=500, y=60)

    Button(
        pantalla_user,
        text="Eliminar",
        command=borrar_usuario,
        bg="red",
        fg="white",
        width=12
    ).place(x=500, y=100)

    Button(
        pantalla_user,
        text="Seleccionar",
        command=seleccionar_usuario,
        bg="black",
        fg="white",
        width=12
    ).place(x=650, y=20)