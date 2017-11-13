"""	author Jonathan Morris
# questions are from http://www.pubquizarea.com/view_question_and_answer_quizzes.php?cat_title=general-knowledge&type_title=multiple-choice&cat=32&type=1&&id=6284
# && http://www.pubquizarea.com/view_question_and_answer_quizzes.php?cat_title=general-knowledge&type_title=multiple-choice&cat=32&type=1&&id=6272
"""

input = """1. What is the name of the dance troupe formed by Dublin-born Margaret Kelly in Paris in 1932?
 
Bluebell Girls (C)
Daffodil Girls
Daisy Girls
Lily Girls"""

endproduct = """questions.push_back(Question("What is the name of the dance troupe formed by Dublin-born Margaret Kelly in Paris in 1932?", aPair("Bluebell Girls", 1), aPair("Daffodil Girls", 0), aPair("Daisy Girls", 0), aPair("Lily Girls", 0)));"""

questions = ["""1. What is the name of the dance troupe formed by Dublin-born Margaret Kelly in Paris in 1932?
 
Bluebell Girls (C)
Daffodil Girls
Daisy Girls
Lily Girls""","""2. Which TV soap features the Beale and Mitchell families?
 
Coronation Street
EastEnders (C)
Emmerdale
Hollyoaks""","""3. The small republic of San Marino is completely surrounded by which larger country?
 
India
Iran
Israel
Italy (C)""","""4. What was the name of Robert Maxwell's luxury yacht, from which he fell overboard in 1991?
 
Lady Chatterley
Lady Ghislaine (C)
Lady Godiva
Lady of Shalott""","""5. Something described as 'tactile' means that it relates to which of the senses?
 
Hearing
Sight
Taste
Touch (C)""","""6. The words of which song title appear on the Shankly Gates at Liverpool FC's Anfield stadium?
 
Abide With Me
Follow That Dream
My Way
You'll Never Walk Alone (C)""","""7. According to Greek mythology, after Pandora had opened her box to release all the evils of the world, what remained inside after she'd closed it again?
 
Charity
Faith
Hope (C)
Love""","""8. In US law enforcement agencies, what do the initials stand for in SWAT team?
 
Special War Against Terror
Special Weapons And Tactics (C)
Special Women's Assimilation Test
Special Wrongdoers' Arrest Treatment""","""9. In Treasure Island, Jim Hawkins is hiding in a barrel of what when he overhears Long John Silver's plan to take over the Hispaniola and murder its officers?
 
Apples (C)
Beer
Flour
Rum""","""10. When Premium Bonds were introduced in 1956, an individual bond cost how much?
 
1 (C)
10
20
50"""]

questions2=[
"""1. In bullfighting, what name is given to the horseman who jabs the bull with a lance?
 
Picador (C)
Picaroon
Picotee
Piculet"""
 , 
"""2. What is the title of the TV arts programme presented by Melvyn Bragg since 1970?
 
The East London Show
The North Country Show
The South Bank Show (C)
The West End Show

In May 2009 ITV announced that the show is to be axed when Bragg retires in 2010"""
,
"""3. In which country is the Harz mountain range?
 
Austria
Belgium
Germany (C)
Spain""",
"""4. What type of creature is a gecko?
 
Bird
Fish
Lizard (C)
Monkey""",
"""5. During a 1987 court case, who was famously described by the judge as 'fragrant'?
 
Mary Archer (C)
Mary Parkinson
Mary Poppins
Mary Quant

Her husband Jeffrey had brought a libel action against the Daily Star""",
"""6. Which US president once claimed to have been 'misunderestimated'?
 
George W Bush (C)
Jimmy Carter
Gerald Ford
Ronald Reagan

It is one of his famous 'Bushisms'""",
"""7. Which Shropshire town is named after a famous civil engineer?
 
Bridgnorth
Ludlow
Telford (C)
Whitchurch""",
"""8. Which of these is a type of persimmon?
 
Chantelle Fruit
Brandine fruit
Sharon fruit (C)
Tracy Fruit

It is named after Israel's Sharon Valley, where it is grown""",
"""9. What colour is the pigment chlorophyll?
 
Blue
Green (C)
Red
Yellow""",
"""10. Which pre-decimal coin was nicknamed a 'tosheroon'?
 
Penny
Threepenny bit
Sixpence
Half-crown (C)"""]

def vectorReady( strinput ):
	output="""questions.push_back(Question(\""""
	
	strinput=strinput.splitlines()
	s1=strinput[0]
	output+=s1.split(' ',1)[1] #gets the question without the number at the start
	output+="""\", """
	ans=strinput[2:]
	
	for a in ans:
		if a.split(' ')[-1] == "(C)":
			a=' '.join(a.split(' ')[0:-1])
			output+="""aPair(\""""+a+"""\", 1), """
		else: 
			output+="""aPair(\""""+a+"""\", 0), """
	output+="\b\b));"
	return output

[print(vectorReady(Q)) for Q in questions]
[print(vectorReady(Q)) for Q in questions2]