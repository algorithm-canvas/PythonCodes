Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
chai_type = "masala"
quantity = 2
order = "I ordered {} cup of {} chai"
order
'I ordered {} cup of {} chai'
print(order.format(quantity, chai_type))
I ordered 2 cup of masala chai
chai_variety = ["Lemon", "Masala", "Ginger"]
chai_variety
['Lemon', 'Masala', 'Ginger']
print("".join(chai_variety))
LemonMasalaGinger
print("-".join(chai_variety))
Lemon-Masala-Ginger
print(", ".join(chai_variety))
Lemon, Masala, Ginger
>>> chai = "Masala Chai"
>>> chai
'Masala Chai'
>>> print(len(chai))
11
>>> print chai[0]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> chai[0]
'M'
>>> for letter in chai:
...     print(letter)
... 
...     
M
a
s
a
l
a
 
C
h
a
i
>>> chai = "He said, \"Masala Chai is awesome\" "
>>> chai
'He said, "Masala Chai is awesome" '
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nchai"
>>> print(chai)
Masala\nchai
>>> chai = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
