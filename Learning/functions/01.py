def funct1():
    print(3)
    # indentation is how function's work is defined

funct1()

name = "piyush"
print(name)

print(name[0])
print(name[0:3]) # this creates a new string containing char value of piyush as mentioned as strings are immutable

# name[a:b] => from a(0) to b-1
# start from 0 and go till 3 -> char

print(name.upper()) # full caps
print(name.capitalize()) # first char caps
print(name.count("y"))

def test(name, date):
    st = f'hi this is {name} and i will get my job at {date}'
    print(st)


test("Piyush", "2025")

def avg(a, b):
    return (a + b)/2

print(avg(2, 5))