import networkx as nx


def xtraceroute(G, origem, destino):
    caminho = nx.shortest_path(G, origem, destino)
    print(f'Rota de {origem} para {destino}:')
    for idx, nodo in enumerate(caminho):
        ip = G.nodes[nodo]['ip']
        print(f'Salto {idx+1}: {nodo} (IP: {ip})')
    print(f'Total de saltos: {len(caminho)-1}')
