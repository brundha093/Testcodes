# Python program to demonstrate 
# main() function 
  
  
from program1 import return_divisible_num

def main():
  list1 = []
  for j in return_divisible_num(100):
      list1.append(j)
  return list1
    


  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 
