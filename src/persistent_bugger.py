def persistence(n):
    if n < 10: 
        return 0
    multiplicacion = 1
    while(n > 0):
        multiplicacion = (n % 10) * multiplicacion   #Obtencion del modulo
        n = n // 10                                  #Division entera
    return persistence(multiplicacion) + 1

if __name__ == "__main__":
    persistence()