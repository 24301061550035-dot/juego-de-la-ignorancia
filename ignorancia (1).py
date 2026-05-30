import random
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conecta_bd import *
import conecta_bd
from ed_categoria import *
from ed_usuario import *
from PIL import Image, ImageTk

pant = Tk()
pant.title("Juego de la ignorancia-BD")

# ---------------- PANTALLA ----------------
ancho = pant.winfo_screenwidth()
alto = 1080
pant.geometry(f"{ancho}x{alto}")
pant.resizable(True, True)
# escala general
escalar = ancho / 1920

x1 = 10
x2 = 10
x3 = 10
x4 = 10
y_j1 = 500
y_j2 = 600
y_j3 = 700
y_j4 = 830

# ---------------- FONDO ----------------
img = Image.open(r"./imagen/luffy.png")
img = img.resize((ancho, alto))
fon = ImageTk.PhotoImage(img)
canvas = Canvas(pant, width=ancho, height=alto, highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=fon, anchor="nw")

# ---------------- VARIABLES ----------------
selection = ()
str_preg = StringVar()
str_res1 = StringVar()
str_res2 = StringVar()
str_res3 = StringVar()
str_res4 = StringVar()
str_sig = StringVar()
correcto = 0
turno = 1

# ---------------- FUNCIONES ----------------
def avanza_jug():
    global x1, x2, x3
    avance = canvas.winfo_width() * 0.05
    if turno == 1:
        x1 += avance
        canvas.coords(j1, x1, y_j1)
    elif turno == 2:
        x2 += avance
        canvas.coords(j2, x2, y_j2)
    elif turno == 3:
        x3 += avance
        canvas.coords(j3, x3, y_j3)

def mover_ignorancia():
    global x4
    avance = canvas.winfo_width() * 0.05
    x4 += avance
    canvas.coords(j4, x4, y_j4)

def siguiente_turno():
    global turno
    turno += 1
    if turno > 3:
        turno = 1
    str_sig.set(f"Turno del jugador {turno}")

def desactivar_botones():
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)

def activar_botones():
    r1.config(state=NORMAL)
    r2.config(state=NORMAL)
    r3.config(state=NORMAL)
    r4.config(state=NORMAL)

def opc1():
    desactivar_botones()
    if correcto == 1:
        avanza_jug()
    else:
        mover_ignorancia()
    siguiente_turno()

def opc2():
    desactivar_botones()
    if correcto == 2:
        avanza_jug()
    else:
        mover_ignorancia()
    siguiente_turno()

def opc3():
    desactivar_botones()
    if correcto == 3:
        avanza_jug()
    else:
        mover_ignorancia()
    siguiente_turno()

def opc4():
    desactivar_botones()
    if correcto == 4:
        avanza_jug()
    else:
        mover_ignorancia()
    siguiente_turno()

def sel_preg():
    global correcto
    tam = len(selection)
    if tam != 0:
        n = random.randint(0, tam - 1)
        str_preg.set(selection[n][1])
        str_res1.set(selection[n][2])
        str_res2.set(selection[n][3])
        str_res3.set(selection[n][4])
        str_res4.set(selection[n][5])
        correcto = selection[n][6]
        activar_botones()
    else:
        str_preg.set("Categoría sin preguntas")
        str_res1.set("")
        str_res2.set("")
        str_res3.set("")
        str_res4.set("")
        desactivar_botones()
    pant.update()

def preguntas(event):
    global selection
    cat = event.widget.get()
    selection = recupera_preguntas(cat)
    sel_preg()

def pregunta_sig():
    global selection
    cat = categorias.get()
    selection = recupera_preguntas(cat)
    sel_preg()

def mani_cats():
    manipula_categorias()

def ganar():
    meta = canvas.winfo_width() * 0.90

    if x1 >= meta or x2 >= meta or x3 >= meta:
        messagebox.showinfo("Alguien gano el juego :D")
    if x4 >= meta:
        messagebox.showerror("GANO LA IGNORANCIA D:")


# ---------------- CATEGORIAS ----------------
cats = conecta_bd.recupera_categorias()
eti = Label(pant, text="Categoría", font=("Arial", int(18 * escalar)), bg="white")
eti.place(x=10, y=10)
categorias = ttk.Combobox(pant, font=("Arial", int(18 * escalar)))
categorias["values"] = cats
categorias.place(x=150, y=10)
categorias.bind("<<ComboboxSelected>>", preguntas)

