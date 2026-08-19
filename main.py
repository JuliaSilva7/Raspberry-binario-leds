from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)


# Binários de 0 até 15
binarios = [
    "0000", "0001", "0010", "0011",
    "0100", "0101", "0110", "0111",
    "1000", "1001", "1010", "1011",
    "1100", "1101", "1110", "1111"
]

while True:
    numero = int(input('Escreva um número de 0 a 15: '))
    if 0 <= numero < 16:

        binario = binarios[numero]

        print("Decimal:", numero)
        print("Binário:", binario)
        print("Hexadecimal:", hex(numero))
        print("LEDs:", binario)
        print("----------------")

        led1.value(int(binario[3]))
        led2.value(int(binario[2]))
        led3.value(int(binario[1]))
        led4.value(int(binario[0]))

        sleep(1)
    else:
        print('Valor Inválido')