def car_in():
    for i in range(len(park)):
        for c in range(len(park[i])):
            if park[i][c] == "L":
                park[i][c] = "O"
                return  # Sai da função após preencher o primeiro "L" encontrado

# Chamar a função várias vezes e imprimir o estado da matriz após cada chamada
park = [["L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L"]]

# Número de chamadas para testar a função
for _ in range(10):
    car_in()
    print(park)  # Imprime o estado da matriz após cada chamada