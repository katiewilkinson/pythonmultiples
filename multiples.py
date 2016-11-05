#create a function called multiply (def multiply) that reads every value in the array(arr)
#every value is multipled by 5

 a = [2,4,10,16]
 def multiply(arr):
   for a in range (len(arr)):
       arr[i] = arr[i] * 5
       return arr
b = multiply(a, 5)
print b
