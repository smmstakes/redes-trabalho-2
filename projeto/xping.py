import time
import networkx as nx


def xping(G, origem, destino, n_pacotes=4):
    caminho = nx.shortest_path(G, origem, destino)
    print(f'Caminho: {" -> ".join(caminho)}')
    enviados = n_pacotes
    recebidos = n_pacotes  # Simulação sem perda
    tempo_total = 0
    for i in range(n_pacotes):
        inicio = time.time()
        # Simula tempo de ida e volta
        tempo = len(caminho) * 2
        time.sleep(0.01)
        tempo_total += tempo
        print(f'Resposta de {destino}: tempo={tempo}ms')
    print(
        f'Estatísticas: enviados={enviados}, recebidos={recebidos}, perdidos={enviados-recebidos}'
    )
    print(f'Tempo médio: {tempo_total/n_pacotes}ms')
