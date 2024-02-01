def interleave_two_strings(string_1, string_2):
  """
  python code eto interleave two strings
  """
    value = ""
    value_1 = len(string_1)
    value_2 = len(string_2)
    if value_1 > value_2:
        for i in range(0,value_2):
            value = value + string_1[i] + string_2[i]
        num = value_1 - value_2
        for j in range (value_2,value_2+num):
            value = value + string_1[j]
    if value_2 > value_1:
        for i in range(0,value_1):
            value = value + string_1[i] + string_2[i]
        num = value_2 - value_1
        for j in range (value_1,value_1+num):
            value = value + string_2[j]    
        
    print(value)
