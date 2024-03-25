Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
chai_types = {"Masala":"Spicy", "Ginger": "Zesty", "Green": "Mild"}
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
chai_types["Ginger"]
'Zesty'
chai_types.get("Green")
'Mild'
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
chai_types["Green"] = "Fresh"
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
for tea in chai_types:
        print(chai)

        
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(chai)
NameError: name 'chai' is not defined
for tea in chai_types:
        print(tea)

        
Masala
Ginger
Green
for tea in chai_types
SyntaxError: expected ':'
for tea in chai_types:
        print(tea,chai_types[chai])

        
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    print(tea,chai_types[chai])
NameError: name 'chai' is not defined
for tea in chai_types:
        print(tea,chai_types[tea])

        
Masala Spicy
Ginger Zesty
Green Fresh
for tea, swad in chai_types.items():
        print(tea, swad)

        
Masala Spicy
Ginger Zesty
Green Fresh
if "Masala"in chai_types:
        print("I have masala cha")

        
I have masala cha
print(len(chai_types))
3
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
chai_types["Earl Grey"] = "Citrus"
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
chai_types.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    chai_types.pop()
TypeError: pop expected at least 1 argument, got 0
chai_types.pop("Earl Grey")
'Citrus'
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
chai_types.popitem()
('Green', 'Fresh')
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
chai_types["Green"] = "Fresh"
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
del chai_types["Green"]
chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
chai_types_copy = chai_types.copy()
chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> tea_shop = {
...     "chai": {"Masala":"Spicy", "Ginger":"Zesty"},
...     "garmi": {"Green":"Mild", "Black":"Strong"}
...     }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'garmi': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> square_num = {x:x**2 for x in range(10)}
>>> sqaure_num
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sqaure_num
NameError: name 'sqaure_num' is not defined. Did you mean: 'square_num'?
>>> square_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> sqaure_num.clear()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sqaure_num.clear()
NameError: name 'sqaure_num' is not defined. Did you mean: 'square_num'?
>>> square_num.clear()
>>> square_num
{}
>>> keys = ["Masala","Ginger","Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict =  dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict =  dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
