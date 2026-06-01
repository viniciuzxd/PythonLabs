# 🐍 Curso de Python 3 - Mundo 1, 2 e 3

Este diretório contém as minhas resoluções para os desafios propostos no **Curso de Python 3**, criado e disponibilizado gratuitamente pelo canal Curso em Vídeo.

## 📌 Sobre o Curso
Um dos cursos de Python mais populares e didáticos do Brasil. O curso é dividido em três "Mundos", guiando o aluno desde a instalação do ambiente e primeiros comandos, passando por estruturas de controle (condições e laços), até chegar em estruturas de dados compostas (listas, tuplas, dicionários), funções e modularização.

---

## 📂 Organização Estrutural (Mundo 3)

Para manter o repositório limpo, escalável e profissional, a reta final do Mundo 3 foi reestruturada saindo do modelo de arquivos soltos para uma arquitetura dividida por pilares de evolução. 

A estrutura de diretórios foi definida da seguinte forma:

```text
mundo_tres/
│
├── 01_funcoes/          # Desafios 096 a 106 (Escopo, parâmetros e PyHelp)
│   ├── ex096_area.py
│   └── ...
│
├── 02_modularizacao/    # Desafios 107 a 112 (Construção do pacote utilidadesCeV)
│   ├── teste.py         # Script principal de execução
│   └── utilidadesCeV/   # Pacote contendo os submódulos 'moeda' e 'dado'
│       ├── __init__.py
│       ├── dado/
│       └── moeda/
│
└── 03_erros_e_arquivos/ # Desafios 113 a 115 (Tratamento de exceções e persistência)
    ├── desafio113.py
    ├── desafio114.py
    └── desafio150
        └── projeto_cadastro/ # Sistema completo com banco de dados em texto simples
            ├── principal.py
            ├── interface/
            └── arquivo/ 
            
```

---

## 🏆 Progresso dos Desafios (A Jornada da Platina)

## 🌍 Mundo 1: Fundamentos Básicos
Nesta fase inicial, o foco foi entender a sintaxe base do Python, como a linguagem lida com variáveis, tipos primitivos e operações matemáticas, além de introduzir a lógica condicional simples.

### 🟢 Tipos Primitivos e Saída de Dados (Concluído)
- [x] **001** - Deixando tudo pronto
- [x] **002** - Respondendo ao Usuário
- [x] **003** - Somando dois números
- [x] **004** - Dissecando uma Variável
### 🟢 Operadores Aritméticos (Concluído)
- [x] **005** - Antecessor e Sucessor
- [x] **006** - Dobro, Triplo, Raiz Quadrada
- [x] **007** - Média Aritmética
- [x] **008** - Conversor de Medidas
- [x] **009** - Tabuada
- [x] **010** - Conversor de Moedas
- [x] **011** - Pintando Parede
- [x] **012** - Calculando Descontos
- [x] **013** - Reajuste Salarial
- [x] **014** - Conversor de Temperaturas
- [x] **015** - Aluguel de Carros
### 🟢 Utilizando Módulos/Bibliotecas (Concluído)
- [x] **016** - Quebrando um número
- [x] **017** - Catetos e Hipotenusa
- [x] **018** - Seno, Cosseno e Tangente
- [x] **019** - Sorteando um item na lista
- [x] **020** - Sorteando uma ordem na lista
- [x] **021** - Tocando um MP3
### 🟢 Manipulação de Texto (Strings) (Concluído)
- [x] **022** - Analisador de Textos
- [x] **023** - Separando dígitos de um número
- [x] **024** - Verificando as primeiras letras de um texto
- [x] **025** - Procurando uma string dentro de outra
- [x] **026** - Primeira e última ocorrência de uma string
- [x] **027** - Primeiro e último nome de uma pessoa
### 🟢 Condições Básicas (If/Else) (Concluído)
- [x] **028** - Jogo da Adivinhação v1.0
- [x] **029** - Radar eletrônico
- [x] **030** - Par ou Ímpar?
- [x] **031** - Custo da Viagem
- [x] **032** - Ano Bissexto
- [x] **033** - Maior e menor valores
- [x] **034** - Aumentos múltiplos
- [x] **035** - Analisando Triângulo v1.0

## 🌍 Mundo 2: Estruturas de Controle
O Mundo 2 foi dedicado ao controle de fluxo do programa. Aqui, aprofundei o uso de laços de repetição e lógicas condicionais complexas, essenciais para a construção de pequenos sistemas interativos e validação de dados.

