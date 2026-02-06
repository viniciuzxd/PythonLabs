# =====================================================
# GUIA DE APRENDIZADO: VARIÁVEIS E CÁLCULOS EM PYTHON
# =====================================================

# 1. TIPOS DE VARIÁVEIS (Data Types)
nome = "Python"           # str  (String): Textos, sempre entre aspas.
idade = 25                # int  (Integer): Números inteiros.
altura = 1.75             # float (Floating Point): Números decimais (usa-se ponto).
estudando = True          # bool (Boolean): Verdadeiro (True) ou Falso (False).

# 2. CONVERSÃO DE TIPOS (Casting)
# Útil quando você recebe um dado do input() que vem sempre como texto.
texto_numero = "10"
inteiro = int(texto_numero)    # Converte string para inteiro
decimal = float("10.5")        # Converte string para float
palavra = str(100)             # Converte número para string

# 3. OPERADORES ARITMÉTICOS (Cálculos)
soma = 10 + 5            # Resultado: 15
subtracao = 10 - 5       # Resultado: 5
multiplicacao = 10 * 5   # Resultado: 50
divisao = 10 / 3         # Resultado: 3.333... (sempre retorna float)

# Operadores Especiais:
potencia = 2 ** 3        # Resultado: 8 (2 elevado a 3)
divisao_inteira = 10 // 3 # Resultado: 3 (descarta o que vem após a vírgula)
resto_divisao = 10 % 3   # Resultado: 1 (o que sobra da divisão)

# 4. FORMATAÇÃO DE TEXTO (f-strings)
# A melhor forma de exibir resultados misturando texto e variáveis
print(f"O nome é {nome} e a altura é {altura:.2f}m.")

# 5. ENTRADA DE DADOS
# Todo input() entra como STRING, por isso usamos int() ou float() em volta
valor = float(input("Digite um valor para calcular o dobro: "))
print(f"O dobro de {valor} é {valor * 2}")

# =====================================================
# DICA: Use o comando type(variavel) para saber o tipo dela!
# Exemplo: print(type(altura)) -> <class 'float'>