# Programa para calcular a média das notas e verificar aprovação
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

# Recebendo as notas do aluno
notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)
status = verificar_aprovacao(media)

print(f"Média: {media:.2f}")
print(f"Status: {status}")

# Salvando os resultados em um arquivo
with open("resultado.txt", "w") as f:
    f.write(f"Média: {media:.2f}\n")
    f.write(f"Status: {status}")
