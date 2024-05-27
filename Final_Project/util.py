#this is a tuple of questions, wont be modified by user and will be printed each time
#its iterated over in the function resolveTest from the file util.py 
#from line code 10 to 14
questions = ("Cuanto es 1 + 1? ",
             "Cuantos es 10 + 10? ",
             "Cuantos es 5 + 5? ",
             "Cuantos es 10 / 2? ",
             "Cuantos es 2 * 4? ",
             )
#this tuple will be printed to the user in the terminal right after each qeustion printed
#so he/she knows which could be the answer
options = (("A. 2 ", "B. 3 ", "C. 5 ", "D. 7 "),
           ("A. 2 ", "B. 20 ", "C. 5 ", "D. 7 "),
           ("A. 4 ", "B. 6 ", "C. 8 ", "D. 10 "),
           ("A. 6 ", "B. 8 ", "C. 10 ", "D. 5 "),
           ("A. 10 ", "B. 11 ", "C. 8 ", "D. 13 "))
#this is a list with the answers, this list will check if the answer is correct 
#by comparing the users input in the variable guesses
answers = ("A","B","D","D","C")