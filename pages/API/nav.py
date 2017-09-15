import json

class Page():
	def __init__(self,name,link):
		self.title = name
		self.link = link
		self.subPages = []
	def getDict(self):
		result = {}
		result["title"] = self.title
		result["link"] = self.link
		result["subPages"] = []
		for p in self.subPages:
			result["subPages"].append(p.getDict())
		return result

class Nav():
	def __init__(self, mainT, mainL):
		self.main = Page(mainT,mainL)
		self.pages = []
	def addPage(self, title, link):
		self.pages.append(Page(title,link))
	def addSubPage(self, target, title, link):
		if target == "main":
			self.main.subPages.append(Page(title,link))
			return
		for p in self.pages:
			if p.title == target:
				p.subPages.append(Page(title,link))
				return
		raise Exception("Non-existant target page: "+target)
	def getJson(self):
		result = {}
		result["main"] = self.main.getDict()
		result["pages"] = []
		for p in self.pages:
			result["pages"].append(p.getDict())
		return json.dumps(result)