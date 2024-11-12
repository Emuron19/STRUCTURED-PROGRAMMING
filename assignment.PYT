#NUMBER1
def even_numbers(integers):
    return [j for j in integers if j %2==0]

list = [1,2,3,4,5,6,7,8,9,10]
even_num = even_numbers (list)
print (even_num)

#NUMBER2
def print_multiplication_table (number ):
    for i in range (1,13):
        print ("f*{number} x {i}={number * i}")
        number=5
        print_multiplication_table(number) 
    
 #NUMBER 3
def biggest_sum(sum):
     if not sum:
         return None
     large =sum [0] 
     for i in  sum:
         if i > large:
             large = i
     return large 
sum =[10,4,2,15,7]
large =biggest_sum(sum)
print (large)

#NUMBER 4
input_string ="hello world"
comparison_string = "hello world" 
if input_string ==comparison_string :
    print ("its the same string")
else:
    print("its not the same string")    
    
         
                