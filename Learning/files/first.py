s = "piyush is a new coder"

# with open("text.txt", "w") as f:
#     f.write(s)

# with open("text.txt", "a") as f: a => append
#     f.write(s)

# fp = open("test.txt", "w") # w here is for write
# fp.write(s)

fp = open("test.txt", "r")
s = fp.read()
print(s)