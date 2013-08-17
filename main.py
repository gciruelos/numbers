'''
This is a very simple script that converts numbers to words. It relies on
a recursive method, which I think is the most suitable to do this.

Please feel free to contribute, adding a language or fixing bugs, creating
a pull request.

Author: Gonzalo Ciruelos <comp.gonzalo@gmail.com>
License: MIT
'''



def decompose(number, significant_figures):
	figures = []
	
	num_string = str(number)
	
	for i in num_string:
		if i=='.':
			index = num_string.index(i)+1
			figures.append(int(''.join(num_string[index:index+significant_figures])))
			break
		else:
			figures.append(int(i))
	
	return figures
	

class Number():
	def __init__(self, num, significant_figures = 2):
		self.sign = num/abs(num)
		self.num = num * self.sign
		self.significant_figures = significant_figures
		self.decomposed = decompose(self.num, significant_figures)
		self.length = len(self.decomposed)
		
		
		if '.' not in str(self.num):
			self.significant_figures = 0
		else:
			self.significant_figures = len(str(self.decomposed[-1]))
	
	def __str__(self):
		return str(self.num)+'\t'+str(self.decomposed)
	
	def wordSpanish(self):
		import spanish as spa
		
		words = []
		
		flags = {'u': 0,
				 'k': 0,
				 'M': 0,
				 'B': 0,
				 'T': 0}
		
		if self.num == 0:
			return 'cero'
		
		numeral = self.decomposed
		
		if self.significant_figures == 0:
			end = self.length
		else:
			end = self.length-1
			
		iterable = range(0, end)
		
		for index in iterable:
			
			order = end - index
			
			if numeral[index]==0:
				continue


			if order == 1:
				if flags['u']: continue
				words.append(spa.order1[numeral[index]])
			elif order == 2:
				if numeral[index]*10+numeral[index+1]<=20:
					words.append(spa.order20[numeral[index]*10+numeral[index+1]])
					flags['u'] = 1
				elif numeral[index]*10+numeral[index+1]<30:
					words.append('veinti'+Number(numeral[index+1]).wordSpanish())
					flags['u'] = 1
				else:
					words.append(spa.order2[numeral[index]])
					if numeral[index+1]:
						words.append('y')
			elif order == 3:
				if numeral[index]==1 and numeral[index+1]==0 and numeral[index+2]==0:
					words.append('cien')
				else:
					words.append(spa.order3[numeral[index]])
			
			elif order >= 4 and order <= 6:
				if flags['k']:
					continue
					
				'''
				if order == 4:
					num = numeral[index]
					if num == 1: num = 0
				elif order == 5:
					num = int(''.join(map(str, numeral[index:index+2])))
				else: #elif order == 6:
					num = int(''.join(map(str, numeral[index:index+3])))
					
				Self explainatory. The same hereby.
				'''
				
				num = int(''.join(map(str, numeral[index:index+(order-3)])))
				
				if num == 1:
					words.append('mil')
					continue
					
				words.append(Number(num, 0).wordSpanish())
				words.append('mil')
				flags['k'] = 1
			
			elif order >= 7 and order <= 12:
				if flags['M']: continue

				num = int(''.join(map(str, numeral[index:index+(order-6)])))
				
				if num == 1:
					words.append('un millon')
					continue
				
				words.append(Number(num, 0).wordSpanish())
				words.append('millones')
				flags['M'] = 1
			
			elif order >= 13 and order <= 24:
				if flags['B']: continue

				num = int(''.join(map(str, numeral[index:index+(order-12)])))
				
				if num == 1:
					words.append('un billon')
					continue
				
				words.append(Number(num, 0).wordSpanish())
				words.append('billones')
				flags['B'] = 1
			
			elif order >= 24 and order <= 47:
				if flags['T']: continue

				num = int(''.join(map(str, numeral[index:index+(order-23)])))
				
				if num == 1:
					words.append('un trillon')
					continue
				
				words.append(Number(num, 0).wordSpanish())
				words.append('trillones')
				flags['T'] = 1



			else:
				return 'infinito'
				#words.append('error')
				
				
				
				
		if self.significant_figures:
			words.append('coma')
		
			if self.significant_figures == 1:
				words.append(spa.order1[self.decomposed[-1]])
			
			elif self.significant_figures == 2:
				words.append(Number(self.decomposed[-1], 0).wordSpanish())
			
			else:
				for i in str(self.decomposed[-1]):
					words.append(spa.order1[int(i)])

		#print words
		if self.sign == 1:
			return ' '.join(words)
		else:
			return 'menos '+' '.join(words)
		
		
	def wordEnglish(self):
		pass
		



while 1:
	pi = input('> ')

	a = Number(pi, 4)
	print a.wordSpanish()
