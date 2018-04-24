
class collections:

	def main(self):
		self.printNumbers()

	def printLettersofWord(self, word):
		result = []

	def printNumbers(self):
		for num in self.First100NumbersPairs:
			print num

	def First100NumbersPairs(self):
		numbers = []
		num = 2
		count = 0
		while(count < 100):
			numbers.append(num)
			num +=2
			count +=1
		return numbers

if __name__ == '__main__':
	self.main()