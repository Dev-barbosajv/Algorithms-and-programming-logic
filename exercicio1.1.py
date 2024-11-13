from colorama import Fore, Back, Style


def main():
    
    new_moedas = float(input("inserir nova moeda:"))

    arr_moedas = [
        1.20,
        2.50,
        2.43,
        4.30,
        1.20
    ]

    arr_moedas.append(new_moedas)

    for moeda in arr_moedas:
        if moeda > 2.43:
            print(Fore.RED + f"Essa Moeda é falsa: {moeda}")

        elif moeda == 2.43:
            print(Fore.GREEN + f"Essa Moeda é a verdadeira: {moeda}")

        else:
            print(Fore.RED + f"Essa moeda é falsa {moeda}")


if __name__ == "__main__":
    main()