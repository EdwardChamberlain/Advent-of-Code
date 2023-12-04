import sys
import os

class Game:
    def __init__(self, game_string) -> None:
        game_number_string, results = game_string.split(':')
        games = results.split(';')
        games = [g.split(', ') for g in games]
        games = [
            {
                pull.strip().split(' ')[1]: int(pull.strip().split(' ')[0])
                for pull in g
            }
            for g in games
        ]

        self.id = int(game_number_string[5:])
        self.games = games

    @property
    def power(self):
        return self.min_known_colour('red') * self.min_known_colour('green') * self.min_known_colour('blue')

    def min_known_colour(self, colour):
        return max([
            i[colour]
            for i in self.games
            if colour in i
        ])


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
data = data.split('\n')
data = [Game(d) for d in data]

# Pt 1
result = []
for g in data:
    if g.min_known_colour('red') > 12:
        continue

    if g.min_known_colour('green') > 13:
        continue

    if g.min_known_colour('blue') > 14:
        continue
    
    result.append(g.id)

print(sum(result))

# Pt 2
result = [g.power for g in data]
print(sum(result))