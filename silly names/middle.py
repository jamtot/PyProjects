"""Generate silly names by randomly combining names from 2 separate lists."""
import sys
import random

def silly():
    """Choose silly names at random from 2 tuples of names and print to screen."""
    print("Welcome to the silly name generator.'\n")
    print("Here's your silly name:\n\n")

    first = ('Analagous',
             'Billy', "Bill 'Beenie-Weenie'",
             'Bob', 'Boxelder',
             "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks',
             'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
             'Cleet', 'Cornbread', 'Crab Meat', 'Crapps',
             'Dark Skies', 'Dennis Clawhammer', 'Dicman',
             'Ding-Dong', 'Elphonso', 'Fancypants', 'Figgs',
             'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Hugh', 'Ignatious', 'Jimbo',
             'Joe', 'Johnny', 'Kash',
             'Lemongrass', 'Lil Debil', 'Longbranch',
             'Mergatroid', 'Mike', 'Moe',
             '"Mr Peabody"', 'Oinks',
             'Ovaltine', 'Paddy ', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut',
             'Sid', 'Skidmark', 'Slaps', 'Snakes',
             'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout',
             'Squids', 'Stinky', 'Storyboard', 'TeeTee',
             'Wheezy Joe', 'Whet', 'Winston', 'Worms')

    middle = ('Baby Oil', 'Bad News', 'Big Bum', 'Big Burps', 'Bowel Noises',
              'Jazz Hands', 'Lunch Money', 'Oil-Can', 'Old Scratch', 'Pottin Soil',
              'Stinkbug', 'Sweet Tea', 'The Knees', 'The Squirts')

    last = ('Appleyard', 'Bigmeat', 'Black', 'Bloominshine',
            'Boogerbottom', 'Breedslovetrout', 'Butterbaugh',
            'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott',
            'Faartz', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jass', 'Jefferson',
            'Jenkins', 'Jingley-Schmidt', 'Johnson', 'Kingfish',
            'Lester', 'Listenbee', 'Litoris', "M'Bembo", 'McFadden',
            'Money', 'Moonshine', 'Nettles', 'Noseworthy',
            'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson',
            'Pieplow', 'Pinkerton', 'Porkins', 'Putney',
            'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
            'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick',
            'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'White',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:
        first_name = random.choice(first)
        middle_name = (random.choice(middle)+' ' if random.randint(0, 2) == 1 else '')
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}{}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter or 'n' to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    silly()
