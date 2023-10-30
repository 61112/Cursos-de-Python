#Centrar a la izquierda con caracter *
nombre= input ("Nombre: ")



print(f"\n              Bienvenido:{nombre.title()}")

print("\nTe ayudaremos en la Compra de un celular")


marcas_celular = ["0.Samsumg", "1.Apple", "2.Xiaomi", "3.Huawei"]

print(f"\nActualmente tenemos en existencia: {len(marcas_celular)} tipos de marcas diferentes y son:")

print("")
print(marcas_celular )

print("")
print("\n              Selecciona la marca que deseas:")


n= int(input("\nIngresa la marca SOLO EL NUMERO:"))


print(f"\nUsted selecciono la marca:  {marcas_celular[n]}")
