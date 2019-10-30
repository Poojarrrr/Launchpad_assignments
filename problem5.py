def reverse_ans(x):
	pooj = x.split()
	pooj.reverse()
	return " ".join(pooj)
question = input(" Enter statement:  ")
print(reverse_ans(question))