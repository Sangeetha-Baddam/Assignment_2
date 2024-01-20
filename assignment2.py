#1
first_name=input("enter your first name:")
last_name=input("enter your last name:")
full_name=(first_name+' '+last_name)
print(full_name)

def string_alternative(str):
    result=""#taking a new string
    for i in range (len(str)):
        if(i%2==0):
           result+=str[i] 
    return result
print(string_alternative("Sweety"))

#2
input_file = open('input.txt', 'r')#reading the input file
count = dict()# to count 
source = input_file.read()# read data from the input file
words = source.split()# splitting the words
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
f = open('output.txt', 'w')#writing the output file
f.write(source)
f.write('\nword_count:\n')
for key, value in count.items():
    f.write(f"{key}: {value}\n")
f.close()

#3
ist_inches=list(map(float,input('enter list').split()))#input list in inches
list_cm=[]#new list in cm
for i in list_inches:
    i*=2.54#convertion
    list_cm.append(i)
print(list_cm)  #printion
