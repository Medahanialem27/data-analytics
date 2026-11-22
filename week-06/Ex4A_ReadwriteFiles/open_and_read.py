f = open("week-06/Ex4A_ReadwriteFiles/about_me.txt", "r")
#print(f.read(50))
#print(f.read(50))
#print(f.readline(10))
#print(f.readline())
#for i in range(1,  5):
    #print(f.readline())
#print(f.readlines(1))
#print(f.readlines(1))
#print(f.readlines(10))
#print(f.readlines(10))
#print(f.readlines(-1))
#print(f.readlines(-1))

first_50_chars = f.read(50)

next_four_lines = []
for i in range(1, 5):
    next_four_lines.append(f.readline())

next_100_chars = f.readlines(100)
f.close()

print(f"First 50 characters: {first_50_chars}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100_chars}")