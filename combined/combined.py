file1 = open("numbers1.txt", "w+")      #creating numbers1 file with variable file1
numbers1 = [20,5,18,6,442,7,18]         #making numbers1 a list
numbers1.sort()                         #sorting in smallest to largest
file1.write(str(numbers1))              #writting on the new file

file1.close()#closing file

file2 = open("numbers2.txt", "w+")      #creating numbers2 file with variable file2
numbers2 = [1,65,9,745,0,4,30,8]        #making numbers2 a list
numbers2.sort()                         #sorting
file2.write(str(numbers2))              #writting on a new file

file2.close()#closing file

file3 = open("all_numbers.txt", "w+")   #creating new file
numbers1.extend(numbers2)               #adding numbers 2 to numbers 1
numbers1.sort()                         #sorting

file3.write(str(numbers1))             #writing all numbers on the new all_numbers file

file3.close()#closing file