
val = raw_input("Enter your String: ")
w = ""
for i in val:
    w = i + w
 
if (val == w):
    print("Yes! it is palindrome")
else:
    print("No, this is not a palindrome")
