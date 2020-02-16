def pangram():
  string = input("Please enter a string: ")
  string = string.lower()
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  a = []
  b = []
  total = 0
  
  #creates an array containing the separate characters from the string
  for char in string:
    a.append(char)
  
  #removes the duplicates from above array  
  for char in a:
      if char not in b:
        b.append(char)
  
  #a sum of the total number of letters in an array containing
  #the single characters from the string (not including grammar and
  # spaces) is created
  for letter in b:
    if letter in alphabet:
      total += 1
  
  #if the running total is equal to 26, then the string contained every
  #letter from the alphabet atleast once
  #hence, the string is a pangram
  if total==26:
    print("The string is a pangram.")
  else:
    print("The string is not a pangram.")
