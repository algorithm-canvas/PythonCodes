Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tea_varieties = ["Black", "Green", "Ola", "White"]
print(tea_varieties)
['Black', 'Green', 'Ola', 'White']
print(tea_varities[0])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(tea_varities[0])
NameError: name 'tea_varities' is not defined. Did you mean: 'tea_varieties'?
print(tea_varieties[0])
Black
print(tea_varieties[1])
Green
print(tea_varieties[-1])
White
print(tea_varieties[-4])
Black
print(tea_varieties[-1:-4])
[]
print(tea_varieties[1:3])
['Green', 'Ola']
print(tea_varieties[:3])
['Black', 'Green', 'Ola']
print(tea_varieties[0:])
['Black', 'Green', 'Ola', 'White']
print(tea_varieties[0:3:1])
['Black', 'Green', 'Ola']
tea_varieties[3] = "oyo"
print(tea_varieties)
['Black', 'Green', 'Ola', 'oyo']
tea_varieties = ["Black", "Green", "Ola", "White"]
print(tea_varieties)
['Black', 'Green', 'Ola', 'White']
print(tea_varieties[1:3])
['Green', 'Ola']
tea_varieties[1:3] = ["jai","hind"]
print(tea_varieties)
['Black', 'jai', 'hind', 'White']
tea_varieties[1:1]
[]
tea_varieties[1:2]
['jai']
tea_varieties[1:2]=[]
print(tea_varieties)
['Black', 'hind', 'White']
tea_varieties = ["Black", "Green", "Ola", "White"]
print(tea_varieties)
['Black', 'Green', 'Ola', 'White']
for superman in tea_varieties:
        print(superman)

        
Black
Green
Ola
White
for tea in tea_varieties:
    print(tea, end="@")

    
Black@Green@Ola@White@
tea_varities
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tea_varities
NameError: name 'tea_varities' is not defined. Did you mean: 'tea_varieties'?
tea_varieties
['Black', 'Green', 'Ola', 'White']
if "oolonf" in tea_varieities:
        print("I have oolong")

        
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    if "oolonf" in tea_varieities:
NameError: name 'tea_varieities' is not defined. Did you mean: 'tea_varieties'?
tea_varieties.append("oolonf")
tea_varieties
['Black', 'Green', 'Ola', 'White', 'oolonf']
if "oolonf" in tea_varieities:
        print("I have oolong")

        
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    if "oolonf" in tea_varieities:
NameError: name 'tea_varieities' is not defined. Did you mean: 'tea_varieties'?
if "oolonf" in tea_varieties:
        print("I have oolong")

        
I have oolong
tea_varieties
['Black', 'Green', 'Ola', 'White', 'oolonf']
tea_varieties.pop()
'oolonf'
tea_varieties
['Black', 'Green', 'Ola', 'White']
tea.varieties.remove("green")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tea.varieties.remove("green")
AttributeError: 'str' object has no attribute 'varieties'
tea_varieties.remove("green")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tea_varieties.remove("green")
ValueError: list.remove(x): x not in list
>>> tea_varieties.remove("Green")
>>> tea_varieties
['Black', 'Ola', 'White']
>>> tea_varieties.insert(1,"green")
>>> tea_varieties
['Black', 'green', 'Ola', 'White']
>>> tea_varieties_copy = tea_varieties.copy()
>>> tea_varieties_copy.append("Lemon")
>>> tea_varieties_copy
['Black', 'green', 'Ola', 'White', 'Lemon']
>>> square_nums = [x**2 for x in range(10)]
>>> square_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> print(y)
range(0, 10)
>>> square_nums = [x for x in range(10)]
>>> square_nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> cube_num = [y**3 for y in range (500)]
>>> cube_num

>>> cube_num = [y**3 for y in range (100)]
>>> cube_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167, 13824, 15625, 17576, 19683, 21952, 24389, 27000, 29791, 32768, 35937, 39304, 42875, 46656, 50653, 54872, 59319, 64000, 68921, 74088, 79507, 85184, 91125, 97336, 103823, 110592, 117649, 125000, 132651, 140608, 148877, 157464, 166375, 175616, 185193, 195112, 205379, 216000, 226981, 238328, 250047, 262144, 274625, 287496, 300763, 314432, 328509, 343000, 357911, 373248, 389017, 405224, 421875, 438976, 456533, 474552, 493039, 512000, 531441, 551368, 571787, 592704, 614125, 636056, 658503, 681472, 704969, 729000, 753571, 778688, 804357, 830584, 857375, 884736, 912673, 941192, 970299]
