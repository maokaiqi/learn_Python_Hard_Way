things = ['a','b','c']
print things[1]
things[1] = 'z'
print things[1]
print things


stuff = {'name':'Zed', 'age':35, 'height':5*12+2}

print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = 'San Francisco'

print stuff['city']

stuff[1] = "Wow"

stuff[2] = "Neato"

print stuff[1]

print stuff[2]

print stuff
# {'city':'San francisco', 2:'Wow', 1:'Neato', 'name':'Zed', 'age':35, 'height':74}

del stuff['city']

del stuff[1]

del stuff[2]

print stuff


