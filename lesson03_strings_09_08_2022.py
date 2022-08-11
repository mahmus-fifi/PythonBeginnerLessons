#lesson 03
#working with strings and string methods 
#09/08/2022

message = "hello Nancy"
print(message)

#replacing text
new_nancy = message.replace("Nancy","cool friend")
print(new_nancy)

#change text to upper case
upper_case = new_nancy.upper()
print(upper_case)

#count text
count = upper_case.count("cool")
print(count)
#findout 



#find text
text = "the world is sad"
find_text = text.find("is")
print(find_text)


#slicing
greeting = "how are you today"
print(greeting[0:10])
print(greeting[3:7])
print(greeting[-5:])
help(str)
#help(int)

print("Hello World")
name = "fish fish fish "

new_upper_name = name.upper()

print(name.count("fish"))
print(new_upper_name.isupper())

isAtTheOffice = True

if(isAtTheOffice):
    print("he is at the office")









