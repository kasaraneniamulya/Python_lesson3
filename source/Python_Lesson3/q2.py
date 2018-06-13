s = input("Enter ur string") #input sentence
s1 = s.lower()               #entire sentence is changed to lower case and stored in s1
count = 0
vowels = set("aeiou")        #defining vowels
for letter in s1:             #loop for each letter in a sentence
  if letter in vowels:         #if the letter is vowel count is increased by 1
    count += 1
print ('Number of vowels:' ,count)