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
            pokemon = dict(zip(headers, row))
            pokemon["_id"] = int(pokemon.pop("#"))

            pokemon["types"] = [pokemon.pop("Type 1")]
            type2 = pokemon.pop("Type 2")
            if type2 != "":
                pokemon["types"].append(type2)

            pokemon["name"] = pokemon.pop("Name")
            pokemon["legendary"] = True if pokemon.pop("Legendary") == "True" else False

            pokemon.pop("Sp. Atk")
            pokemon.pop("Sp. Def")

            for key in ("HP", "Attack", "Defense", "Speed", "Generation"):
                pokemon[key.lower()] = int(pokemon.pop(key))
            all_pokemons.append(pokemon)

    with open("./data/pokemon.json", "w") as file:
        json.dump(all_pokemons, file, indent=2)

    shutil.copy("./pokemon/combats.csv", "./data/combats.csv")


def modify_netflix():
    all_movies = []
    with open("./netflix/netflix_titles.csv") as file:
        reader = csv.reader(file)
        headers = reader.__next__()

        for row in reader:
            movie = dict(zip(headers, row))

            movie["_id"] = int(movie.pop("show_id"))

            if movie["date_added"]:
                time_struct = time.strptime(movie["date_added"].strip(), "%B %d, %Y")
                iso_date = time.strftime("%Y-%m-%dT%H:%M:%SZ", time_struct)
                movie["date_added"] = iso_date
            else:
                movie.pop("date_added", None)

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
