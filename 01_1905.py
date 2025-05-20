# lista
numeros = []

# ponto de partida de operações
soma = 0
quantidade_total = 0

# coleta de dados 
for i in range(7):
    num = int(input("Digite um número: "))
    numeros.append(num)
    quantidade_total += 1
    soma += num

# calculo da média
media = soma / quantidade_total

# cálculo do maior, menor e contagem acima da média
maior = max(numeros)
menor = min(numeros)
acima_da_media = 0

for n in numeros:
    if n > media:
        acima_da_media += 1

# saídas
print(f"Números digitados: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media:.2f}")
print(f"{acima_da_media} número(s) estão acima da média.")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")