numero_procurado = 13  # número que queremos verificar se pertence à sequência

a, b = 0, 1  # valores iniciais da sequência de Fibonacci
encontrado = False  # flag para indicar se o número foi encontrado ou não

while b < numero_procurado:
    a, b = b, a + b  # calcula o próximo valor da sequência
    
if b == numero_procurado:
    encontrado = True  # número foi encontrado na sequência

if encontrado:
    print(f"O número {numero_procurado} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero_procurado} não pertence à sequência de Fibonacci.")
