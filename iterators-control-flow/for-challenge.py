# split IP addresses into segments and print the length of those segments

address = input("Please enter an IP address: ")
segmentLength = 0
segment = 1
char = ""

for char in address:
    if char == ".":
        print("segment {} contains {} characters".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

if char != ".":
    print("segment {} contains {} characters".format(segment, segmentLength))

