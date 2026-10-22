a="  I Love Python Programming  "
b=a.strip()
print(f"b lower: {b.lower()} and b upper: {b.upper()}. ")
#for i in b:
#    if i == "":
#        print("No character.")
#        break
#    l+=1
#if len(b) != 0 :
if b:
    print(f"Number of characters: {len(b)}. ")
    print(f"first character: {b[0]}, last character: {b[-1]}")
    #print(f"first character: {b.startswith('a')}, last character: {b.endswith('z')}")
else:
    print("No character.")
print("python" in a)
print(f"first: {b.split()[0][0]}, last: {b.split()[-1][-1]}")
print(b.replace("Python","python"))
print(b[::-1])
print(f"last character Position is: {b.rfind(b[-1])}")