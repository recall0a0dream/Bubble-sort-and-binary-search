import random
list1=[57,97,72,13,66,36,35,26,21,13]# Optionally set a list of numbers.
tuple1=tuple(list1)
n=len(list1)

# Use the bubbling method to sort the above list from smallest to largest.
for i in range(n-1):
    for j in range(n-i-1):
        if list1[j]>list1[j+1]:
            a=list1[j+1]
            list1[j+1]=list1[j]
            list1[j]=a
print(list1)

# Use the dichotomy to find a predetermined number's index in the sorted list.
a=random.choice(list1) # Choose a number from the list randomly.
m=0
while len(list1)>=1:
    n=len(list1)
    if a==list1[int((n-1)/2)]:
        print("The rank of ",a," is ",m+int((n-1)/2))
        break
    elif a<list1[int((n-1)/2)]:
        list1=list1[:int((n-1)/2)]
    else:
        list1=list1[int((n-1)/2)+1:]
        m=m+int((n-1)/2)+1
# The number m can help us to find the correct index of a in the initial ordered list1.
if n==1:   # At this time, the selected a is the unique one.
    n=n
elif n==2: # At this time, the selected a is definitely the first one.
    if list1[1] == a:
        print("The rank of ", a, " is ", m + int((n - 1) / 2) + 1)
else:  # That means n>=3, then the selected number definitely not at the end.
# By the way, the location of the above "else" will be wrong if you merely press the "Enter" at the end of the last line. It's due to the rule of retract of Python.
    for i in range(int((n - 1) / 2) - 1, -1, -1):
        if list1[i] == a:
            print("The rank of ", a, " is ", m + int((n - 1) / 2) - (int((n - 1) / 2) - i))
    for j in range(int((n - 1) / 2) + 1,n):
        if list1[j] == a:
            print("The rank of ", a, " is ", m + int((n - 1) / 2) + (j - int((n - 1) / 2)))









