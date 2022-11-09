from biblioteca import Biblioteca
from libro import Libro

if __name__=='__main__':
    flag = True
    while(flag):
        print("--- BIBLIOTECAS ---")
        opcion = int(input("Qué vas a hacer?\n1. Crear Biblioteca\n2. Agregar Libro\n3. Ver catalogo\n4. Quitar libro\n5. Salir\n[opcion]:"))

        try:
            opcion = int(opcion)
        except ValueError:
            print("No es entero. Intenta de nuevo...")
            exit()
        
        if opcion == 1:
            nombre = input("Nombre de la bibliote: ")
            biblioteca= Biblioteca(nombre)
            print(f'Se creó la biblioteca: {biblioteca.consultar_nombre_biblioteca()}')

        elif opcion == 2:

            titulo = input("Título: ")
            autor= input("Autor: ")
            cantidad_de_paginas = input("Paginas: ")
            genero=input("Genero: ")
            sinopsis=input("Sinopsis: ")
            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)

            biblioteca.agregar_libro(libro)

        elif opcion == 3:
            print("Catalogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)
        elif opcion == 4:
            indice= int(input("Id del libro a eliminar"))
            biblioteca.quitar_libro(indice)
        elif opcion == 5:
            flag=False
        else:
            print("Opcion incorrecta, terminando el programa.")
        print("")




