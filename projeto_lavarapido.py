from datetime import datetime, timedelta
from babel.dates import format_datetime

def data_formatada():   
    data_hora_atual = datetime.now()
    return format_datetime(data_hora_atual, "EEEE, d 'de' MMMM 'de' yyyy,'às' HH:mm", locale='pt_BR')

def calcular_horario_termino(tempo_minutos, horario_inicio):
    horario_termino = horario_inicio + timedelta(minutes=tempo_minutos)
    return horario_termino

def tempo_lavagem(tamanho_carro, tipo_lavagem):
    if tamanho_carro == 'pequeno':
        if tipo_lavagem == 1:
            return 30
        elif tipo_lavagem == 2:
            return 40
        elif tipo_lavagem == 3:
            return 50
    elif tamanho_carro == 'grande':
        if tipo_lavagem == 1:
            return 40
        elif tipo_lavagem == 2:
            return 50
        elif tipo_lavagem == 3:
            return 60  
    return 0

def calcular_valor(tipo_lavagem):
    if tipo_lavagem == 1:
        return 50
    elif tipo_lavagem == 2:
        return 100
    elif tipo_lavagem == 3:
        return 60

def formatar_horario(horario):
    return format_datetime(horario, "HH:mm", locale='pt_BR')

def input_opcao():
    while True:
        opcao = input("Qual é sua opção?\n")
        if opcao.isdigit():
            return int(opcao)
        else:
            print("Por favor, insira um número válido.")

def input_nome():
    while True:
        nome = input("Digite seu nome:  ").capitalize()
        if nome.isalpha():
            return nome
        else:
            print("Por favor, insira um nome válido (somente letras).")


quantidade_atendidos = 0
horario_livre = datetime.now()
print('🚗'*17)
print('  Seja bem-vindo ao Lava Rápido')
print('🚗'*17)
print('')


nome = input_nome()


tamanho_carro = input("Informe o tamanho  do seu  carro (pequeno/grande): ").lower()
while tamanho_carro not in ['pequeno', 'grande']:
    tamanho_carro = input("Tipo de carro inválido. Informe 'pequeno' ou 'grande': ").lower()


fila_horarios = []


while True:
    print(f"\nOlá, {nome}. Hoje é {data_formatada()}\n"         
        "Qual serviço você gostaria de realizar?\n"
        " [1] Lavagem Simples\n"
        " [2] Lavagem Completa\n"
        " [3] Só Polimento\n"
        " [4] Relatório\n"
        " [5] Mudar Tamanho do Carro\n"
        " [6] Sair\n")
    
    
    opção = input_opcao()
    while opção not in [1, 2, 3, 4, 5, 6]:
        print('Opção inválida, informe a opção correta.')
        opção = input_opcao()

    
    if opção in [1, 2, 3]:
        valor = calcular_valor(opção)
        tempo = tempo_lavagem(tamanho_carro, opção)
        horario_atual = datetime.now()

        
        if horario_atual >= horario_livre:
            horario_inicio = horario_atual
        else:
            horario_inicio = horario_livre

        
        horario_termino = calcular_horario_termino(tempo, horario_inicio)

        
        fila_horarios.append(horario_termino)
        horario_livre = horario_termino
        quantidade_atendidos += 1

        
        carros_na_frente = len(fila_horarios) - 1

        if carros_na_frente == 0:
            print("Você é o primeiro  na fila.")
        else:
            print(f"Há {carros_na_frente} carro(s) na sua frente.")

        print(f"Seu serviço será agendado para às {formatar_horario(horario_inicio)}.")
        print(f"Tempo estimado para o serviço: {tempo} minutos")
        print(f"Valor do serviço: R$ {valor},00")
        print(f"Horário estimado de término: {formatar_horario(horario_termino)}")


    elif opção == 4:
        print(f"\nTotal de carros atendidos hoje: {quantidade_atendidos}")

    
    elif opção == 5:
        tamanho_carro = input("Informe o novo tipo de carro (pequeno/grande): ").lower()
        while tamanho_carro not in ['pequeno', 'grande']:
            tamanho_carro = input("Tipo de carro inválido. Informe 'pequeno' ou 'grande': ").lower()
        print(f"Tamanho do carro atualizado para: {tamanho_carro}")

    
    elif opção == 6:
        print("Obrigado por usar o Lava Rápido! Até logo.")
        break

    
    outro_servico = input("Gostaria de realizar outro serviço? (sim/não): ").lower()
    while outro_servico not in ['sim', 'não']:
        outro_servico = input("Resposta inválida. Por favor, digite 'sim' ou 'não': ").lower()

    if outro_servico == 'não':
        print("Obrigado por usar o Lava Rápido! Até logo.")
        break
