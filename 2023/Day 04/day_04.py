import os
import sys
import collections


class Card:
    def __init__(self, string: str) -> None:
        self.id, string = string.split(':')
        self.winning_numbers, self.card_numbers = string.split('|')

        self.id = int(self.id.split()[1]) - 1
        self.winning_numbers = list(map(int, self.winning_numbers.strip().split()))
        self.card_numbers = list(map(int, self.card_numbers.strip().split()))

    @property
    def matched_numbers(self):
        return list(set(self.winning_numbers).intersection(self.card_numbers))

    @property
    def matched_numbers_count(self):
        return len(self.matched_numbers)
    
    @property
    def score(self):
        if (x := 2 ** (self.matched_numbers_count - 1)) == 0.5:
            return 0

        else:
            return x
        
    @property
    def cards_won(self):
        start = self.id + 1
        stop = start + self.matched_numbers_count
        return list(range(start, stop))

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')

cards = [Card(d) for d in data]

# Pt 1
scores = [c.score for c in cards]
print(sum(scores))

# Pt 2
cards_qty = {
    c.id: 1
    for c in cards
}
for c in cards:
    for won_c in c.cards_won:
        cards_qty[won_c] += cards_qty[c.id]


print(sum(cards_qty.values()))
