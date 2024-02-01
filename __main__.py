# Python program to demonstrate 
# main() function 
  
  
from program1 import return_divisible_num
def main():
   list1 = []
    # open a file
    file1 = open("program1_input.txt", "r")


    # read the file
    input = file1.read()
    print(read_content)

    # close the file
    file1.close()
    file2 = open("program2_input.txt","r")
    line = file2.readline()
    value= line.split("")
    string_1 = value[0]
    string_2 = value[1]    

    for j in return_divisible_num(int(input)):
        list1.append(j)
  print(list1)
    
    


  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 
