
file = open("telikos.asm",'w')

def loadvr(v,r):
	ent = search_entity(v)

	# An v einai global variable
	if (ent.nestinglevel == 0):
		print(...,file=file)

	# An v einai local variable
	elif ...

	# An v einai parametros
	elif ...

def storerv(v,r):
	
	ent = search_entity(v)

	# An v einai global variable
	if ...

	# An v einai local variable
	elif ...

	# An einai parametros
	elif ...

