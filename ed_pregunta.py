from tkinter import *
from tkinter import ttk
from conecta_bd  import * 

def manipula_pregunta (datos):
    id=datos [0]
    pantalla_pre=Toplevel()
    pantalla_pre.geometry("1250x550")
    pantalla_pre.resizable(1,1)
    pantalla_pre.config(background="light Sky blue")
    pantalla_pre.title("catalogo")
    str_cat=StringVar()
    str_cat.set(datos[1]) 
    str_pre=StringVar()
    str_op1=StringVar()
    str_op2=StringVar()
    str_op3=StringVar()
    str_op4=StringVar()
    str_cor=StringVar()

    marco_pre=Frame(pantalla_pre)
    marco_pre.pack()
    marco_pre.place(x=20 , y=250)
    ver_sb=ttk.Scrollbar( marco_pre,orient="vertical")
    ver_sb.pack(side=RIGHT,fill=Y)

    tabl_pre=ttk.Treeview(marco_pre,columns=("preg","opc1","opc2","opc3","opc4","corr"),yscrollcommand=ver_sb.set)
    tabl_pre.column("#0",width=50)
    tabl_pre.column("preg",width=500)
    tabl_pre.column("opc1",width=150)
    tabl_pre.column("opc2",width=150)
    tabl_pre.column("opc3",width=150)
    tabl_pre.column("opc4",width=150)
    tabl_pre.column("corr",width=10)

    tabl_pre.heading("#0",text="id")
    tabl_pre.heading("preg",text="preguntas")
    tabl_pre.heading("opc1",text="opc.1")
    tabl_pre.heading("opc2",text="opc.2")
    tabl_pre.heading("opc3",text="opc.3")
    tabl_pre.heading("opc4",text="opc.4")
    tabl_pre.heading("corr",text="correcto")
    tabl_pre.pack()

    ver_sb.config(command=tabl_pre.yview)

    def recupera_preg(ide):
        for record in tabl_pre.get_children():
            tabl_pre.delete(record)
        pregs=tabla_preguntas(ide)
        for preg in pregs:
            tabl_pre.insert(parent="",index="end",iid=preg[0],text=str(preg[0]),values=(str(preg[1]).replace(' ','_'),
			str(preg[2]).replace(' ','_'),str(preg[3]).replace(' ','_'),str(preg[4]).replace(' ','_'),
			str(preg[5]).replace(' ','_'),str(preg[6]).replace(' ','_')))

    def agregar_pre():
        datos=(str_pre.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_cor.get())
        inserta_pregunta(datos,id)
        recupera_preg(id)


    def selec_pre():
        ab = tabl_pre.selection()[0]
        dato=selec_preguntas(ab)
        str_pre.set(dato[1])
        str_op1.set(dato[2])
        str_op2.set(dato[3])
        str_op3.set(dato[4])
        str_op4.set(dato[5])
        str_cor.set(dato[6])
        str_cat.set(datos(1))
        str_pre.set(" ")
        str_op1.set(" ")
        str_op2.set(" ")
        str_op3.set(" ")
        str_op4.set(" ")
        str_cor.set(" ")

    def borra_pre():
        seleccion = tabl_pre.selection()
        ab = seleccion[0]
        borra_pregunta(ab)
        recupera_preg(id)

    def modif_pre():
        seleccion = tabl_pre.selection()
        ab = seleccion[0]
        datos = (str_pre.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_cor.get())
        modif_pregunta(ab, datos)
        recupera_preg(id)

    et1=Label(pantalla_pre,text="Categoria",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=20, y=20)
    cate=Entry(pantalla_pre,textvariable=str_cat,font='Helvetica 14 bold ',bg="Lavender",width=50,state=DISABLED).place(x=120, y=20)

    et2=Label(pantalla_pre,text="Pregunta",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=20, y=60)
    preg=Entry(pantalla_pre,textvariable=str_pre,font='Helvetica 14 bold ',bg="Lavender",width=80).place(x=120, y=60)

    et3=Label(pantalla_pre,text="Opcion 1",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=20, y=90)
    opc1=Entry(pantalla_pre,textvariable=str_op1,font='Helvetica 14 bold ',bg="Lavender",width=30).place(x=120, y=90)

    et4=Label(pantalla_pre,text="Opcion 2",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=550, y=90)
    opc2=Entry(pantalla_pre,textvariable=str_op2,font='Helvetica 14 bold ',bg="Lavender",width=30).place(x=670, y=90)

    et5=Label(pantalla_pre,text="Opcion 3",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=20, y=120)
    opc3=Entry(pantalla_pre,textvariable=str_op3,font='Helvetica 14 bold ',bg="Lavender",width=30).place(x=120, y=120)

    et6=Label(pantalla_pre,text="Opcion 4",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=550, y=120)
    opc4=Entry(pantalla_pre,textvariable=str_op4,font='Helvetica 14 bold ',bg="Lavender",width=30).place(x=670, y=120)

    et7=Label(pantalla_pre,text="Correcto",bg="Light Sky Blue", font='Helvetica 14 bold ').place(x=20, y=150)
    corr=Entry(pantalla_pre,textvariable=str_cor,font='Helvetica 14 bold ',bg="Lavender",width=30).place(x=120, y=150)
    
    b_pre=Button(pantalla_pre,text="agregar pregunta",command=agregar_pre,fg="white",bg="red4",font="arial 12").place(x=10,y=200)
    b_modif_pre=Button(pantalla_pre,text=" modifica pregunta",command=modif_pre,fg="white",bg="red4",font="arial 12",width=20).place(x=160,y=200)
    b_borra_pre=Button(pantalla_pre,text="borrar pregunta",command=borra_pre,fg="white",bg="red4",font="arial 12",width=20).place(x=350,y=200)
    b_selec_pre=Button(pantalla_pre,text="seleciona pregunta",command=selec_pre,fg="white",bg="red4",font="arial 12", width=20 ).place(x=540,y=200)
    recupera_preg(id)