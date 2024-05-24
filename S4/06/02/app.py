from pokemom import PokemonMapper

base_url = "https://pokeapi.co/api/v2/pokemon"
limit = 20
pokemon_mapper = PokemonMapper(base_url, limit)
pokemon_mapper.fetch_pokemons()


for pokemon in pokemon_mapper.pokemons:
    print(pokemon['name'])