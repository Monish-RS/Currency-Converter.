# Currency-Converter.
A currency converter in Python is a program that allows users to convert amounts from one currency to another based on the current exchange rates.
# Introduction
The purpose of this project is to create a Python program that enables users to seamlessly convert amounts from one currency to another, providing a handy tool for international travelers, businesses, and anyone dealing with multi-currency transactions.
# Fundamental Concepts used in this program
## IT INCLUDES:
Dictionary data type,
Functions and variables,
Input and output,
String operations,
Exception handling,
Conditional statements.
# Dictionary data type:
A dictionary in Python is a collection of key-value pairs, where each key is unique, and each key is associated with a value. It's denoted by curly braces {} and can be used to store and retrieve data efficiently. 
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/8deaa460-777d-40df-9322-a11788049364)
# FUNCTIONS
Functions are blocks of reusable code that perform specific tasks. They are designed to take input arguments, process them, and return a result. Functions allow you to organize your code into modular pieces, making it easier to read, understand, and maintain.
## 1.Defining a Function:
To create a currency conversion function, you would use the (def )keyword fhe function name, a set of parentheses with any input parameters (if needed), and a colon.
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/1cb58d30-e947-4fd2-99c7-88d0276dde9a)
## 2.Input Parameters: 
Functions can take input parameters, which represent the data the function needs to perform its task. In the case of a currency converter, the input parameters could be the (amount) to be converted and the( exchange_rate) for the conversion.

## 3.Function Body: 
The function body contains the instructions that define how the currency conversion will take place. In this example, the function multiplies the (amount) by the (exchange_rate) to get the converted amount.
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/c7c2a38f-cb03-4cb8-ae47-8e7350f19e22)
## 4.Return Statement: 
The return statement is used to specify the value that the function will return once it has completed its task. In this case, the function returns the (converted_amount.)
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/c927d654-d0ef-4fb4-98c6-04d1b7a10673)
## 5.Calling the Function: 
To perform a currency conversion, you call the function with the appropriate arguments (values for amount and exchange_rate).
### Input:
This function is used to get user input, such as the amount to convert, the source currency, and the target currency.
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/64a885d6-68ca-41fa-b1e1-3e97b20a9a65)
Float is used to represents the floating point number. Of real numbers and is written with a decimal point dividing the integer and fractional parts.
### OUTPUT:
The output of a currency converter in Python is the converted amount of money.
For example , we converting 100 USD to INR:
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/3d5b3f78-96e0-4d39-baa7-653b12704233)
### Exceptional handle:
This function deals with potential errors, such as invalid inputs or connection problems when retrieving exchange rates from an external source. It ensures that the program gracefully handles unexpected situations.
Here we use, raise value and try catch error:
![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/d3a13ab6-67d6-4a0c-9464-43f1edda82df)
### Main function
This function ties everything together. It typically calls the input function to get user inputs, then calls the currency conversion function with the provided inputs, and finally displays the result using the display function.

![image](https://github.com/Monish-RS/Currency-Converter./assets/141045837/cba4888b-b550-49a4-b49c-d292d48e719c)


























