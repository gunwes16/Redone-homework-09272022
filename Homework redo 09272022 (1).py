#!/usr/bin/env python
# coding: utf-8

# 1. Print out your favorite color and write comment about what you are doing above the code.

# In[2]:


#printing favorite color
print(green)


# 2. Print the sumation of numbers 1 through 10

# In[10]:


print(1+2+3+4+5+6+7+8+9+10)


# 3. Print what 2 to the 8th power is.

# In[5]:


print(2**8)


# 4. Print the remainder of 100 divided by 11. 

# In[11]:


print(100%11)


# 5. What is the result of adding strings: 20, 8, 77?

# In[13]:


print("20"+"8"+"77")


# 6. Print out 100 divided by 5

# In[7]:


print(100/5)


# 7. What is the difference (subtraction) between 10/4 and 10//4?  Print out the result

# In[16]:


print((10/4) - (10//4))


# 8. Create a variable called height and store your height value there.
# Print a sentence describing your height and use the variable in the sentence as well.

# In[18]:


height= "6 3"
print("My height is", height)


# 9. Print the same information as exercise 8 using a formatted string. 

# In[20]:


print(f"my height is {height}")


# 10. Use two different (single and double) quotes in a string to print out a sentence

# In[23]:


print("I am pointing out the 'difference'")


# 11. Print out Hello World! 7 times each on a new line using only one line of code.

# In[25]:


print('Hello World!\n' * 7)


# 12. Write a code to get two integers from a user. Then print out their summation, subtraction, multiplication, and division.

# # num1 = int(input("give me a number: "))
# num2 = int(input("give me a number: "))

# In[2]:


print(num1 + num2)
print(num1 - num2)
print(num1 * num2)


# 13. You and your collegue have been tasked to write a code to get 5 numbers from a user and then print out their summation and average in a formatted string.  Your partner wrote codes below.  Now it is up to you to fix all errors.

# In[3]:


prompt = f"Enter a number: "

numb1 = int(input("Enter a number: "))
numb2 = int(input("Enter a number: "))
numb3 = int(input("Enter a number: "))
numb4 = int(input("Enter a number: "))
numb5 = int(input("Enter a number: "))

total = (numb1 + numb2 + numb3 + numb4 + numb5)
avg = total // 5

print("{numb1} + {numb2} + {numb3} + {numb4} + {numb5} = {total}")
print("average is {total}")


# In[ ]:





# 14. You and your partner have been assigned to a project to write a program to calculate the amount of runoff rain on a roof from any given rainfall.  
# 
# You and your partner have figured out that to calculate the runoff from any given rainfall. 
# 
# You need to take the dimensions of the footprint of the roof and <b>convert them to inches</b> (ex - a 50' x 20' roof is 600" x 240"). The dimensions should be user submitted. 
# 
# Then, multiply the roof dimensions by the number of inches of rainfall. As an example, 600" x 240" x 1" = 144,000 cubic inches of water for an inch of rainfall. Finally, divide that result by 231 to get the number of gallons (because 1 gallon = 231 cubic inches; 144,000/231 = 623.38).
# 
# Your partner started coding before getting sick and it is up to you to finish the program.

# In[ ]:


print("\nRainfall Calculation ***\n")

width = int(input("What's roof's width in foot? ")) * 12
length = int(input("What's roof's length in foot? ")) * 12
rain = int(input("How much did it rain? "))
cubic_length = width X length X rain

gallon = cubic_inch/231

print(gallon)



# In[ ]:





# 15. A program is required to get a customer’s name, a purchase amount and a discount rate (in %). The program must compute the discount amount, sales tax (6%) and the total amount due. Using one print statement, print the customer’s name, purchase amount, discount amount, sales tax and total amount due in friendly format.

# In[ ]:





# In[2]:


name = input("customer name")
Amount = float(input('price of purchase:'))
discount = float(input("discount percentage:")) / 100

Taxe_rate = .06

Discount_amount = amount * discount
Subtotal = amount - discount_amount
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax


# In[1]:


print("*" * 30)
print(f"{name}\n{amount}\n{discount_amount}\n{sales_tax}\n{total}")
**************************


# In[ ]:





# In[ ]:




