#A function to see if the given number is a phone number.

def isPhoneNumber(text):
#First, we see if our string is the proper length of a phone number (with hyphens)
  if len(text) != 12:
    return False
#Then, we check if the first group actually has numbers.
  for i in range(0,3):
    if not text[i].isdecimal():
      return False
#Does this index contain a hyphen?    
  if text[3] != "-":
    return False
#Does the next group contain numbers?
  for i in range (4,7):
    if not text[i].isdecimal():
      return False
#Is there another sexy hyphen?
  if text[7] != "-":
    return False
#Does the final group have numbers?
  for i in range(8,12):
    if not text[i].isdecimal():
      return False
  return True

#Now we finally print
print ("956-555-2021")

print (isPhoneNumber("956-555-2021"))
