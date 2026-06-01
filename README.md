# mission-control-ai
**Sistema Inteligente de Monitoramento de Missão Espacial**

**Missão:** Artemis V Test  
**Equipe:** Starship Troopers  

##  Sobre o Projeto
Este projeto foi desenvolvido como parte da Global Solution da FIAP para a disciplina de Pensamento Computacional e Automação com Python. O objetivo do sistema é monitorar, através de simulações, telemetrias vitais de uma missão espacial, classificando o risco de cada ciclo orbital e emitindo relatórios automáticos de contingência.

##  Funcionalidades
O algoritmo realiza a leitura de uma matriz de dados simulando múltiplos ciclos da missão, avaliando 5 sensores críticos:
1. Temperatura Interna (ºC)
2. Comunicação com a Base (%)
3. Sistema de Energia/Bateria (%)
4. Suporte de Oxigênio (%)
5. Estabilidade Operacional (%)

O sistema processa essas informações e gera um **Relatório Final** exibindo médias, a área mais afetada, a quantidade de ciclos críticos e a tendência geral da missão (piora, melhora ou estabilidade).

##  Regras de Alerta e Classificação
O sistema utiliza um sistema de pontuação de risco para cada sensor:
- **NORMAL** (0 pontos)
- **ATENÇÃO** (1 ponto)
- **CRÍTICO** (2 pontos)

As regras estabelecidas para cada variável seguem os parâmetros abaixo:

| Sensor | NORMAL | ATENÇÃO | CRÍTICO |
| :--- | :--- | :--- | :--- |
| **Temperatura** | 18ºC a 30ºC | < 18ºC ou 31ºC a 35ºC | > 35ºC |
| **Comunicação** | >= 60% | 30% a 59% | < 30% |
| **Bateria** | >= 50% | 20% a 49% | < 20% |
| **Oxigênio** | >= 90% | 80% a 89% | < 80% |
| **Estabilidade**| >= 70% | 40% a 69% | < 40% |

Com base na soma dos pontos de um ciclo, a missão recebe sua classificação geral:
- **0 a 2 pontos:** MISSÃO ESTÁVEL
- **3 a 5 pontos:** MISSÃO EM ATENÇÃO
- **6 a 10 pontos:** MISSÃO CRÍTICA

##  Como Executar
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório.
3. Execute o script principal pelo terminal:
   ```bash
   python mission_control.py
