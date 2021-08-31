#Escribe un método que reciba un número entero positivo n, después debe calcular la suma 1+2+3+...+n. Finalmente regrese el resultado de la suma y sea impreso en pantalla.
#Entrada: Un número entero positivo n
#Salida: El resultado de la suma 1+2+3...+n

def main():
    #escribe tu código abajo de esta línea
    n = int(input('Número: '))
    i = 1
    suma = 0
    while i <= n:
        suma += i
        i+=1
    print(suma)

if __name__=='__main__':
    main()
