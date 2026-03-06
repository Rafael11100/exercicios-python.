# Tabelas de carros em Python

economicos = [
    ["Marca", "Modelo", "Ano"],
    ["Fiat", "Uno", 2015],
    ["Volkswagen", "Gol", 2018],
    ["Chevrolet", "Onix", 2020]
]

esportivos = [
    ["Marca", "Modelo", "Ano"],
    ["Ferrari", "488", 2022],
    ["Lamborghini", "Huracan", 2021],
    ["Porsche", "911", 2023]
]

suvs = [
    ["Marca", "Modelo", "Ano"],
    ["Toyota", "Hilux SW4", 2022],
    ["Jeep", "Compass", 2021],
    ["Hyundai", "Creta", 2023]
]

def mostrar_tabela(nome, tabela):
    print("\n====", nome, "====")
    for linha in tabela:
        print("{:<12} {:<12} {:<6}".format(*linha))

mostrar_tabela("Carros Econômicos", economicos)
mostrar_tabela("Carros Esportivos", esportivos)
mostrar_tabela("SUVs", suvs)