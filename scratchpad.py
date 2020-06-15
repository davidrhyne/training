
# take content of data.txt and copy and "insert" two more times
with open("files/data.txt", "a+") as myfile:
    myfile.seek(0)
    contents = myfile.read() + "\n"
    myfile.seek(0)
    myfile.write(contents)
    myfile.write(contents)

print(contents)

# # read the bear1.txt and append contents to end of bear2.txt
# with open("bear1.txt", "r") as myfile:
#     file_contents = myfile.read()

# with open("bear2.txt", "a") as myfile:
#     myfile.write(file_contents)


read the bear.txt and write first 90 characters to first.txt

with open("files/bear.txt","r") as myfile:
   file_contents = myfile.read()

first_ninety = file_contents[:90]

with open("files/first.txt","w") as myfile:


function that takes single character and filepath and returns the number of occurences that character has in the file
def count_letter_in_file(character,path):
   user_file = open(path)
   file_contents = user_file.read()
   user_file.close()
   return file_contents.count(character)

print(count_letter_in_file('o',"fruits.txt"))


# open file and print first 90 characters
#myfile = open("bear.txt")
#file_contents = myfile.read()
# myfile.close()
# print(file_contents[:91])

# function with kwargs... keyword arguments
# def find_sum(**kwargs):
#    return sum(kwargs.values())
#
# print(find_sum(a=4,two=2,three=3))

# function with #args... take in stings, capitalize the string, and return the list in alphabetically order
# def capitalize_and_sort(*args):
#    sorted_tup = sorted(args)
#    mylist = [value.upper() for value in sorted_tup]
#    return mylist
#
# print(capitalize_and_sort('efg','xyz','abc'))

# function with *args... take in numbers and return the average
# def calc_average(*args):
#    return sum(args) / len(args)
#
# print(calc_average(10,20,30,40))


# function with multiple parameters - take 2 strings and return a concatenated string
# def combine(first,second):
#    return ('%s%s' % (first,second))
#
# print(combine('string1','string2'))
# print(combine(second='string1',first='string2'))

# list comprehension with cast
# def convert_and_sum(input_list):
#    #create a list of floats from the list of string#s
#    result = [float(value) for value in input_list]
#    #and then sum up the values in the list with builtin sum method
#    return sum(result)
#
#data = ['1.2','2.6','3.3']
# print(convert_and_sum(data))

# list comprehension with if else statement
# def zeros_instead(input_list):
#    result = [value if isinstance(value,int) else 0 for value in input_list]
#    return result
#
#data = [99,'no data',95,94,'no data']
# print(zeros_instead(data))

# list comprehension with if statement
# def only_positives(input_list):
#    result = [value for value in input_list if value > 0]
#    return result
#
#data = [-5,3,-1,101]
# print(only_positives(data))


# list comprehension
# def only_numbers(input_list):
#    result = [value for value in input_list if isinstance(value,int)]
#    return result
#
#data = [99,'no data',95,94,'no data']
# print(only_numbers(data))

# def greeting(value):
#    the_greeting = "Hi %s" % value
#    return (the_greeting.title())
#
# greeting("Marry")

# def temp_check(value):
#    if isinstance(value,int):
#        if value > 25:
#            return "Hot"
#        elif value >= 15 and value <= 25:
#            return "Warm"
#        else:
#            return "Cold"
#    else:
#        return False
#
#
#print("26 = ",temp_check(26))
#print("25 = ",temp_check(25))
#print("15 = ",temp_check(15))
#print("14 = ",temp_check(14))
#print("string = ",temp_check("number"))
