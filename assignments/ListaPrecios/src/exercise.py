#Escribe un programa que lea la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos. El programa debe mostrar en la pantalla el precio correspondiente a cada artículo pedido, el programa debe repetirse mientras el usuario no teclee la clave X, cuando el usuario teclee la clave X el programa debe mostrar en la pantalla el total de la compra del cliente.
#Entrada: Una secuencia de letras que representan la clave del artículo que se va a comprar. Debe terminar con X que significa que ya se terminó de comprar.
#Salida: Para cada letra que se ingrese, se debe mostrar el precio del artículo correspondiente.
#Después de que se teclee la letra X se debe mostrar el total de los artículos elegidos.

def main():
    #escribe tu código abajo de esta línea
    precioA = 120
    precioB = 250
    precioC = 360
    total = 0
    art = ''

    while art != 'X':
        
        art = input('¿Qué artículo deseas comprar? (A, B o C)\n')

        if art == 'A':
            print(precioA)
            total += precioA

        elif art == 'B':
            print(precioB)
            total += precioB
        
        elif art == 'C':
            print(precioC)
            total += precioC
        
        elif art == 'X':
            print(total)

        else:
            print('Error. Elige otro artículo.')


if __name__=='__main__':
    main()
