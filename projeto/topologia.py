import networkx as nx

# Criação do grafo da rede
G = nx.Graph()

# Adiciona hosts
hosts = {
    'H1': {'tipo': 'host', 'ip': '192.168.0.1'},
    'H2': {'tipo': 'host', 'ip': '192.168.0.2'},
    'H3': {'tipo': 'host', 'ip': '192.168.0.33'},
    'H4': {'tipo': 'host', 'ip': '192.168.0.34'},
    'H5': {'tipo': 'host', 'ip': '192.168.0.65'},
    'H6': {'tipo': 'host', 'ip': '192.168.0.66'},
    'H7': {'tipo': 'host', 'ip': '192.168.0.97'},
    'H8': {'tipo': 'host', 'ip': '192.168.0.98'},
}

# Adiciona roteadores
routers = {
    'C1': {'tipo': 'roteador', 'ip': '192.168.0.129'},
    'A1': {'tipo': 'roteador', 'ip': '192.168.0.130'},
    'A2': {'tipo': 'roteador', 'ip': '192.168.0.134'},
    'E1': {'tipo': 'roteador', 'ip': '192.168.0.137'},
    'E2': {'tipo': 'roteador', 'ip': '192.168.0.141'},
    'E3': {'tipo': 'roteador', 'ip': '192.168.0.145'},
    'E4': {'tipo': 'roteador', 'ip': '192.168.0.149'},
}

# Adiciona todos os nós ao grafo
for node, attr in {**hosts, **routers}.items():
    G.add_node(node, **attr)

# Adiciona enlaces (arestas) com atributos
G.add_edge('C1', 'A1', tipo='fibra', capacidade='10Gbps')
G.add_edge('C1', 'A2', tipo='fibra', capacidade='10Gbps')
G.add_edge('A1', 'E1', tipo='fibra', capacidade='1Gbps')
G.add_edge('A1', 'E2', tipo='fibra', capacidade='1Gbps')
G.add_edge('A2', 'E3', tipo='fibra', capacidade='1Gbps')
G.add_edge('A2', 'E4', tipo='fibra', capacidade='1Gbps')
G.add_edge('E1', 'H1', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E1', 'H2', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E2', 'H3', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E2', 'H4', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E3', 'H5', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E3', 'H6', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E4', 'H7', tipo='par trançado', capacidade='1Gbps')
G.add_edge('E4', 'H8', tipo='par trançado', capacidade='1Gbps')
