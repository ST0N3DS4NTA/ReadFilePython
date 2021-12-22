# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0

total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line.split()
    search = line.find('0')
    num = float(line[search:])
    count += 1
    total += num

print("Average spam confidence:", total/count)
