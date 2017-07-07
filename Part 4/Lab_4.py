#1a)
def order_dict(my_dict):
	#get all of the keys so you can navigate the dict.
	keys = my_dict.keys()
	sorted_keys = sorted(keys)
	sorted_dict = {}

	#make a new dict that is sorted, based on the sorted key list
	for key in sorted_keys:
		sorted_dict[key] = my_dict[key]
	
	return sorted_dict

#1b)
#detect size of dictionary
def multiple_keys(my_dict):
	return len(my_dict.keys)>1
	
#1c) the directions for this aren’t clear)
def replace_with_sum(my_dict):
	for k in my_dict.keys():
        #assuming values are a list of nums, acculated them at each key
		my_dict[k] = sum(my_dict[k])
	return my_dict

#1d)
def largest_smallest(my_set):
	temp = my_set
	smallest = my_set.pop()
	largest = smallest
    #navigate the set and find the smallest/largest elements
	for i in temp:
		if i < smallest:
			smallest = i
		if i > largest:
			largest = i
	return (smallest, largest)
	
#1e)
def sym_diff(a,b):
    #symmetric diff for sets
	return a ^ b
	

