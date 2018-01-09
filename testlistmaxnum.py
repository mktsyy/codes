#- * -coding: utf - 8 - * -

#testlistmaxnum

# def main():
# 	numlist =[9,10,20,5,40,80,70,100,4]

# 	print max(numlist)

k = [(2,3),(3,4),(4,5),(8,9)]
# a = [(2,3),(3,4),(4,5)]
a = [(2,3),(8,9)]
def main():

	res = list(set(k).intersection(set(a)))
	print res
	# print x



if __name__ == '__main__':
	main()