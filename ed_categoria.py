from tkinter import *
from tkinter import ttk
from conecta_bd import *
from ed_pregunta import *

def manipula_categorias():

    pantalla_cat = Toplevel()
    pantalla_cat.resizable(1,1)
    pantalla_cat.geometry("750x350")
    pantalla_cat.config(background="light sky blue")
    pantalla_cat.title("catalogo de categorias")

    str_cat = StringVar()
    datos = ()

    marco_per = Frame(pantalla_cat)
    marco_per.pack()
    marco_per.place(x=20, y=100)

    ver_sb = ttk.Scrollbar(marco_per, orient="vertical")
    ver_sb.pack(side=RIGHT, fill=Y)

    Tabl_cat = ttk.Treeview(
        marco_per,
        columns=("col1",),
        yscrollcommand=ver_sb.set
    )

    Tabl_cat.column("#0", width=155)
    Tabl_cat.column("col1", width=500)

    Tabl_cat.heading("#0", text="id_categoria")
    Tabl_cat.heading("col1", text="Descripcion")

    Tabl_cat.pack()

    ver_sb.config(command=Tabl_cat.yview)

    # ----------------------------
    # RECUPERA DATOS
    # ----------------------------
    def recupera_db():

        for record in Tabl_cat.get_children():
            Tabl_cat.delete(record)

        categs = tabla_categorias()

        for categ in categs:
            Tabl_cat.insert(parent="",index="end",iid=categ[0],text=str(categ[0]),values=(str(categ[1]).replace(' ','_'),))

    # ----------------------------
    # AGREGA
    # ----------------------------
    def agrega_cat():

        inserta_categoria(str_cat.get())
        recupera_db()

    # ----------------------------
    # BORRA
    # ----------------------------
    def borra_catsel():

        ab = Tabl_cat.selection()[0]
        borra_categoria(ab)
        recupera_db()

    # ----------------------------
    # SELECCIONA
    # ----------------------------
    def select_cat():
        nonlocal datos
        ab = Tabl_cat.selection()[0]
        datos = selec_categoria(ab)
        print(datos)
        str_cat.set(datos[1])

    # ----------------------------
    # MODIFICA
    # ----------------------------
    def modif_catsel():

        ab = Tabl_cat.selection()[0]

        modif_categoria(ab, str_cat.get())

        recupera_db()

    # ----------------------------
    # EDITA PREGUNTAS
    # ----------------------------
    def edita_pregunta():

        print(datos)
        manipula_pregunta(datos)

    recupera_db()

    # ----------------------------
    # LABEL
    # ----------------------------
    et = Label(
        pantalla_cat,
        text="Categoria",
        bg="Light Sky Blue",
        font='Helvetica 14 bold'
    )

    et.place(x=20, y=20)

    # ----------------------------
    # ENTRY
    # ----------------------------
    pre = Entry(
        pantalla_cat,
        textvariable=str_cat,
        font='Helvetica 14 bold',
        bg="Lavender",
        width=50
    )

    pre.place(x=120, y=20)

    # ----------------------------
    # BOTONES
    # ----------------------------
    Button(
        pantalla_cat,
        text="Preguntas",
        command=edita_pregunta,
        fg="white",
        bg="red4",
        font='Arial 12'
    ).place(x=690, y=20)

    Button(
        pantalla_cat,
        text="Agregar categorias",
        command=agrega_cat,
        fg="white",
        bg="red4",
        font='Arial 12'
    ).place(x=10, y=60)

    Button(
        pantalla_cat,
        text="Modifica categoria",
        command=modif_catsel,
        fg="white",
        bg="red4",
        font="Arial 12",
        width=20
    ).place(x=180, y=60)

    Button(
        pantalla_cat,
        text="Borrar categoria",
        command=borra_catsel,
        fg="white",
        bg="red4",
        font="Arial 12",
        width=20
    ).place(x=390, y=60)

    Button(
        pantalla_cat,
        text="Selecciona Categoria",
        command=select_cat,
        fg="white",
        bg="red4",
        font="Arial 12",
        width=20
    ).place(x=580, y=60)