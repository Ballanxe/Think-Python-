
l = ['perro','gato', [5,3,6,7],'leon',[54,6,35,8]]

print len(l)
print sum(l[2])

# def nested_sum(l):
# 	i = 0 
#  	for i in range(len(l)):
#  		if l[i][0] in l: 
#  			sum(l[i]) 

 
# nested_sum(l)
#     

# def capitalize_all(t):
# 	res = []
# 	for s in t:
# 		res.append(s.capitalize())
# 	return res

num = [1,2,3,6,5,4,7]

def cumulative(l):
	ros = []
	for i in range(len(l)):
		total =  l[i] + l[i+1]
		ros.append(total)
	print ros

cumulative(num)


