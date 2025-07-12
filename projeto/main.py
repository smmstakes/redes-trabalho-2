import os
from topologia import G
from xping import xping
from xtraceroute import xtraceroute

if __name__ == '__main__':
    while True:
        hosts = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']

        print('SIMULADOR DE REDE')
        print('\n')
        print('=' * 50)
        print('Escolha o host origem (0 para cancelar):')
        print('=' * 50)
        print(*hosts, sep='\n')
        print('=' * 50)
        host_origem = input('Escolha: ')

        if host_origem == '0':
            break
        if host_origem not in hosts:
            print('\nEscolha inválida, tente novamente')
            continue

        hosts.remove(host_origem)

        print('\n')
        print('=' * 50)
        print('Escolha o host destino (0 para cancelar):')
        print('=' * 50)
        print(*hosts, sep='\n')
        print('=' * 50)
        host_destino = input('Escolha: ')
        print('=' * 50)

        if host_destino == '0':
            break
        if host_destino not in hosts:

            print('\nEscolha inválida, tente novamente\n')
            continue

        print('\n')
        print('=' * 50)
        print(f'Teste XPing de {host_origem} para {host_destino}:')
        print('=' * 50)
        xping(G, host_origem, host_destino)

        print('\n')
        print('=' * 50)
        print(f'Teste XTraceroute de {host_origem} para {host_destino}:')
        print('=' * 50)
        xtraceroute(G, host_origem, host_destino)
        print('=' * 50)

        print('\n')
        input('Pressione qualquer tecla para reiniciar')

        os.system('clear')
