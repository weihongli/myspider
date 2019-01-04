
def dealstring(text):
	for i in range(100):
		text = text.replace("\t", " ")
		text = text.replace("\r\n", "\n")
		text = text.replace("\n\n", "\n")
		text = text.replace("  ", " ")
	return text
