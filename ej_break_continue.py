lista_productos = []

while True:
    producto = input("Ingrese el nombre del producto: (escriba 'echo' para terminar): ")
    if producto.lower() == "echo":
        break
    else:
        lista_productos.append(producto)

print("\nLista productos")
for indice, valor in enumerate(lista_productos):
    print(f"{indice+1}. {valor}")
