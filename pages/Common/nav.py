class Project():
	def __init__(self,name,letter,desc,links):
		self.name = name
		self.letter = letter
		self.desc = desc
		self.links = links

class Nav():
	def __init__(self):
		self.projects = []
		self.templetes = {}
		self.navName = None
		self.navLink = None
	def addProject(self, name,letter,desc,links):
		self.projects.append(Project(name,letter,desc,links))
	def projectList(self):
		return self.projects
	def addPage(self,templete,name,link):
		if templete not in self.templetes:
			self.templetes[templete] = []
		self.templetes[templete].append((name,link))
	def render(self, temp, currentPage, **kargs):
		dark = False
		if "dark" in kargs:
			dark = kargs["dark"]
		pages = self.templetes[temp]
		html = HTML()
		if not dark:
			html.openTag("<ul id='nav-bar' class='nav-bar'>")
		else:
			html.openTag("<ul id='nav-bar' class='nav-bar-dark'>")
		html.addTag("<li class='nav-bar-title'><a href='"+self.navLink+"'><span>"+self.navName+"</span></a></li>")
		for page in pages:
			if page[0] == currentPage:
				html.addTag("<li><a id='"+page[0]+"' href='"+page[1]+"'  class='active'>"+page[0]+"</a></li>")
			else:
				html.addTag("<li><a id='"+page[0]+"' href='"+page[1]+"'>"+page[0]+"</a></li>")
		html.closeTag("</ul>")
		return html.form()

class HTML():
	def __init__(self):
		self.indent = 0
		self.lines = []
	def form(self):
		result = ""
		for line in self.lines:
			result += ("  "*line[0]) + line[1]
			result += '\n'
		return result
	def openTag(self,line):
		self.lines.append((self.indent,line))
		self.indent+=1
	def closeTag(self,line):
		self.indent-=1
		self.lines.append((self.indent,line))
	def addTag(self,line):
		self.lines.append((self.indent,line))

globalNav = Nav()

def initalise(name,link):
	global globalNav
	globalNav.navName = name
	globalNav.navLink = link
	# Project dump (12 in total)
	desc="A puzzle game revolving around a single instruction set arcitecture machine built with a friend."
	links=[("Live","http://subleq.herokuapp.com/"),("Riyasat","http://riyasatsaber.com/"),("Github","https://github.com/rsaber/subleq")]
	globalNav.addProject("Subleq","S",desc,links)

	desc="A simple, beautiful, countdown timer whose background changes every day or so! Works via the Reddit Image script"
	links=[("Live","/timer"),("Github","TBA")]
	globalNav.addProject("Timer","T",desc,links)

	desc="A simple, text to html flashcards app to help you study!"
	links=[("Live","/flashcard"),("Github","TBA")]
	globalNav.addProject("Flashcard","F",desc,links)

	desc="A sharable stunning image from the Reddit Image script that you can overlay text on. Affectionately dubbed 'Deep Image Creator'"
	links=[("Live","/dic"),("Github","TBA")]
	globalNav.addProject("Poster Maker","P",desc,links)

	desc="A debugging/runtime environment for the BF esoteric programming language"
	links=[("Live","/bfd"),("Github","TBA")]
	globalNav.addProject("BFD","B",desc,links)

	desc="A custom designed instruction set, run in python"
	links=[("Docs","TBA"),("Github","TBA")]
	globalNav.addProject("General VM","V",desc,links)

	desc="The html, css, js and back end flask code used in this very site"
	links=[("Live","/"),("Github","TBA")]
	globalNav.addProject("This Site","W",desc,links)

	desc="Markdown notes for some of the courses i've taken at UNSW"
	links=[("Github","TBA")]
	globalNav.addProject("Notes","N",desc,links)

	desc="Markdown notes for some of the courses i've taken at UNSW"
	links=[("Github","TBA")]
	globalNav.addProject("Notes","N",desc,links)

	desc="Some cool things i've build in the C programming language"
	links=[("Github","TBA")]
	globalNav.addProject("C Code","C",desc,links)

	desc="A collection of cool code and a script or two that don't fit into their own project"
	links=[("Github","TBA")]
	globalNav.addProject("Cool Stuff","C",desc,links)

	desc="A small script to search and find a beautiful image from reddit given constraints. Used on this page, Timer and Poster Maker"
	links=[("Github","TBA")]
	globalNav.addProject("Reddit Image","R",desc,links)

def register(temp,name,link):
	global globalNav
	globalNav.addPage(temp,name,link)

def getNav(**kargs):
	global globalNav
	return globalNav