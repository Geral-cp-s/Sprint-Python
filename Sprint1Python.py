"""
G4-TECH
Membros:
Augusto Douglas Nogueira de Mendonça - RM558371
Gabriel Vasquez Queiroz da Silva - RM557056
Guilherme Araujo de Carvalho - RM558926
Gustavo Oliveira Ribeiro - RM559163
"""

# Função para converter o tempo em segundos para minuto:segundo:milissegundo
def converter_tempo(tempo):
    minutos = int(tempo // 60)
    segundos = int(tempo % 60)
    milissegundos = int((tempo - int(tempo)) * 1000)
    return f"{minutos:02}:{segundos:02}:{milissegundos:03}"


# Função para encontrar o melhor e pior tempo e suas respectivas voltas
def encontrar_melhor_pior_tempo(tempos):
    melhor_tempo = tempos[0]
    pior_tempo = tempos[0]
    volta_melhor_tempo = 1
    volta_pior_tempo = 1

    for i in range(1, len(tempos)):
        if tempos[i] < melhor_tempo:
            melhor_tempo = tempos[i]
            volta_melhor_tempo = i + 1
        if tempos[i] > pior_tempo:
            pior_tempo = tempos[i]
            volta_pior_tempo = i + 1

    return melhor_tempo, pior_tempo, volta_melhor_tempo, volta_pior_tempo


# Função para atualizar a lista de melhores voltas
def atualizar_melhores_voltas(melhores_voltas, nome, tempo, volta):
    melhores_voltas.append({"nome": nome, "tempo": tempo, "volta": volta})
    melhores_voltas.sort(key=lambda x: x["tempo"])  # Ordena pela melhor volta (menor tempo)


# Função para exibir a melhor volta registrada
def exibir_melhor_volta(melhores_voltas):
    if melhores_voltas:
        melhor_volta = melhores_voltas[0]
        return melhor_volta["nome"], converter_tempo(melhor_volta["tempo"]), melhor_volta["volta"]
    else:
        return None, None, None


# Lista para armazenar os melhores tempos
melhores_voltas = []

while True:
    print('\n----------------------------------------------------------')
    print('BEM VINDO, ESSE PROGRAMA FOI FEITO PARA ANALISAR SUA VOLTA')
    print('----------------------------------------------------------\n')

    # Exibir a melhor volta registrada na lista antes de pedir os dados
    melhor_nome, melhor_tempo_registrado, melhor_volta = exibir_melhor_volta(melhores_voltas)
    if melhor_nome:
        print(f"\nMelhor volta registrada: {melhor_tempo_registrado} (Volta {melhor_volta}) por {melhor_nome}")
    else:
        print("\nAinda não há voltas registradas.")

    # Coletar o nome do piloto
    nome_piloto = input("Digite o nome do piloto ou 'sair' para encerrar: ")
    if nome_piloto.lower() == "sair":
        break

    # Coletar o número de voltas e os tempos de cada volta
    voltas_input = input("Digite o número de voltas: ")
    try:
        voltas = int(voltas_input)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido de voltas.")
        continue

    tempos_voltas = []

    for i in range(voltas):
        while True:
            try:
                tempo = float(input(f"Digite o tempo da volta {i + 1} em segundos: "))
                tempos_voltas.append(tempo)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um tempo válido em segundos.")

    # Encontrar o melhor e pior tempo e suas respectivas voltas
    melhor_tempo, pior_tempo, volta_melhor_tempo, volta_pior_tempo = encontrar_melhor_pior_tempo(tempos_voltas)

    # Atualizar a lista de melhores voltas
    atualizar_melhores_voltas(melhores_voltas, nome_piloto, melhor_tempo, volta_melhor_tempo)

    # Exibir os resultados
    print("\nTempos das voltas:")
    for i, tempo in enumerate(tempos_voltas):
        print(f"Volta {i + 1}: {converter_tempo(tempo)}")

    print(f"\nMelhor tempo: {converter_tempo(melhor_tempo)} (Volta {volta_melhor_tempo})")
    print(f"Pior tempo: {converter_tempo(pior_tempo)} (Volta {volta_pior_tempo})")

    print('\n---------------------------------------------------------')
    print('ANÁLISE ENCERRADA, OBRIGADO POR UTILIZAR O NOSSO PROGRAMA')
    print('---------------------------------------------------------\n')