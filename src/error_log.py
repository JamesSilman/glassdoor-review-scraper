
class Logging:

	def __init__(self):
		pass

	if __name__ == '__main__':
		pass

	def log(self, error):
		fh = open("errors.txt", "a") 
		fh.write(error + "\n") 
		fh.close 

