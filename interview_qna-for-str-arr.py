# program to check a sting is palindrome or not

# def palindrome_check(s):
#     clean_s=""  
#     for char in s:
#         if char.isalnum():
#             clean_s=clean_s+char.lower()
            
#     return clean_s == clean_s[::-1]
# s="pop , 5 ,.. pop"
# print(palindrome_check(s))

# or 

# def is_palindrome(s):
#     return s == s[::-1]
# s="pop"
# ans=is_palindrome(s)
# print(ans)
    
# -------------------------------------

# program to find all unique characters from a given string

# def unique_characters(str):
#     unique_chars=set()

#     for char in str:
#         if char not in unique_chars:
#             unique_chars.add(char)
#     return unique_chars
# str="geeks"
# char_find = unique_characters(str)
# print(char_find)

# -----------------------------------------------------------

# program to return true or false for unique characters in string

# def unique_characters(s):
#     for i in range(len(s)-1):
#         for j in range(i+1,len(s)):
#             if s[i] == s[j]:
#                 return False
            
#     return True
# s="geeks for geeks"
# print(unique_characters(s))

# ------------------------------
# program for find factorial of number
# def factorial_find(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial = factorial*i
#     return factorial

# n=5
# print(factorial_find(n))

# ----------------------------------------------------------
# program to remove duplicates 

# def remove_duplicates(list):
#     seen=set()
#     result=[]
#     for i in list:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result


# list=[1,2,3,3,4,4,5,7,8,7]
# print(remove_duplicates(list))

# ----------- return true if duplicates found----
# def contains_duplicate(input: list) -> bool:
#     seen = set()
#     for i in input:
#         if i in seen:
#             return True
#         else:
#             seen.add(i)
#     return False
# list=[1,2,3,3,4,4,5,7,8,7]
# print(contains_duplicate(list))

# # -------------------------------------------------


# program for fibonacci numbers 
# def fibonacci_numbers(n):
#     a,b=0,1
#     numbers=[]
#     for _ in range(n):
#         numbers.append(a)
#         a,b = b,a+b
#     return numbers

# n=int(input("Enter a number"))

# fib_numbers=fibonacci_numbers(n)
# print(fib_numbers)

# #  if we want numbers without list then this code
# for num in fib_numbers:
#     print(num)

#  program to check two strings are anagrams

# def are_anagrams(str1,str2):
#     str1=str1.replace(" ","").lower()
#     str2=str2.replace(" ","").lower()

#     return sorted(str1)==sorted(str2)
# str1="listen"
# str2="silent"

# if are_anagrams(str1,str2):
#     print(f'{str1} and {str2} are anagrams')
# else:
#     print(f'{str1} and {str2} are not anagrams')


# without using built_in 

# def are_anagrams(str1,str2):
#     str1=str1.replace(" ","").lower()
#     str2=str2.replace(" ","").lower()

#     if len(str1)!=len(str2):
#         return False
    
#     char1_count={}
#     char2_count={}

#     for char in str1:
#         if char in char1_count:
#             char1_count[char] += 1
#         else:
    #         char1_count[char]=1
    # for char in str2:
    #     if char in char2_count:
    #         char2_count[char] += 1
    #     else:
    #         char2_count[char]=1

    # return char1_count == char2_count

# str1="listen"
# str2="silent"

# if are_anagrams(str1,str2):
#     print(f'{str1} and {str2} are anagrams')
# else:
#     print(f'{str1} and {str2} are not anagrams')

# program to check number is armstrong or not

# def is_armstrong(number):
#     num_str=str(number)
#     len_of_digits=len(num_str)
#     sum=0

#     for digit in num_str:
#         sum += int(digit)**len_of_digits
#     return number == sum
# number = 1535

# if(is_armstrong(number)):
#     print(f'{number} is a armstrong number')
# else:
#     print(f'{number} is a not armstrong number')

# TWO sum probelm
 
# Input: input = [1, 4, 6, 10], target = 10

# Output: [1, 2]

# Explanation: Because 4 + 6 == 10, we return the index of elements 4 and 6, which is [1, 2]

# def two_sum(list):
#     target=10
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]+list[j]==target:
#                 return [i,j]
#     return [-1,-1]
# list = [1,4,6,10]
# two_ele=two_sum(list)
# print(two_ele)


# program to find missing number in list 
# def missing_int(lst):
#     lst.sort()
#     for i in range(len(lst)):
#         if i!=lst[i]:
#             return i
#     return len(lst)
# lst=[0,1,3,4]
# print(missing_int(lst))
    
# product of maximum_3_numbers

