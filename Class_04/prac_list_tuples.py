# WAP to ask the user to enter names of their 3 favorite movies & store in a list.

movies = []
for i in range(3):
  user_input = input("Enter your favorite movies name: ")
  movies.append(user_input)

print(movies)


# WAP to check if a list contain a palindrome of element.

palindrome_1 = [1,2,3,2,1]
reverse_palindrome_1 = palindrome_1.reverse()
palindrome_2 = [1,"abc","abc",1]
reverse_palindrome_2 = palindrome_2.reverse()

if palindrome_1 == [1,2,3,2,1]:
  print("Your list_1 is a palindrome")
else:
    print("Your list_1 is not a palindrome")

if palindrome_2 == [1,"abc","abc",1]:
   print("Your list_2 is a palindrome")
else:
    print("Your list_2 is not a palindrome")