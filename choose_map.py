import random

maps = {"Especial": 1, "Mirage": 2,  "Dust II": 3, "inferno": 4, "Cache": 5, "Vertigo": 6,
        "Ancient": 7, "Overpass": 8, "Train": 9, "Basalt": 10, "Agency": 11, "Office": 12, "Insertion II": 13}


def print_all_maps():
    print("Estes são os mapas disponíveis: ", "\n")
    for key, value in maps.items():
        print(value, ": ", key)
    print("")


def choose_map_pool():
    chosen_maps = [i for i in range(1, 14)]

    want_to_edit = input(
        "Você quer fazer alguma alteração no map pool? (S/N) ").lower()
    if (want_to_edit == "n"):
        return chosen_maps

    removed = [int(item)
               for item in input("Quais mapas você quer remover? ").split()]

    chosen_maps = [i for i in chosen_maps if (i not in removed)]

    while (True):
        want_to_edit = input(
            "Você quer fazer mais alguma alteração no map pool? (S/N) ").lower()
        if (want_to_edit == "n"):
            break

        add_or_remove = input(
            "Você quer adicionar ou remover mapas? (A/R) ").lower()
        if (add_or_remove == "r"):
            removed = [int(item) for item in input(
                "Quais mapas você quer remover? ").split()]
            for i in removed:
                if (i in chosen_maps):
                    chosen_maps.remove(i)
        if (add_or_remove == "a"):
            added = [int(item) for item in input(
                "Quais mapas você quer adicionar? ").split()]
            for i in added:
                if (i not in chosen_maps):
                    chosen_maps.append(i)

    return chosen_maps


def show_map_pool(chosen_maps):
    print("Estes são os mapas escolhidos: ", "\n")
    for key, value in maps.items():
        if (value in chosen_maps):
            print(value, ": ", key)


def select_random_maps(chosen_maps):
    num_of_maps = int(input(
        f"Quantos mapas você quer que sejam selecionados? (1 - {len(chosen_maps)}) "))
    while (num_of_maps > len(chosen_maps) or num_of_maps < 1):
        print(f"O número de mapas deve estar entre 1 e {len(chosen_maps)} ")
        num_of_maps = int(input(
            f"Quantos mapas você quer que sejam selecionados? (1 - {len(chosen_maps)}) "))

    return random.choices(chosen_maps, k=num_of_maps)


def show_final_selection(selected_list):
    print("Esta é a seleção final: ", "\n")
    for key, value in maps.items():
        if (value in selected_list):
            print(value, ": ", key)


if __name__ == '__main__':
    print_all_maps()
    chosen_maps = choose_map_pool()
    show_map_pool(chosen_maps)
    selected_list = select_random_maps(chosen_maps)
    show_final_selection(selected_list)
