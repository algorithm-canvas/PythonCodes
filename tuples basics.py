Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tea_types = ("Black","Green","Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[-1]
'Oolong'
>>> tea_types[0]
'Black'
>>> # tuples dosent change assignments
>>> 
>>> len(tea_types)
3
>>> more_tea=("Herbal","Earl Grey")
>>> all_tea = more_tea+tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> more_tea=("Herbal","Earl Grey","Herbal")
>>> more_tea.count("Herbal")
2
