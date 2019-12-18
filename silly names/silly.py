"""Generate silly names by randomly combining names from 2 separate lists."""
import sys
import random

def silly():
    """Choose silly names at random from 2 tuples of names and print to screen."""
    print("Welcome to the silly name generator.'\n")
    print("Here's your silly name:\n\n")

    first = ('Analagous', 'Baby Oil', 'Bad News',
             'Big Bum Billy', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder',
             "Bud 'Lite' ", 'Butterbean', 'Buttermilk', 'Buttocks',
             'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
             'Cleet', 'Cornbread', 'Crab Meat', 'Crapps',
             'Dark Skies', 'Dennis Clawhammer', 'Dicman',
             'Ding-Dong', 'Elphonso', 'Fancypants', 'Figgs',
             'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Hugh', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Kash',
             'Lemongrass', 'Lil Debil', 'Longbranch',
             '"Lunch Money"', 'Mergatroid', 'Mike', 'Moe',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
             'Ovaltine', 'Paddy "The Knees"', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut',
             "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes',
             'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout',
             'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee',
             'Wheezy Joe', 'Whet', "Winston 'Jazz Hands'", 'Worms')

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
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter or 'n' to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    silly()