# ---------------- BOTONES ----------------
btn_sig = Button(pant, text="Siguiente", command=pregunta_sig, font=("Arial", int(18 * escalar)), bg="red")
btn_sig.place(x=800, y=10)
btn_cat = Button(pant, text="Catálogo", command=mani_cats, font=("Arial", int(18 * escalar)), bg="red")
btn_cat.place(x=920, y=10)
btn_user = Button(pant, text="Usuarios", command=manipula_usuarios, font=("Arial", int(18 * escalar)), bg="red")
btn_user.place(x=1050, y=10)

# ---------------- TURNO ----------------
str_sig.set("Turno del jugador 1")
sig_jug = Label(pant, textvariable=str_sig, font=("Arial", int(18 * escalar)), bg="yellow")
sig_jug.place(x=450, y=10)

# ---------------- PREGUNTA ----------------
eti2 = Label(pant, text="Pregunta", font=("Arial", int(18 * escalar)), bg="white")
eti2.place(x=10, y=60)
pre = Entry(pant, textvariable=str_preg, font=("Arial", int(18 * escalar)), bg="lavender", width=70, state="readonly")
pre.place(x=150, y=100)

# ---------------- RESPUESTAS ----------------
r1 = Button(pant, textvariable=str_res1, command=opc1, font=("Arial", int(18 * escalar)), bg="blue", fg="white", width=20)
r1.place(x=100, y=180)

r2 = Button(pant, textvariable=str_res2, command=opc2, font=("Arial", int(18 * escalar)), bg="blue", fg="white", width=20)
r2.place(x=360, y=180)

r3 = Button(pant, textvariable=str_res3, command=opc3, font=("Arial", int(18 * escalar)), bg="blue", fg="white", width=20)
r3.place(x=620, y=180)

r4 = Button(pant, textvariable=str_res4, command=opc4, font=("Arial", int(18 * escalar)), bg="blue", fg="white", width=20)
r4.place(x=880, y=180)

desactivar_botones()

# ---------------- GIFS ----------------
def cargar_gif(ruta):
    frames = []
    i = 0
    while True:
        try:
            frame = PhotoImage(file=ruta, format=f"gif -index {i}")
            frames.append(frame)
            i += 1
        except:
            break
    return frames

# ---------------- JUGADOR 1 ----------------

ju1 = cargar_gif(r"./imagen/jugador1.gif")

if len(ju1) > 0:
    j1 = canvas.create_image(x1, y_j1, image=ju1[0], anchor="nw")

    def animar1(i=0):
        canvas.itemconfig(j1, image=ju1[i])
        i += 1
        if i >= len(ju1):
            i = 0
        pant.after(60, animar1, i)
    animar1()

# ---------------- JUGADOR 2 ----------------

ju2 = cargar_gif(r"./imagen/jugador2.gif")

if len(ju2) > 0:
    j2 = canvas.create_image(x2, y_j2, image=ju2[0], anchor="nw")

    def animar2(i=0):
        canvas.itemconfig(j2, image=ju2[i])
        i += 1
        if i >= len(ju2):
            i = 0
        pant.after(60, animar2, i)
    animar2()

# ---------------- JUGADOR 3 ----------------

ju3 = cargar_gif(r"./imagen/jugador3.gif")

if len(ju3) > 0:
    j3 = canvas.create_image(x3, y_j3, image=ju3[0], anchor="nw")

    def animar3(i=0):
        canvas.itemconfig(j3, image=ju3[i])
        i += 1
        if i >= len(ju3):
            i = 0
        pant.after(60, animar3, i)
    animar3()

# ---------------- IGNORANCIA ----------------

ju4 = cargar_gif(r"./imagen/ignorancia.gif")

if len(ju4) > 0:
    j4 = canvas.create_image(x4, y_j4, image=ju4[0], anchor="nw")
    
    def animar4(i=0):
        canvas.itemconfig(j4, image=ju4[i])
        i += 1
        if i >= len(ju4):
            i = 0
        pant.after(60, animar4, i)
    animar4()

pant.mainloop()