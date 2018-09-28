def bday(age):
    ordinal=""
    if str(age)[-1] == '1' and age != 11:
        ordinal = "st"
    elif str(age)[-1] == '2' and age != 12:
        ordinal = "nd"
    elif str(age)[-1] == '3' and age != 13:
        ordinal = "rd"
    else:
        ordinal = "th"

    print("Happy "+str(age)+ ordinal+ " Birthday")

def nm(name):
    name_l = name.split()
    print(name_l[-1])
    print(name_l[0])
    name_l.reverse()
    print((" ").join(name_l))
    l = input("Insert a letter to search for in the name-> ")
    print("'"+ l+ "'" +" appears " + str(l_count(l[0], name)) + " times.")

def l_count(letter, name):
    return sum([1 for x in name if x==letter])

def draw_grid(row, column):
    grid=""
    for x in range(row):
        grid+=(" ---"*column)
        grid+="\n"
        grid+=("|   "*column)
        grid+="|\n"
    grid+=(" ---"*column)
    print(grid)

def draw_box(width, height):
    box=""
    box+=("-"*width)
    box+='\n'
    for y in range(height):
        box+="|"
        box+=" "*(width-2)
        box+="|\n"
    box+=("-"*width)
    print(box)