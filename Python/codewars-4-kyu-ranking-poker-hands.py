from collections import Counter

def is_low_straight(ranks):
    return sorted(ranks) ==  sorted(["A", "2", "3", "4", "5"])

def is_straight(ranks):
    return sorted(ranks) in [
        sorted(["2", "3", "4", "5", "6"]),
        sorted(["3", "4", "5", "6", "7"]),
        sorted(["4", "5", "6", "7", "8"]),
        sorted(["5", "6", "7", "8", "9"]),
        sorted(["6", "7", "8", "9", "T"]),
        sorted(["7", "8", "9", "T", "J"]),
        sorted(["8", "9", "T", "J", "Q"]),
        sorted(["9", "T", "J", "Q", "K"]),
        sorted(["T", "J", "Q", "K", "A"])
        ]

class PokerHand():

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        
        self.suits = ['H', 'S', 'D', 'C']
        self.values = ['2', '3', '4', '5', '6', '7', '8',
                  '9', 'T', 'J', 'Q', 'K', 'A']
        self.combinations = ['high_card', 'pair', 'two_pairs', 'three_of_a_kind', 'low_straight',
                        'straight', 'flush', 'full_house', 'four_of_a_kind',
                        'low_straight_flush','straight_flush']
        self.hand = hand

    def get_combination(self):
    
        suits = [card[1] for card in self.hand.split(' ')]  # Получаем список мастей карт
        ranks = [card[0] for card in self.hand.split(' ')]  # Получаем список номиналов карт
        combination = 'high_card'
        ranks_count = Counter(ranks)
        if len(set(suits)) == 1 and is_low_straight(ranks):
            combination = "low_straight_flush"
        elif len(set(suits)) == 1 and is_straight(ranks):
            combination = "straight_flush"
        elif len(set(ranks)) == 2:
            for rank in set(ranks):
                if ranks.count(rank) == 4:
                    combination = "four_of_a_kind"
                elif ranks.count(rank) == 3:
                    combination = "full_house"
        elif len(set(suits)) == 1:
            combination = "flush"
        elif is_straight(ranks):
            combination = "straight"
        elif is_low_straight(ranks):
            combination = "low_straight"
        elif 3 in ranks_count.values():
            combination = 'three_of_a_kind'
        elif 2 in ranks_count.values() and len(ranks_count) == 3:
            combination = 'two_pairs'
        elif 2 in ranks_count.values():
            combination = 'pair'    
        value = [self.combinations.index(combination)*1000]
        for card in ranks:
            value.append(self.values.index(card))
        return sorted(value, reverse=True)
  
    def compare_with(self, opponent):
        player_value = self.get_combination()
        opponent_value = opponent.get_combination()
        print(player_value, opponent_value)
        if player_value > opponent_value:
            return "Win"
        elif player_value == opponent_value:
            return "Tie"
        else:
            return "Loss"

player, opponent = PokerHand('2S 2H 4H 5S 4C'), PokerHand('AH AC 5H 6H 7S')
print(player.compare_with(opponent))

player, opponent = PokerHand('JH 8S TH AH QH'), PokerHand('KD 6S 9D TH AD')
print(player.compare_with(opponent))

