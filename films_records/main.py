from film import Film
from serie import Serie

if __name__ == '__main__':
    harry_potter = Film("harry potter e a pedra filosofal", 2000, 160)
    game_of_throne = Serie("game of throne", 2013, 7)
    print(f'Filme - Título: {harry_potter.title}, Ano: {harry_potter.year}, Duração: {harry_potter.duration}, gostei: {harry_potter.like}')
    print(f'Serie - Título: {game_of_throne.title}, Ano: {game_of_throne.year}, Temporadas: {game_of_throne.session}, gostei: {game_of_throne.like}')
