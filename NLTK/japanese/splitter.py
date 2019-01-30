import japanese_splitter

def hey(text, target):
	if(target == None):
		target = 'output.txt'
	with open(target ,'w', encoding='utf8') as f:
		f.write(str(text))
	print('written to output.txt file')

hey(japanese_splitter.jTokenize("私は子供です。だから、お菓子を食べてが好き！"))
#hey("。、！？」「", 'punct.txt')




