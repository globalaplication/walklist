import os
def walklist(path, liste=list(), 
options="list"):	
	for f in path:
		if os.path.isdir(f) is False:
			liste.append(f)
		else:
			for path, folder, file in os.walk(f): 
				liste.append(path)
				for beta in file:
					liste.append(os.path.join(path,
						beta))
	if (options == "remove"):
		liste.reverse()
		for rm in liste:
			if os.path.isdir(rm) is True:
				os.removedirs(rm)
			else:
				os.remove(rm)
	return liste
#path = "/home/elementary/Here/icons"
#walklist(path, 
options="list")
#print walklist(path, 
options="remove")
