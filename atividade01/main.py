maior_altura = 0
menor_altura = 999
soma_altura_masculino = 0
contador_masculino = 0
contador_feminino = 0

for i in range(1, 16):
    print(f"\nPessoa {i}")

    altura = float(input("Digite a altura (em metros, ex: 1.75): "))
    genero = input("Digite o gênero (M para Masculino / F para Feminino): ").strip().upper()

    
    while genero != "M" and genero != "F":
        genero = input("Gênero inválido! Digite M ou F: ").strip().upper()


    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura


    if genero == "M":
        soma_altura_masculino += altura
        contador_masculino += 1


    if genero == "F":
        contador_feminino += 1


if contador_masculino > 0:
    media_masculino = soma_altura_masculino / contador_masculino
else:
    media_masculino = 0

print("\n===== RESULTADOS =====")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_masculino:.2f} m")
print(f"Número de mulheres: {contador_feminino}")