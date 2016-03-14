import random
from datetime import datetime
random.seed(datetime.now())


def num_generator(nums, min, max, has_bonus = True):
    numbers = []
    for i in xrange(nums):
        randy = random.randint(min,max)
        while randy in numbers:
            randy = random.randint(min,max)
        numbers+=[randy]
        numbers = sorted(numbers)
    if (has_bonus):
        bonus = random.randint(min,max)
        while bonus in numbers:
            bonus = random.randint(min,max)
        return numbers, bonus
    else:
        return numbers

def generate_num(min,max):
    return random.randint(min,max)

def take_input(draw_balls, draw_min, draw_max, nums = []):
    print "Please enter %d numbers between %d and %d: " % (draw_balls, draw_min, draw_max)
    input = raw_input()

    if input is '':
        for i in xrange(draw_balls):
            num = generate_num(draw_min, draw_max)            
            while num in nums:
                num = generate_num(draw_min, draw_max)
            nums.append(num) 
    else:
        num_strings = input.split()
        for num in num_strings:
            if num.isdigit():
                num = int(num)
                if num >= draw_min and num <= draw_max:
                    if num not in nums:
                        nums.append(num)
    return nums

def run_till_win(quick_pick = True):
    import time

    start_time = time.time()

    draw_min = 1 
    draw_max = 47
    draw_balls = 6

    draw, bonus = num_generator(draw_balls, draw_min, draw_max)
    if quick_pick:
        nums = num_generator(draw_balls, draw_min, draw_max, False)
    else: 
        nums = take_input(draw_balls, draw_min, draw_max)

        if len(nums) < draw_balls:
            while len(nums) < draw_balls:
                 nums=take_input(draw_balls-len(nums), draw_min, draw_max, nums)
        if len(nums) > draw_balls:
            print "Too many numbers given. Taking the first %d entered." % draw_balls
            nums = nums[:draw_balls]

        nums = sorted(nums)

    draws_entered = 0
    
    while sorted(draw) != sorted(nums): 
        draws_entered+=1
        draw, bonus = num_generator(draw_balls, draw_min, draw_max)
        elapsed = time.time() - start_time
        mins = 0
        if elapsed % 60 == 0:
            mins+=1
            print "%d mins elapsed." % mins
        #if quick_pick:
        #    nums = num_generator(draw_balls, draw_min, draw_max, False)
    time = ''
    if draws_entered < (52*2): time = "%d weeks" % draws_entered/2
    elif draws_entered >= (52*2) and draws_entered < (52*2)*100: time = "%.2f years" % float(draws_entered/(52.*2.))
    elif draws_entered >= (52*2)*100: time = "%.2f centuries" % float(draws_entered/(52.*2.*100.))

    print """You finally won the jackpot after %d games played. 
If you played twice a week, at 2 euro a pop, you spent %s playing, and %d euros.""" % (
        draws_entered, time, draws_entered*2)

def do_lotto(draw_min = 1, draw_max = 47, draw_balls = 6):
    draw, bonus = num_generator(draw_balls, draw_min, draw_max)

    nums = take_input(draw_balls, draw_min, draw_max)

    if len(nums) < draw_balls:
        while len(nums) < draw_balls:
             nums=take_input(draw_balls-len(nums), draw_min, draw_max, nums)
    if len(nums) > draw_balls:
        print "Too many numbers given. Taking the first %d entered." % draw_balls
        nums = nums[:draw_balls]

    nums = sorted(nums)

    print "The lotto draw is:"
    print "%r bonus: %d" % (draw, bonus)
    print "Your numbers are:"
    print nums
    
    has_bonus = False
    matched = 0
    if bonus in nums:
            has_bonus = True
    for num in nums:
        if num in draw:
            matched+=1
    string = '.'
    if has_bonus:
        string = "and the bonus ball."
    print ("You matched %d numbers"+string) % matched
    
    winnings = "nothing."
    if matched == 6:
        winnings = "2 million Euros!"
    elif matched == 5:
        if has_bonus:
            winnings = "100,000 Euros!"
        else:
            winnings = "1,500 Euros!"
    elif matched == 4:
        if has_bonus:
            winnings = "150 Euros!"
        else: winnings = "50 Euros!"
    elif matched == 3:
        if has_bonus:
            winnings = "25 euros!"
        else: winnings = "9 euro."
    elif matched == 2:
        if has_bonus:
            winnings = "a 3 euro scratchcard."
 
    print "You have just won %s Congratulations!" % winnings

if __name__ == "__main__":
    #do_lotto()
    run_till_win()
        


