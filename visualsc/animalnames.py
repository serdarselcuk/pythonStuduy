#Use while to get the user input, animal_name, of 4 animals
#use a counter, num_animals, in the while loop condition
#append the names to a string variable, all_animals
#User can exit early by typing "exit" (check if animal_name is "exit" and break)
#when the loop finishes, print the names of all_animals
#-bonus: print "no animals" if animal_name is empty after exiting the loop

#Tip: Think about Sequence and variables that need to be initialized before the while loop

# [ ] Create the Animal Names program, run tests
animalnames=[]
while True:

    animalname=(input())
   
    animalnames.append(animalname)
    print(animalnames)
    print(len.animalnames)