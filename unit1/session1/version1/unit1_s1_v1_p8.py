def print_todo_list(task):
	print("Pooh's To Dos:")
	for i, work in enumerate(task):
		print(str(i+1)+ ".", work)
	print("")


task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)