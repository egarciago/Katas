import sys

class collections:

	def main(self):
		self.printNumbers()

	def printLettersofWord(self, word):
		result = []

	def printNumbers(self):
		numbersFinds = self.First100NumbersPairs()
		result=''
		for num in numbersFinds:
			result += str(num) + ','
		print result

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
	collection = collections();
	collection.main()