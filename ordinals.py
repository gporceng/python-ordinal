class OrdinalEngine:
	def __init__(self):
		pass
	def ordinalize(self,x):
		y=int(x)
		if(x<11):
			if(x==1):
				return(str(x)+"st")
			if(x==2):
				return(str(x)+"nd")
			if(x==3):
				return(str(x)+"rd")
			if(x>3):
				return(str(x)+"th")
		if(x>10 and x<20):			
			return(str(x)+"th")
		#Find the exponent of 10
		i=y
		i/=10
		i*=10
		l=y
		l-=i
		if(x>19):
			if(l==0):
				return(str(x)+"th")
			if(l==1):
				return(str(x)+"st")
			if(l==2):
				return(str(x)+"nd")
			if(l==3):
				return(str(x)+"rd")
			if(l>3):
				return(str(x)+"th")