# def maximum_product(input):
#     input.sort()
#     max1=input[-1]*input[-2]*input[-3]
#     max2=input[0]*input[1]*input[-1]
#     return max(max1,max2)
# input=[1,2,4,5]
# print(maximum_product(input))
  
# or

# def maximum_product(input):
#     max_product=input[0]*input[1]*input[2]
#     input.sort()
#     for i in range(len(input)-2):
#         for j in range(i+1,len(input)-1):
#             for k in range(j+1,len(input)):
#                 cur_product=input[i]*input[j]*input[k]
#                 if cur_product>max_product:
#                     max_product= cur_product
#     return max_product
# input=[1,2,4,5]
# print(maximum_product(input))

#---------- largest prime factor -----------

# def largest_prime_factor(target):
#     i=2
#     while i*i<=target:
#         if target%i!= 0:
#             i=i+1
#         else:
#             target=target//i
#     return target
# target=72
# print(largest_prime_factor(target))

# given lst find 3 numbers which will give 180 as multiplication of that 3 numbers
# 
# def find_triplets(lst):
#     target=180
#     result=[]

#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             for k in range(j+1,len(lst)):
#                 if lst[i]*lst[j]*lst[k]==180:
#                     result.append((lst[i],lst[j],lst[k]))
#     return result
# lst=[1,2,3,27,5,4,9,4]
# print(find_triplets(lst))

# program to find sum of continguos subarray in array
# def max_continguos_array(arr):
#     max_sum=0
#     for i in range(len(arr)):
#         current_sum=0
#         for j in range(i,len(arr)):
#             current_sum += arr[j]
#             if current_sum>max_sum:
#                 max_sum=current_sum
#     return max_sum
# arr=[0,-9,4,8,6,5,4]
# print(max_continguos_array(arr))
# ---------------------------------------------
# program to find  trailing zeros 

# def trailing_zeroes(n):
  
#   def factorial(n):
#     answer=1
#     for i in range(1,n+1):
#       answer=answer*i
#     return answer
    
#   n_factorial=factorial(n)
#   zero_count=0
#   while n_factorial%10==0:
#     zero_count += 1
#     n_factorial //= 10
#   return zero_count
# n=48
# print(trailing_zeroes(n))

# -----------------------------------
# function to find smallest_multiple

# import math

# def lcm(a,b):
#     return a*b//math.gcd(a,b)

# def smallest_multiple(target):
#     result=1
#     for i in range(2,target+1):
#         result=lcm(result,i)
#     return result
# target=5
# print(smallest_multiple(target))

# -----------------------------------------------------------
# def find_largest_num(arr):
#     num=0
#     for i in arr:
#         if i>num:
#             num=i
#     return num
# arr=[1,7,6,9]
# print(find_largest_num(arr))

# ---------------------------------------------------------------
# check if array is sorted

# def sorted_array(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[i]:
#                 return False
#     return True
# arr=[1,2,3,4]
# print(sorted_array(arr))

# ------------------------------------------------------
# finding second largest element in array

# def secondlargest(arr):
#     n=len(arr)
#     if n==0 or n==1:
#         return (-1,-1)
#     arr.sort()
#     large=arr[n-2]
#     print("second largest element is",large)

# arr=[1,3,4,99,6,98]
# secondlargest(arr)


# check if sum of two  number is zero or not
# def checker(list):
#     for i in list:
#         for j in list:
#             if i+j==0:
#                 return True
#     return False

# list=[1,2,3]
# list=[1,3,4,-3]
# print(checker(list))

# optimized way

# def checker(list):
#     seen=set()
#     for num in list:
#         if -num in seen:
#             return True
#         seen.add(num)
#     return False
# list=[1,3,4,-3]
# print(checker(list))

# swapping of two numbers 

# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     return a,b
# a=5
# b=8
# print(swap(a,b))

# using tuple packing

# def swap(a,b):
#     a,b=b,a
#     return a,b
# a=5
# b=8
# print(swap(a,b))

# Tuple unpacking allows you to assign the elements of a tuple or iterable to variables directly. 
# Instead of extracting values individually and assigning them one by one, you can unpack the entire tuple in one line.


# probelm to count elements in list

# def count_elements(lst):
#     counts={}
#     for item in lst:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
#     return counts

# lst=["app","dev","test" ,"prod","app","test"]
# print(count_elements(lst))


# find the items greater than itself in list

# lst=[99,28,12,85,15,45,10]
# for i in lst:
#     count=0
#     res=[]
#     for j in lst:
#         if j>i:
#             res.append(j)
#             count=count+1
    # print(i,count,res)
        

# to find student with highest marks 

# students=[('sagar',45),('srujana',32),('sai',98)]

# highest_marks=0
# top_student=''

