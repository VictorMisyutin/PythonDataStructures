string = "this is a phrase"
result1 = [line.strip().split() for line in
string.split('\n')]
string = "this is another phrase"
result2 = [line.strip().split() for line in
string.split('\n')]
result = [result1,result2]
print (result)