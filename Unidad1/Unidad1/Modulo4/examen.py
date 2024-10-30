listarouters= []


listarouters.insert(0,"router 1")
listarouters.insert(1,"router 2")
listarouters.insert(2,"router 3")
print("selecciona una opción:")

while True:
  print("1)Agregar router")
  print("2)Listar routers")
  print("3)Buscar router")
  print("4)Modificar router")
  print("e)Eliminar router")
  print("f)Salir")
  opcion = int(input("]Ingrese la opcion que necesite"))
  nombrenuevo=input("Ingresa el nombre del router:")
  if opcion == 1:
    if nombrenuevo in listarouters:
      print("el router ya existe")
    else:
     listarouters.append(nombrenuevo)
  elif opcion == 2:
    print("los routers son:")
    print({listarouters})
         
  elif opcion == 3:
   buscar =str(input("¿Que router buscas?"))
   for i in listarouters:
    if buscar == i:
      print("el router existe")
         
    else:
      print("el router no existe")
         
  elif opcion == 4:
     print("¿Que router deseas modificar?")
     modificar = str(input())
     for i in listarouters:
      if modificar == i:
         listarouters.append(modificar)
         print({listarouters})
