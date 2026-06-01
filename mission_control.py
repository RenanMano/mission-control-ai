# ==========================================
# GLOBAL SOLUTION 2026.1 - FIAP
# Mission Control AI: Sistema Inteligente de Monitoramento
# Missão: Artemis V Test
# Equipe: Starship Troopers
# ==========================================

# 1. Matriz Principal e Áreas Monitoradas
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Matriz [temperatura, comunicacao, bateria, oxigenio, estabilidade] - 6 Ciclos
dados_missao = [
    [22, 95, 90, 98, 92], # Ciclo 1: Estável
    [28, 85, 75, 92, 88], # Ciclo 2: Estável
    [32, 55, 45, 85, 65], # Ciclo 3: Atenção (Aquecendo, Comms caindo)
    [36, 25, 15, 75, 38], # Ciclo 4: Crítico (Temp alta, Bateria e Oxigênio baixos)
    [31, 45, 35, 82, 55], # Ciclo 5: Atenção (Recuperação parcial)
    [26, 70, 60, 90, 80]  # Ciclo 6: Estável (Sistemas restabelecidos)
]

# Dicionário para acumular os pontos de risco por área ao longo de todos os ciclos
risco_acumulado_areas = {
    0: 0, # Temperatura
    1: 0, # Comunicação
    2: 0, # Bateria
    3: 0, # Oxigênio
    4: 0  # Estabilidade
}

# --- FUNÇÕES DE ANÁLISE DE DADOS (Requisito: Mínimo de 5 funções) ---

def analisar_sensor(valor, tipo):
    """Função 1: Analisa o valor de um sensor específico e retorna os pontos de risco e a string de status"""
    status = ""
    pontos = 0
    
    if tipo == "temperatura":
        if valor < 18 or (valor > 30 and valor <= 35):
            status, pontos = "ATENÇÃO", 1
        elif valor > 35:
            status, pontos = "CRÍTICO", 2
        else:
            status, pontos = "NORMAL", 0
            
    elif tipo == "comunicacao":
        if valor < 30:
            status, pontos = "CRÍTICO", 2
        elif 30 <= valor <= 59:
            status, pontos = "ATENÇÃO", 1
        else:
            status, pontos = "NORMAL", 0
            
    elif tipo == "bateria":
        if valor < 20:
            status, pontos = "CRÍTICO", 2
        elif 20 <= valor <= 49:
            status, pontos = "ATENÇÃO", 1
        else:
            status, pontos = "NORMAL", 0
            
    elif tipo == "oxigenio":
        if valor < 80:
            status, pontos = "CRÍTICO", 2
        elif 80 <= valor <= 89:
            status, pontos = "ATENÇÃO", 1
        else:
            status, pontos = "NORMAL", 0
            
    elif tipo == "estabilidade":
        if valor < 40:
            status, pontos = "CRÍTICO", 2
        elif 40 <= valor <= 69:
            status, pontos = "ATENÇÃO", 1
        else:
            status, pontos = "NORMAL", 0
            
    return status, pontos

def classificar_ciclo(pontuacao_total):
    """Função 2: Classifica o ciclo com base na pontuação total e sugere recomendação"""
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL", "Manter operação normal e continuar monitoramento."
    elif 3 <= pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO", "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "MISSÃO CRÍTICA", "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

def analisar_tendencia(risco_inicial, risco_final):
    """Função 3: Compara o risco do primeiro e último ciclo para definir a tendência"""
    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def identificar_area_mais_afetada(dicionario_riscos, lista_areas):
    """Função 4: Encontra qual área acumulou mais pontos de risco durante a missão"""
    indice_maior_risco = max(dicionario_riscos, key=dicionario_riscos.get)
    return lista_areas[indice_maior_risco]

def calcular_medias_missao(matriz):
    """Função 5: Calcula a média de todos os sensores em toda a missão"""
    qtd_ciclos = len(matriz)
    somas = [0, 0, 0, 0, 0]
    
    for ciclo in matriz:
        for i in range(5):
            somas[i] += ciclo[i]
            
    medias = [soma / qtd_ciclos for soma in somas]
    return medias

