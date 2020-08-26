import csv
import json
import time
import shutil


def modify_pokemon():
    all_pokemons = []
    with open("./pokemon/pokemon.csv") as file:
        reader = csv.reader(file)
        headers = reader.__next__()

        for row in reader:
            # Truque secreto para mergear duas listas em um dict
            # sendo uma de chaves e outra de valores
            pokemon = dict(zip(headers, row))

            pokemon["_id"] = int(pokemon.pop("#"))

            pokemon["types"] = [pokemon.pop("Type 1")]

            # Caso tenha algum valor no "Type 2", adicionamos ao array "types"
            type2 = pokemon.pop("Type 2")
            if type2 != "":
                pokemon["types"].append(type2)

            pokemon["name"] = pokemon.pop("Name")
            # Convertendo o Legendary para boleano
            pokemon["legendary"] = True if pokemon.pop("Legendary") == "True" else False

            # Apenas nos livrando de atributos que não vamos utilizar de maneira segura
            pokemon.pop("Sp. Atk")
            pokemon.pop("Sp. Def")

            # Uma iteração para passar para letras minúsculas e converter
            # para número inteiro.
            for key in ("HP", "Attack", "Defense", "Speed", "Generation"):
                pokemon[key.lower()] = int(pokemon.pop(key))
            all_pokemons.append(pokemon)

    # Gravando o arquivo novo, que vai ser importado pelo mongo
    with open("./data/pokemon.json", "w") as file:
        json.dump(all_pokemons, file, indent=2)

    # Fazendo uma cópia simples do arquivo combats.csv
    shutil.copy("./pokemon/combats.csv", "./data/combats.csv")


def modify_netflix():
    all_movies = []
    with open("./netflix/netflix_titles.csv") as file:
        reader = csv.reader(file)
        headers = reader.__next__()

        for row in reader:
            movie = dict(zip(headers, row))

            movie["_id"] = int(movie.pop("show_id"))

            # Convertendo para uma ISODate, forma recomendada de
            # registrar valores de data no Mongo DB
            if movie["date_added"]:
                time_struct = time.strptime(movie["date_added"].strip(), "%B %d, %Y")
                iso_date = time.strftime("%Y-%m-%dT%H:%M:%SZ", time_struct)
                movie["date_added"] = iso_date
            else:
                movie.pop("date_added", None)

            # Separando os valores de texto com vírgulas para os arrays
            # As duas formas produzem o mesmo resultado nesse caso
            movie["cast"] = list(map(str.strip, movie.pop("cast").split(",")))
            movie["countries"] = [s.strip() for s in movie.pop("country").split(",")]
            movie["directors"] = [s.strip() for s in movie.pop("director").split(",")]
            movie["listed_in"] = [s.strip() for s in movie.pop("listed_in").split(",")]

            movie["release_year"] = int(movie["release_year"])

            all_movies.append(movie)

    with open("./data/netflix.json", "w") as file:
        json.dump(all_movies, file, indent=2)


modify_pokemon()
modify_netflix()
