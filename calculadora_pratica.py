# CALCULADORA WHILE 

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador que deseja (+ para somar, - para subtrair, / para divisão e * para multiplicação): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    # caso de erro nos números digitados. 
    if numeros_validos is None: 
        print('Um ou os dois números digitados não é válido.')
        continue
    
    operadores_validos = '=-/*'

# caso digite algum operador fora do específicado.
    if operador not in operadores_validos:
        print ('Operador inválido.')
        continue

    if len(operador) > 1: 
        print('Digite apenas um operador.')

    print('Realizando conta...')

    if operador == '+':
        print(num_1_float + num_2_float) 

    elif operador == '-':
        print(num_1_float - num_2_float) 

    elif operador == '/':
        print(num_1_float / num_2_float) 

    elif operador == '*':
        print(num_1_float * num_2_float) 
    else: 
        print('Você nunca deveria ter chego aqui.')
    
    
    sair = input('Você deseja sair?:  [s]im. Ou deseja fazer outra conta? pressione [r]efazer: ').lower().startswith('s')
    
    if sair is True:
        break