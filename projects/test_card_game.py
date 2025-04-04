from card_game import WarGame, Deck, Card

def test_play_auto():
    game = WarGame("A", "B")
    game.play_auto(max_rounds=1000)

def test_win():
    game = WarGame("A", "B")
    fixed_deck = Deck()
    fixed_deck.shuffle()
    hand1, hand2 = fixed_deck.deal()
    hand1 += hand2
    hand2.clear()
    high_card = hand1.pop()
    while high_card.value == 2:
        hand1.insert(0, high_card)
        high_card = hand1.pop()
    for card in hand1:
        if card < high_card:
            hand2.append(card)
            hand1.remove(card)
            break
    hand1.append(high_card)
    game.set_hands(hand1, hand2)
    game.play_auto()
    assert len(game.player2.hand) == 0

def test_end_on_war():
    game = WarGame("A", "B")
    fixed_deck = Deck()
    fixed_deck.shuffle()
    hand1, hand2 = fixed_deck.deal()
    hand1 += hand2
    hand2.clear()
    high_card = hand1.pop()
    for card in hand1:
        if card == high_card:
            hand2.append(card)
            hand1.remove(card)
            break
    hand1.append(high_card)
    game.set_hands(hand1, hand2)
    game.play_auto()
    assert len(game.player2.hand) == 0

if __name__ == "__main__":
    # test_play_auto()
    # test_win()
    test_end_on_war()


# come up with an idea or two for what I want to do for capstone
### Double check requirements