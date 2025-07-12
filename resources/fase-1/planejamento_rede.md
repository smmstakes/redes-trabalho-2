# Cálculo de VLSM

## Sub-redes para os hosts

Contém 4 sub-redes para os hosts, com as seguintes quantidades de hosts:

- Sub-rede e1: 30 hosts
- Sub-rede e2: 30 hosts

- Sub-rede e3: 20 hosts
- Sub-rede e4: 20 hosts

# Sub-redes para os roteadores

Contém 6 sub-redes para as conexões entre os roteadores e as sub-redes de hosts.

- Conexão c1 $\leftrightarrow$ a1
- Conexão c1 $\leftrightarrow$ a2
- Conexão a1 $\leftrightarrow$ e1
- Conexão a1 $\leftrightarrow$ e2

- Conexão a2 $\leftrightarrow$ e3
- Conexão a2 $\leftrightarrow$ e4
-

## Cálculo de VLSM

Criar sub-redes de tamanhos diferentes, otimizando o uso de endereços IP

### Definir a quantidade de bits para cada sub-rede

A quantidade de bits para cada sub-rede deve superar sua quantidade de hosts, assim:

- Redes com 30 hosts (e1, e2)
  $$
  2^5 - 2 \geq 30 \Rightarrow  32 -2 \geq 30 \Rightarrow 30 \geq 30
  $$
  - Dos 32 bits de IP da rede 5 estão alocados para essa sub-rede, assim a máscara (CIDR) é $32 - 5 = 27$, portanto **\27**
- Redes com 20 hosts (e3, e4)

  $$
   2^5 - 2 \geq 20 \Rightarrow  32 -2 \geq 20 \Rightarrow 30 \geq 20
  $$

      - CIDR: $32 - 5 = 27$, portanto **\27**

- Roteadores
  $$
  2^2 - 2 \geq 2 \Rightarrow 4 - 2 \geq 2 \Rightarrow 2\geq 2
  $$
      - CIDR: $32 - 2 = 30$, portanto **/30**

### Alocando as sub-redes

O intervalo de IP privado mais comum é o 192.168.0.0 a 192.168.255.255, será utilizado o **192.168.0.0 /24**

Para as redes com 32 endereços

- **Rede e1:** `192.168.0.0 /27`
  - 192.168.0.0 - 192.168.0.31
- **Rede e2:** `192.168.0.32 /27`
  - 192.168.0.32 - 192.168.0.63
- **Rede e3:** `192.168.0.64 /27`
  - 192.168.0.64 - 192.168.0.95
- **Rede e4:** `192.168.0.0 /27`
  - 192.168.0.96 - 192.168.0.127

Para as redes com 4 endereços, continuando do ultimo endereço disponível que é 192.168.0.128

- **Link c1-a1:** `192.168.0.128 /30`
  - 192.168.0.129 -192.168.0.130
- **Link c1-a2:** `192.168.0.132 /30`
  - 192.168.0.133 -192.168.0.134
- **Link a1-e1:** `192.168.0.136 /30`
  - 192.168.0.137 -192.168.0.138
- **Link a1-e2:** `192.168.0.14 /30`
  - 192.168.0.141 -192.168.0.142
- **Link a2-e3:** `192.168.0.144 /30`
  - 192.168.0.145-192.168.0.146
- **Link a2-e4:** `192.168.0.148 /30`
  - 192.168.0.149 -192.168.0.150

| Uso da Sub-rede           | Endereço de Rede | Máscara | Faixa de IPs Úteis           | Endereço de Broadcast |
| ------------------------- | ---------------- | ------- | ---------------------------- | --------------------- |
| **Rede para Hosts de e1** | 192.168.0.0      | /27     | 192.168.0.1 - 192.168.0.30   | 192.168.0.31          |
| **Rede para Hosts de e2** | 192.168.0.32     | /27     | 192.168.0.33 - 192.168.0.62  | 192.168.0.63          |
| **Rede para Hosts de e3** | 192.168.0.64     | /27     | 192.168.0.65 - 192.168.0.94  | 192.168.0.95          |
| **Rede para Hosts de e4** | 192.168.0.96     | /27     | 192.168.0.97 - 192.168.0.126 | 192.168.0.127         |
| **Enlace c1-a1**          | 192.168.0.128    | /30     | .129, .130                   | 131                   |
| **Enlace c1-a2**          | 192.168.0.132    | /30     | .133, .134                   | 135                   |
| **Enlace a1-e1**          | 192.168.0.136    | /30     | .137, .138                   | 139                   |
| **Enlace a1-e2**          | 192.168.0.140    | /30     | .141, .142                   | 143                   |
| **Enlace a2-e3**          | 192.168.0.144    | /30     | .145, .146                   | 147                   |
| **Enlace a2-e4**          | 192.168.0.148    | /30     | .149, .150                   | 151                   |

---

## Dúvidas sobre os Roteadores

### Trocar Roteadores de Edge (e1-e4) por Switches?

1. **Função do Roteador:** Um roteador é usado para **conectar redes diferentes**. O seu dispositivo `e1`, por exemplo, precisa conectar duas redes distintas:
   - A rede dos hosts (ex: `192.168.0.0/27`).
   - A rede do enlace com o roteador de agregação a1 (ex: 192.168.0.136/30).
     Apenas um roteador (ou um Switch de Camada 3, que é mais complexo) pode fazer isso, pois ele opera com endereços IP e toma decisões de roteamento. Um switch comum não consegue.
2. **O Requisito de "30 hosts":** Este é um ponto-chave que causa confusão. O requisito de que "as sub-redes e1 e e2 devem ter capacidade para endereçar ao menos 30 hosts em cada uma", se refere ao **tamanho do espaço de endereçamento IP**, e não à quantidade de portas físicas em um único aparelho.
   - O seu plano de usar uma máscara `/27` (que permite 30 IPs úteis) atende perfeitamente a esse requisito.
   - Em uma rede real, para conectar esses 30 hosts, você usaria um ou mais switches de 24 portas ligados entre si, e esse conjunto de switches se conectaria a uma única porta do seu roteador `e1`.
   - **Para o seu projeto no Packet Tracer, usar um único switch e 2 hosts (`H1`, `H2`) para representar essa rede local é uma simplificação perfeitamente aceitável e correta.**

### Sub-redes dos Roteadores de Agregação

- **No Plano de Endereçamento:** Ao usar o VLSM e um bloco grande como `192.168.0.0/24`, você deixou muito espaço de IPs livres. Há centenas de sub-redes disponíveis para serem usadas no futuro, então seu plano de IPs é escalável.

- **Na Escolha do Hardware:** O roteador `2911` é um equipamento **modular**. Isso significa que, no mundo real, você poderia comprar e instalar novos "módulos de interface" (chamados HWICs) para adicionar mais portas a ele conforme a necessidade. Você não precisa fazer isso no Packet Tracer, mas pode (e deve) mencionar essa característica no seu relatório.

**Como Documentar Isso no Relatório:**

> "Para os roteadores de agregação:
> `a1` e `a2`, foi escolhido o modelo modular Cisco 2911. Embora na implementação atual apenas 3 portas sejam utilizadas em cada um, este modelo suporta a adição de novos módulos de interface, garantindo a escalabilidade futura para suportar as 6 sub-redes ou mais, conforme solicitado nos requisitos do projeto
>
> O plano de endereçamento IP também foi projetado com ampla capacidade para acomodar essas futuras sub-redes."

---

## Tabelas de Roteamento Estático

### Roteadores de Borda

- **Network:** 0.0.0.0
- **Mask:** 0.0.0.0
- **Para E1:** Next Hop -> 192.168.0.137 (A1)
- **Para E2:** Next Hop -> 192.168.0.141 (A1)
- **Para E3:** Next Hop -> 192.168.0.145 (A2)
- **Para E4:** Next Hop -> 192.168.0.149 (A2)

### Roteador A1

| Network      | Mask            | Next Hop      | Descrição                      |
| ------------ | --------------- | ------------- | ------------------------------ |
| 192.168.0.0  | 255.255.255.224 | 192.168.0.138 | Para alcançar a LAN do E1      |
| 192.168.0.32 | 255.255.255.224 | 192.168.0.142 | Para alcançar a LAN do E2      |
| 0.0.0.0      | 0.0.0.0         | 192.168.0.129 | Para todo o resto (lado de A2) |

### Roteador A2

| Network      | Mask            | Next Hop      | Descrição                      |
| ------------ | --------------- | ------------- | ------------------------------ |
| 192.168.0.64 | 255.255.255.224 | 192.168.0.146 | Para alcançar a LAN do E3      |
| 192.168.0.96 | 255.255.255.224 | 192.168.0.150 | Para alcançar a LAN do E4      |
| 0.0.0.0      | 0.0.0.0         | 192.168.0.133 | Para todo o resto (lado de A1) |

### Roteador C1

| Network       | Mask            | Next Hop      | Descrição           |
| ------------- | --------------- | ------------- | ------------------- |
| 192.168.0.0   | 255.255.255.224 | 192.168.0.130 | LAN de E1 (via A1)  |
| 192.168.0.32  | 255.255.255.224 | 192.168.0.130 | LAN de E2 (via A1)  |
| 192.168.0.136 | 255.255.255.252 | 192.168.0.130 | Link A1-E1 (via A1) |
| 192.168.0.140 | 255.255.255.252 | 192.168.0.130 | Link A1-E2 (via A1) |
| 192.168.0.64  | 255.255.255.224 | 192.168.0.134 | LAN de E3 (via A2)  |
| 192.168.0.96  | 255.255.255.224 | 192.168.0.134 | LAN de E4 (via A2)  |
| 192.168.0.144 | 255.255.255.252 | 192.168.0.134 | Link A2-E3 (via A2) |
| 192.168.0.148 | 255.255.255.252 | 192.168.0.134 | Link A2-E4 (via A2) |

---

## Documentação

**EXPLICAR MELHOR CADA PARTE DESDE O PADRÃO ATÉ A CAPACIDADE E SEUS USOS**

---

## Dispositivos

- **Roteadores:** CISCO 2901 com adição de portas para fibra optica
- **Switches:** CISCO 2960
- **Hosts:** PC
