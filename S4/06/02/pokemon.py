import requests

"""
V1_
class PokemonMapper():
    def __init__(self,base_url,limit):
        self.base_url = base_url
        self.limit = limit
        self.pokemons = []

    def fetch_pokemons(self):
        try:
            response = requests.get(f"{self.base_url}?limit={self.limit}")
            response.raise_for_status()  # Esto lanzará una excepción si la solicitud no fue exitosa
            data = response.json()
            self.pokemons = data['results']
            print(f"Successfully fetched {len(self.pokemons)} Pokémon(s).")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Pokémon data: {e}")

"""
""" V2_
import requests

class PokemonMapper:
    def __init__(self, base_url, limit):
        self._base_url = base_url
        self._limit = limit
        self._pokemons = []

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    @property
    def pokemons(self):
        return self._pokemons

    def fetch_pokemons(self):
        try:
            response = requests.get(f"{self.base_url}?limit={self.limit}")
            response.raise_for_status()
            data = response.json()
            self._pokemons = data['results']
            print(f"Successfully fetched {len(self._pokemons)} Pokémon(s).")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Pokémon data: {e}")
"""
# V3_
import requests

class PokemonMapper:
    def __init__(self, base_url, limit):
        self._base_url = base_url
        self._limit = limit
        self._pokemons = []

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    @property
    def pokemons(self):
        return self._pokemons

    def fetch_pokemons(self):
        try:
            print(f"Obteniendo Pokemon de la Url:{self.base_url}...")
            response = requests.get(f"{self.base_url}?limit={self.limit}")
            response.raise_for_status()
            data = response.json()
            self._pokemons = data['results']
            print(f"Successfully fetched {len(self._pokemons)} Pokémon(s).")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Pokémon data: {e}")


