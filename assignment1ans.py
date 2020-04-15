print("good morning")

my_str = "Thakur College"
for i in my_str:
  print(i)
  
  
my_str = "Thakur College"
for i in my_str:
  print(i)
  
my_str = "Thakur College"
for i in my_str:
  print(i)
  
  
original_str = "The quick brown rhino jumped over the extremely lazy fox."
count=0
for i in original_str:
  count+=1

print(count)



addition_str = "2+5+10+20"
lst=[]
for i in addition_str:
  if i=="+":
    pass
  else:
    lst.append(i)
for i in range(len(lst)):
  lst[i]=int(lst[i])

print(sum(lst))



week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

x=week_temps_f.split(",")
print(x)
for i in range(len(x)):
  x[i]=float(x[i])

print(sum(x)/len(x))



lst=[]
for i in range(0,66):
  lst.append(i)

print(lst)


original_str = "The quick brown rhino jumped over the extremely lazy fox"
x=original_str.split(" ")
print(x)
  
for i in x:
  print(len(i))
  
  
  
lett=""

if lett=="":
  lett="bbbbbb"

print(lett)



