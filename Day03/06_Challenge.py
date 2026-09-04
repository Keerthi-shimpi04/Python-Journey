#Student marks analysis
'''
marks = [78, 92, 65, 88, 55, 92]


Find:

Total marks
Average
Highest
Lowest
Number of students who scored above 80
Remove duplicate marks
Sort marks descending
'''

marks = [78, 92, 65, 88, 55, 92]


print(sum(marks))

sum=0

for i in marks:
 sum=sum+i

average=(sum/len(marks))
print(average)


Highest=marks[0]

for i in marks:
 if(i>Highest):
  Highest=i

print(Highest)

lowest=marks[0]

for i in marks:
 if(i<Highest):
  Lowest=i

print(Lowest)


count=0

for i in marks:
 if(i>80):
  count+=1

print("Number of student scored above 80 are:",count)


unique_marks=set(marks)
print(unique_marks)

marks.sort(reverse=True)
print(marks)



'''

# Highest
highest = max(marks)

# Lowest
lowest = min(marks)

# Number of students scoring above 80
above_80 = 0

for mark in marks:
    if mark > 80:
        above_80 += 1

# Remove duplicates
unique_marks = set(marks)

# Sort descending
descending_marks = sorted(marks, reverse=True)

# Display results

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Students scoring above 80:", above_80)
print("Unique Marks:", unique_marks)
print("Marks in descending order:", descending_marks)
'''


# challenge 2
cart = []

while True:

    print("\n1. Add product")
    print("2. Delete product")
    print("3. View cart")
    print("4. Count items")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            product = input("Enter the item you want to add: ")
            cart.append(product)
            print("Product added!")

        case 2:
            product = input("Enter the item you want to remove: ")

            if product in cart:
                cart.remove(product)
                print("Product removed!")
            else:
                print("Product not found!")

        case 3:
            print("Your cart:", cart)

        case 4:
            print("Number of items:", len(cart))

        case 5:
            print("EXIT")
            break

        case _:
            print("Invalid choice!")

# Challenge 3

contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Count Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")

            contacts[name] = phone

            print("Contact added successfully!")

        case 2:
            name = input("Enter name to search: ")

            if name in contacts:
                print("Phone number:", contacts[name])
            else:
                print("Contact not found!")

        case 3:
            if len(contacts) == 0:
                print("Contact book is empty!")
            else:
                print("\nAll Contacts:")

                for name, phone in contacts.items():
                    print("Name:", name, "| Phone:", phone)

        case 4:
            name = input("Enter name to delete: ")

            if name in contacts:
                del contacts[name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")

        case 5:
            print("Total contacts:", len(contacts))

        case 6:
            print("Thank you for using Contact Book!")
            break

        case _:
            print("Invalid choice!")
            