# strings
name = input(" Enter your name:")
print(f"Good morning {name}")

# letter
letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''
print(letter.replace("<|NAME|>","Manas").replace("<|DATE|>","19/05/2026"))'''

# detect double space 
m = "Manas is  hired"
print(m.find("  "))

# replace double sapce with single space 
print(m.replace("  ", " "))

# special characters 
letter = "Dear Manas,\nThis python course is nice.\nThanks!"
print(letter)
