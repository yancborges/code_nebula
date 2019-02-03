def hey(text, target, option, nrow):
	with open(target ,option, encoding='utf8') as f:
		f.write(str(text))
		if(nrow == True):
			f.write('\n')
	print('written to '+ target + ' file')