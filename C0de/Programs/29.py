import tkinter as tk
from random import shuffle

# Define the card suits and ranks
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a deck of cards
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Shuffle the deck
shuffle(deck)

# Create a tkinter window
window = tk.Tk()
window.title("29 Card Game")

# Create a label to display the cards
card_label = tk.Label(window, font=('Arial', 14), wraplength=300, justify='left')
card_label.pack()

def deal_card():
    # Deal a card from the deck
    if deck:
        card = deck.pop()
        card_label.config(text=card)
    else:
        card_label.config(text="No more cards!")

# Create a button to deal a card
deal_button = tk.Button(window, text="Deal Card", command=deal_card)
deal_button.pack()

# Start the tkinter event loop
window.mainloop()
