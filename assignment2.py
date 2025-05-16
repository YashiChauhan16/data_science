#CONDITIONAL STATEMENTS!!

#QUESTION-1
# numb=float(input("ENTER A NUMBER:"))
# if numb>=0:
#     print("NUMBER IS POSITIVE.")

#QUESTION-2
# numb2=float(input("ENTER FIRST:"))
# if numb2>=0:
#     print("NUMBER IS POSITIVE.", numb2)
# else:
#     print("NUMBER IS NEGATIVE.",numb2)

#QUESTION-3
# numb_3=float(input("ENTER A VALUE:"))
# if numb_3>=0:
#     print("NUMBER IS POSITIVE.",numb_3)
# elif numb_3 <= 0:
#     print("NUMBER IS NEGATIVE.",numb_3)
# else:
#     print("NUMBER IS ZERO.",numb_3)

#QUESTION-4
# numb_4 = float(input("ENTER NUMBER:"))
# if numb_4 >= 0:
#     if numb_4 % 2 == 0:
#         print("NUMBER IS PORITIVE AND EVEN.")
#     else:
#         print("NUMBER IS POSITIVE AND ODD.")
# else:
#     print("NUMBER IS NEGATIVE.")


#LOOPS
#Question-5
# for q in range(1,11):
#     print(q)

#Question-6
# a= 1
# while a<=10:
#     print(a)
#     a+=1

#Question-7
# for aste in range(5):  
#     for risk in range(5):  
#         print("*", end=" ")  
#     print()  

#Question-8
# sum=0
# while True:
#     a=int(input("ENTER NUMBER(stop=0):"))
#     if a == 0:
#         break
#     sum += a
#     print(f"Total is {sum}")

#Question-9
# for i in range(1,11):
    # if i == 5:
    #     continue
    # print(i)

#Question-10
# def empty_funt():
#     pass

# print(empty_funt()) #returns none

#Question-11
# z= int(input("ENTER A NUMBER:"))
# for a in range(1,z+1):
#     if z%2==0:
#         print(a)
'''print
(z) it prints z(the enteres number)
after ever number.'''

#Question-12

#Question-13
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Not for negative numbers.")
# else:
#     factorial = 1
#     i = 1
#     while i <= num:
#         factorial *= i
#         i += 1
#     print(f"The factorial of {num} is {factorial}")

#Question-15
# num = int(input("ENTER A NUMBER:"))
# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")



  