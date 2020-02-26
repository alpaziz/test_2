def maxOfTwo(n1, n2):
	if(n1 > n2):
		return(n1)
	else:
		return(n2)

def main():
	a = maxOfTwo(10, 20)

	print("a is ", a)

if __name__ == '__main__':
	main()