# for name,marks in students:
#     if marks>highest_marks:
#         highest_marks=marks
#         top_student=name

# result=(top_student,highest_marks)
#                                         #     change brackets from ( ) to [] if u want ouput in list
# print(result)


# str="aaaabbbccd"
# output should be [4,3,2,1]

# input_str="aaaabbbccd"

# counts=[]
# current_count=1

# for i in range(1,len(input_str)):
#     if input_str[i]==input_str[i-1]:
#         current_count +=1
#     else:
#         counts.append(current_count)
#         current_count=1

# counts.append(current_count)

# print(counts)


# Mask email  input: Saikumaryal@gmail.com 
#             output: S*********l@gmail.com

# input = 'Saikumaryal@gmail.com'

# def mask_email(input):
#     intial = input.split('@')[0]
#     domain = input.split('@')[1]
#     return intial[0]+(len(intial)-2)*'*'+ intial[-1]+'@'+domain

# print(mask_email(input))
                       

# lst=['01-01-2022','02-09-2024','06-06-2020','12-12-2020']
# output = ['01-jan-2022','02-sep-2024','06-jun-2020','12-dec-2020']

# from datetime import datetime

# lst=['01-01-2022','02-09-2024','06-06-2020','12-12-2020']

# result=[]

# for date in lst:
#     date_obj=datetime.strptime(date, '%d-%m-%Y')
#     formatted_date=date_obj.strftime('%d-%b-%Y').lower()
#     result.append(formatted_date)

# print(result)

#  or

# def convert_date_format(date_list):
#     months = {
#         '01': 'jan', '02': 'feb', '03': 'mar', '04': 'apr', '05': 'may', '06': 'jun',
#         '07': 'jul', '08': 'aug', '09': 'sep', '10': 'oct', '11': 'nov', '12': 'dec'
#     }
#     output = []
#     for date in date_list:
#         day, month, year = date.split('-')
#         output.append(f"{day}-{months[month]}-{year}")
#     return output

# # Example usage
# date_list = ['01-01-2022', '02-09-2024', '06-06-2020', '12-12-2020']
# result = convert_date_format(date_list)
# print(result)

# interview  question 
# You are given a list of integers n . You need to split it as n/2 such a way that the sum of the integers in each pair is odd. 
# N is even. Every element of the list must be present in exactly one pair.

# def can_form_pairs_with_odd_sums(arr):
#  # Count odd and even numbers
#  odd_count = sum(1 for x in arr if x % 2 != 0)
#  even_count = len(arr) - odd_count
 
#  # Check if we can form pairs
#  if odd_count == even_count:
#    return True
#  else:
#     return False

# # Example usage
# arr = [1, 2, 3, 4, 5, 6]
# print(can_form_pairs_with_odd_sums(arr)) 

# Output: True
# Possible pairs: (1, 2), (3, 4), (5, 6)
 
#  or  this way

# def can_form_pairs(lst):
#   odd_res=[]
#   even_res=[]
#   for i in lst:
#     if i%2!=0:
#       odd_res.append(i)
#     else:
#       even_res.append(i)
#   return len(odd_res)==len(even_res)
    
# lst=[1,2,3,4,5,6]
# print(can_form_pairs(lst))

# if we want pairs in the output then

# def odd_even_numbers(lst):
#     res = []   # List to store odd numbers
#     e_res = [] # List to store even numbers
    
#     # Loop through the list and separate odd and even numbers
#     for i in lst:
#         if i % 2 != 0:
#             res.append(i)  # Append odd numbers to res
#         else:
#             e_res.append(i) # Append even numbers to e_res
    
#     # Check if the number of odd and even numbers is the same
#     if len(res) == len(e_res):
#         # Form pairs with one odd and one even number
#         pairs = [(res[i], e_res[i]) for i in range(len(res))]
#         return pairs
#     else:
#         return "Cannot form pairs with equal odd and even numbers."

# # Example usage
# lst = [1, 2, 3, 4, 5, 6]
# print(odd_even_numbers(lst))


#  Write a Python function to return the result string which should not contain digits and duplicate characters. 

# def clean_string(s):
#     result=""
#     for char in s:
#         if char.isalpha() and char not in result:
#             result = result+char

#     return result
# s="Hellosai123"
# print(clean_string(s))


#

# def merge(dict1,dict2):
#     for key,value in dict2.items():
#         dict1[key]=value
#     return dict1

# dict1={'x':2,'y':9}
# dict2={'a':4,'s':8}
# print(merge(dict1,dict2))


# Nested function

# def outer():
#     print("outer function is this")

#     def inner():
#         print("this is inner function")

#     inner()

# outer()

# inner() ---> cannot be accesed outside the function  because not declared in global scope