### 🟢 Condições Aninhadas (Elif) (Concluído)
- [x] **036** - Aprovando Empréstimo
- [x] **037** - Conversor de Bases Numéricas
- [x] **038** - Comparando números
- [x] **039** - Alistamento Militar
- [x] **040** - Aquele clássico da Média
- [x] **041** - Classificando Atletas
- [x] **042** - Analisando Triângulos v2.0
- [x] **043** - Índice de Massa Corporal
- [x] **044** - Gerenciador de Pagamentos
- [x] **045** - GAME: Pedra Papel e Tesoura
### 🟢 Laços de Repetição (For) (Concluído)
- [x] **046** - Contagem regressiva
- [x] **047** - Contagem de pares
- [x] **048** - Soma ímpares múltiplos de três
- [x] **049** - Tabuada v2.0
- [x] **050** - Soma dos pares
- [x] **051** - Progressão Aritmética
- [x] **052** - Números primos
- [x] **053** - Detector de Palíndromo
- [x] **054** - Grupo da Maioridade
- [x] **055** - Maior e menor da sequência
- [x] **056** - Analisador completo
### 🟢 Laços de Repetição (While) (Concluído)
- [x] **057** - Validação de Dados
- [x] **058** - Jogo da Adivinhação v2.0
- [x] **059** - Criando um Menu de Opções
- [x] **060** - Cálculo do Fatorial
- [x] **061** - Progressão Aritmética v2.0
- [x] **062** - Super Progressão Aritmética v3.0
- [x] **063** - Sequência de Fibonacci v1.0
- [x] **064** - Tratando vários valores v1.0
- [x] **065** - Maior e Menor valores
### 🟢 Interrompendo Repetições (Break) (Concluído)
- [x] **066** - Vários números com flag
- [x] **067** - Tabuada v3.0
- [x] **068** - Jogo do Par ou Ímpar
- [x] **069** - Análise de dados do grupo
- [x] **070** - Estatísticas em produtos
- [x] **071** - Simulador de Caixa Eletrônico

## 🌍 Mundo 3: Estruturas Compostas
O Mundo 3 marca a transição para estruturas de dados mais complexas. O objetivo é aprender a armazenar, organizar e manipular múltiplos dados de forma eficiente na memória do computador.

### 🟢 Tuplas (Concluído)
- [x] Desafio 072: Número por Extenso
- [x] Desafio 073: Tuplas com Times de Futebol
- [x] Desafio 074: Maior e menor valores em Tupla
- [x] Desafio 075: Análise de dados em uma Tupla
- [x] Desafio 076: Lista de Preços com Tupla
- [x] Desafio 077: Contando vogais em Tupla

### 🟢 Listas - Parte 1 (Concluído)
- [x] Desafio 078: Maior e Menor valores na Lista
- [x] Desafio 079: Valores únicos em uma Lista
- [x] Desafio 080: Lista ordenada sem repetições
- [x] Desafio 081: Extraindo dados de uma Lista
- [x] Desafio 082: Dividindo valores em várias Listas
- [x] Desafio 083: Validando expressões matemáticas

### 🟢 Listas - Parte 2: Listas Compostas (Concluído)
- [x] Desafio 084: Lista composta e análise de dados
- [x] Desafio 085: Listas com pares e ímpares
- [x] Desafio 086: Matriz em Python
- [x] Desafio 087: Mais sobre Matriz em Python
- [x] Desafio 088: Palpites para a Mega Sena
- [x] Desafio 089: Boletim com listas compostas

### 🟢 Dicionários (Concluído)
- [x] Desafio 090: Dicionário em Python
- [x] Desafio 091: Jogo de Dados em Python
- [x] Desafio 092: Cadastro de Trabalhador em Python
- [x] Desafio 093: Cadastro de Jogador de Futebol
- [x] Desafio 094: Unindo dicionários e listas
- [x] Desafio 095: Aprimorando os Dicionários

### 🟢 Funções - Parte 1 (Concluído)
- [x] Desafio 096: Função que calcula área
- [x] Desafio 097: Um print especial (Formatador de CLI)
- [x] Desafio 098: Função de Contador (Validação de Edge Cases)
- [x] Desafio 099: Função que descobre o maior (Empacotamento de parâmetros)
- [x] Desafio 100: Funções para sortear e somar (Passagem por referência)

- [x] Desafio 101: Funções para votação
- [x] Desafio 102: Função para Fatorial
- [x] Desafio 103: Ficha do Jogador
- [x] Desafio 104: Validando entrada de dados em Python
- [x] Desafio 105: Analisando e gerando Dicionários
- [x] Desafio 106: Sistema interativo de ajuda em Python

### 🟢 Modularização e Pacotes
- [x] Desafio 107: Exercitando módulos em Python
- [x] Desafio 108: Formatando Moedas em Python
- [x] Desafio 109: Formatando Moedas em Python (Aperfeiçoado)
- [x] Desafio 110: Reduzindo ainda mais seu programa
- [x] Desafio 111: Transformando módulos em pacotes
- [x] Desafio 112: Entrada de dados monetários

### 🟢 Tratamento de Erros e Projetos Finais
- [x] Desafio 113: Funções aprofundadas em Python
- [x] Desafio 114: Site está acessível?
- [x] Desafio 115a: Criando um menu
- [x] Desafio 115b: Arquivos com Python
- [x] Desafio 115c: Finalizando o projeto