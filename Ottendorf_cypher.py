# Ottendorf cypher
# Findings from clue files
import re
print ("Finding the name of files from Clue file")

# To open the Clue file
Clue = open('Clue.txt')
C1 = Clue.read()

# To find list of triplets file name
my_string = C1
my_pattern = "(\d+.txt)|(\d+.TXT)"
Lfa = re.findall(my_pattern, my_string)
print(Lfa)
for i in range(len(Lfa)):
    Lfa[i] = Lfa[i][0] + Lfa[i][1]

print (Lfa)

# To check for the file
for i in range(len(Lfa)):
    try:
        L_T = open(Lfa[i]).read()
        print ("file found")
    except:
        print ("File not found")

# To find the file name of secret key
my_string = C1
my_pattern = "(_(\B[A-Z]{2}\B)\d{3}\.(txt|.TXT))"
Sfa = re.findall(my_pattern, my_string)
Sfa1 = []

# To merge the sub lists in a list
for i in Sfa:
    Sfa1 += i

print (Sfa1)

# To check for the file
for i in range(len(Sfa1)):
    try:
        S_K = open(Sfa1[i]).read()
        print ("File found")
    except:
        print ("File not found")


# Decoding the Secret Message
# Reading the Secret_Key file in to a list
secret_key = open("_DZ854.txt")
SK_lines = secret_key.readlines()
SK_Elines = list()
for line in SK_lines:
    line = line.strip()
    line = line.strip('')
    line = line.split(" ")
    SK_Elines.append(line)
print (SK_Elines)
S = SK_Elines

# Reading the List of Triplets file in to a list
list_triplets = open("3245656.TXT")
LT_lines = list_triplets.readlines()
LT_Elines = list()
for line in LT_lines:
    line = line.strip()
    line = line.split("-")
    LT_Elines.append(line)
print (LT_Elines)
L = LT_Elines

# Changing the List of triplets in to list of integers
L2 = [map(int, x) for x in L]
print (L2)

# Decoding the secrete message
C_D = []
for i in range(len(L2)):
    j = L2[i][0]
    k = L2[i][1]
    l = L2[i][2]
    C_D.append(S[j][k][l])
print (C_D)

CDF = ''.join(C_D)
print (CDF.upper())




