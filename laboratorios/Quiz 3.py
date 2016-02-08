#programa que maneje una lista de super desde pueda agregar,ver,buscar y elimininar atriculos
lista_super=[]
lista =["arroz","leche","tuna","cereal","jugo"]

print("Listado de supermercado")
print("1.Agragar Articulo")
print("2.Eliminar Atriculo")
print("3.Ver Lista")
print("4.salir")
lis = int(input())
while lis!=4:
    if lis == 1:
        print(lista)
        print("Que articulo desea agragar: ")
        a=input()
        lista_super.append(a)
        print(lista)
        print(lista_super)
        print("1.Agragar Articulo")
        print("2.Eliminar Atriculo")
        print("3.Ver Lista")
        print("4.salir")
        lis = int(input())
    elif lis == 2:
        print(lista_super)
        print("Que articulo desea elimino: ")
        b=input()
        try:
            lista_super.remove(str(b))
            lis = int(input())
            print("1.Agragar Articulo")
            print("2.Eliminar Atriculo")
            print("3.Ver Lista")
            print("4.salir")
            lis = int(input())
        except ValueError:
            print("producto no en lisa")
            print(lista)
            print(lista_super)
            print("1.Agragar Articulo")
            print("2.Eliminar Atriculo")
            print("3.Ver Lista")
            print("4.salir")
            lis = int(input())
    elif lis == 3:
        print("El listado de articulos: ")
        print(lista)
        print(lista_super)
        print("1.Agragar Articulo")
        print("2.Eliminar Atriculo")
        print("3.Ver Lista")
        print("4.salir")
        lis = int(input())
    else:
        lis ==4
        print(lista)
        print(lista_super)
        break