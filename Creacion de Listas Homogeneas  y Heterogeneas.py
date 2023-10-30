#Creando una lista vacia


print("Lista vacia")

lista_vacia = []
print(lista_vacia)



#**********************************************************
print("\nLista Homogenea")
#Lista Homogenea
#Solo adminte introducir valores de un mismo caracter
#Ejemplo:
#eduardo, carlos, juan, santiago  ....

lista_homogenea = ["eduardo", "carlos", "juan", "santiago"]

print(lista_homogenea )


#**************************************************************
print("\nLista Heterogenea")
#Lista Heterogenea
#Admite valores de diferentes caracteres
#Ejemplo:
#eduardo, 25, 3.1416, true  ...

lista_heterogenea = ['eduardo', 24, 1.64, True]

print(lista_heterogenea )


#************************************************************
print("****************************************************")

#segundo programa
#consultar un dato de mi tabla

#tabla de ejemplo
print("\nTabla de ejemplo")
marcas_celular = ["samsumg", "apple", "xiaomi", "huawei"]

print("\nTabla completa")
print(marcas_celular )

print("")
print(f"\nLa tabla de Marcas de celulares tiene: {len(marcas_celular)} tipos de datos diferentes")

print(f"\nUsted selecciono la marca[0]: la cual es  {marcas_celular[0]}")