# --- LÓGICA PRINCIPAL DO PROGRAMA ---

print("============================================================")
print("                    MISSION CONTROL AI                      ")
print("============================================================")
print("Missão: Artemis V Test")
print("Equipe: Starship Troopers")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("============================================================\n")

# Variáveis para armazenar dados para o relatório final
historico_pontuacoes = []
ciclos_criticos = 0
maior_risco_registrado = -1
ciclo_mais_critico = 0

# Estrutura de repetição para percorrer os ciclos da matriz
for i in range(len(dados_missao)):
    ciclo_atual = dados_missao[i]
    print(f"CICLO {i + 1}")
    
    # Analisando cada sensor do ciclo e acumulando pontuação de risco
    stat_temp, pts_temp = analisar_sensor(ciclo_atual[0], "temperatura")
    stat_com, pts_com = analisar_sensor(ciclo_atual[1], "comunicacao")
    stat_bat, pts_bat = analisar_sensor(ciclo_atual[2], "bateria")
    stat_oxi, pts_oxi = analisar_sensor(ciclo_atual[3], "oxigenio")
    stat_est, pts_est = analisar_sensor(ciclo_atual[4], "estabilidade")
    
    # Acumulando riscos globais para o relatório final
    risco_acumulado_areas[0] += pts_temp
    risco_acumulado_areas[1] += pts_com
    risco_acumulado_areas[2] += pts_bat
    risco_acumulado_areas[3] += pts_oxi
    risco_acumulado_areas[4] += pts_est
    
    pontuacao_ciclo = pts_temp + pts_com + pts_bat + pts_oxi + pts_est
    historico_pontuacoes.append(pontuacao_ciclo)
    
    # Atualizando estatísticas para o relatório final
    if pontuacao_ciclo > maior_risco_registrado:
        maior_risco_registrado = pontuacao_ciclo
        ciclo_mais_critico = i + 1
        
    classificacao, recomendacao = classificar_ciclo(pontuacao_ciclo)
    
    if classificacao == "MISSÃO CRÍTICA":
        ciclos_criticos += 1

    # Impressão do relatório do ciclo atual
    print(f"Temperatura: {ciclo_atual[0]}ºC | {stat_temp}")
    print(f"Comunicação: {ciclo_atual[1]}% | {stat_com}")
    print(f"Bateria: {ciclo_atual[2]}% | {stat_bat}")
    print(f"Oxigênio: {ciclo_atual[3]}% | {stat_oxi}")
    print(f"Estabilidade: {ciclo_atual[4]}% | {stat_est}")
    print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}\n")

# --- GERAÇÃO DO RELATÓRIO FINAL ---
medias_finais = calcular_medias_missao(dados_missao)
risco_medio = sum(historico_pontuacoes) / len(historico_pontuacoes)
tendencia = analisar_tendencia(historico_pontuacoes[0], historico_pontuacoes[-1])
area_critica = identificar_area_mais_afetada(risco_acumulado_areas, areas_monitoradas)
classe_final, _ = classificar_ciclo(risco_medio)

print("============================================================")
print("                 RELATÓRIO FINAL DA MISSÃO                  ")
print("============================================================")
print("Missão: Artemis V Test")
print("Equipe: Starship Troopers")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")

print(f"Média de temperatura: {medias_finais[0]:.2f}ºC")
print(f"Média de comunicação: {medias_finais[1]:.2f}%")
print(f"Média de bateria: {medias_finais[2]:.2f}%")
print(f"Média de oxigênio: {medias_finais[3]:.2f}%")
print(f"Média de estabilidade: {medias_finais[4]:.2f}%\n")

print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco_registrado}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {ciclos_criticos}\n")

print("Tendência da missão:")
print(tendencia, "\n")

print("Pontuação acumulada por área:")
for i in range(5):
    print(f"{areas_monitoradas[i]}: {risco_acumulado_areas[i]} pontos")

print(f"\nÁrea mais afetada:\n{area_critica}\n")

print("Classificação final da missão:")
print(classe_final)
print("============================================================")