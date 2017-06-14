class Source:
	def __init__(self, text):
		self.pos = 0
		self.text = text
	def accept(self):
		if(self.pos >= len(self.text)):
			return -1
		self.pos+=1
		return self.text[self.pos-1]
	def peek(self, offset):
		if(self.pos+offset >= len(self.text)):
			return -1
		return self.text[self.pos+offset]

class Grammar:
	def __init__(self, terminals, transformations, root):
		self.terminals = terminals
		self.terminals["E"] = -1
		self.terminals["ASCII"] = -1
		self.terminals["EOF"] = -1
		self.root = root
		self.transformations = {}
		self.selectSets = {}
		self.initTransformations(transformations)
	def initTransformations(self,transList):
		for trans in transList:
			left = trans.split(" -> ")[0]
			self.transformations[left] = trans.split(" -> ")[1].split(" | ")
		for trans in self.transformations.keys():
			self.getSelectSet(trans)

	def getSelectSet(self,left):
		# set up
		right = self.transformations[left]
		if(left not in self.selectSets):
			self.selectSets[left] = set()
		#for each option
		for op in right:
			concatList = op.split(" ")
			for concat in concatList:
				# see if the leftmost has a select set we can take
				if(concat in self.selectSets):
					self.selectSets[left] |= self.selectSets[concat]
					continue
				# see if it's a terminal
				if(concat in self.terminals):
					self.selectSets[left].add(concat)
					break
				# get it's select set
				self.getSelectSet(concat)
				self.selectSets[left] |= self.selectSets[concat]
				# see if it could evaluate to E in which case keep looking
				if("E" not in self.selectSets[left]):
					break
		return

	def parse(self, src):
		n = src.peek(0)
		result = []
		for terminal in self.terminals.keys():
			if()


# NOTE E is epsilon, ASCII is ASCII and EOF is EOF
# these are provided by the system
transformations = []
transformations.append("Program -> Card Program | EOF")
transformations.append("Card -> Question QAS Answer CS | Question QAS Answer EOF")
transformations.append("Question -> Text Question | Table Question | NL Question | E")
transformations.append("Text -> ASCII")
transformations.append("Table -> TR TS Text TR TE")
transformations.append("Answer -> Text Answer | Table Answer | NL Answer | E")
terminals = {}
terminals['QAS'] = "---"
terminals['NL'] = '\n'
terminals['CS'] = "***"
terminals['TR'] = '!'
terminals['TS'] = "t"
terminals['TE'] = "e"

FcGrammar = Grammar(terminals, transformations, "Program")
test = '''hello world!
---
so how you doing?
***
hey?
---
r u ready for the sex baby
'''
FcGrammar.parse(Source(test))






