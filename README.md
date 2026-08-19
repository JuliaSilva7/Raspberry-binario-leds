# Leitura de Binários

Simulação feita no [Wokwi](https://wokwi.com) que converte um número decimal (0 a 15) digitado pelo usuário em sua representação **binária** e **hexadecimal**, exibindo o resultado tanto no console quanto em 4 LEDs conectados a um Raspberry Pi Pico.

🔗 Projeto original: https://wokwi.com/projects/472751858971122689

## Como funciona

O programa roda em loop infinito e, a cada execução:

1. Pede ao usuário que digite um número decimal entre **0 e 15**.
2. Verifica se o número está dentro do intervalo válido.
3. Converte o número para binário (4 bits) usando uma tabela pré-definida.
4. Imprime no console o valor em decimal, binário e hexadecimal.
5. Acende os LEDs de acordo com os bits do número (1 = aceso, 0 = apagado).
6. Aguarda 1 segundo antes de pedir um novo número.

Se o valor digitado estiver fora do intervalo de 0 a 15, o programa exibe a mensagem `Valor Inválido`.

## Componentes utilizados

| Componente | Quantidade | Função |
|---|---|---|
| Raspberry Pi Pico | 1 | Microcontrolador principal |
| LED | 4 | Representação visual dos bits |
| Resistor 220Ω | 4 | Proteção dos LEDs |
| Protoboard | 1 | Montagem do circuito |

## Conexões (pinos do Pico)

| LED | Pino GPIO | Bit representado |
|---|---|---|
| LED 1 | GP15 | Bit 0 (menos significativo) |
| LED 2 | GP14 | Bit 1 |
| LED 3 | GP13 | Bit 2 |
| LED 4 | GP12 | Bit 3 (mais significativo) |

Cada LED é ligado em série com um resistor de 220Ω até o GND da protoboard.

##  Diagrama do circuito

<img width="822" height="496" alt="chrome_slGhjHKLfE" src="https://github.com/user-attachments/assets/991f1a7c-468c-47be-b2d9-bdf61ee43509" />

## Execução do Projeto

<img width="1920" height="911" alt="chrome_jKTH9Q8ACC" src="https://github.com/user-attachments/assets/8c0e2580-615f-4507-a1f8-d182e4ebf66c" />

## Estrutura do projeto

```
.
├── main.py            # Código principal em MicroPython
├── diagram.json        # Diagrama do circuito (formato Wokwi)
└── wokwi-project.txt   # Link de origem do projeto no Wokwi
```

## Como executar

1. Acesse o [Wokwi](https://wokwi.com) e crie um novo projeto para Raspberry Pi Pico.
2. Substitua o `main.py` e o `diagram.json` pelos arquivos deste repositório.
3. Inicie a simulação e digite números de 0 a 15 no terminal serial para ver o resultado.

## Tecnologias

- **MicroPython** (ambiente `micropython-20260406-v1.28.0`)
- **Wokwi** (simulador de circuitos eletrônicos)
