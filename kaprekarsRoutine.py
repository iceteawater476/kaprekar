def in1():
  x = input("Enter a 4 digit number following Kaperkar's constant theorem rule: ") # takes value
  val = x #stores value
  va1 = x #stores value for the first input
  return val , va1


val , va1 = in1()

if len(val) != 4:
  print("Please enter a 4 digit number") #checks if the digit is 4 digit or not
  in1()
elif len(set(val)) == 1: #converts the str value to a set, convert the string into a set(). Since a set only keeps unique elements, any 4-digit number with identical digits (like "1111" or "7777") will compress down to a set with a length of 1
    print("Invalid: Number must have at least two distinct digits.")
    in1()

count = 1 #first iteration number

num1 = 0 #placeholder so it doesn't throw an error
while num1 != 1:
  val = str(val).zfill(4) #uses zfill function (pads the input with 0 as leading 0's to conform with Kaprekar's constant algorithm) ; The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
  num = [int(x) for x in val] #converts string to list of integers
  num.sort() #sorts integers in a decending order
  num_neg= sorted(num, reverse=True) #sorts number in ascending order
  val1 = int("".join(map(str, num_neg))) #makes the list to an integer
  val2 = int("".join(map(str, num))) #makes the list io an integer
  num1 = val1 - val2 #finds the difference of two values


  if num1 != 6174:
    print(num1, f"lowest {val2}, highest {val1}, iteration{count}") #prints the lowest and highest value for a given number
    val = str(num1) #converts the int to str for to run in the loop again
    count += 1 #adds 1 to the iteration count

  elif num1 == 6174:
      print(num1, f"lowest {val2}, highest {val1}, iteration{count}")
      print(f"6174 i.e. Kaperkar's Constant found \n it took {count} number of tries for the input {va1}") #if kaperkar's constant is found it outputs how many iteration it took to find the value
      break







