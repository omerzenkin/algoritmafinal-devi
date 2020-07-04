#SORU1
o = input("Tarihi giriniz :")
m = o.split("-");
e = m[0]
r = m[1]
z = m[2]

if(r == "01" or r == "1"):
    r = "Ocak"
elif(r=="02" or r == "2"):
    r = "Şubat"
elif(r=="03" or r == "3"):
    r = "Mart"
elif(r=="04" or r == "4"):
    r = "Nisan"
elif(r=="05" or r == "5"):
    r = "Mayıs"
elif(r=="06" or r == "6"):
    r = "Haziran"
elif(r=="07" or r == "7"):
    r = "Temmuz"
elif(r=="08" or r == "8"):
    r = "Ağustos"
elif(r=="09" or r == "9"):
    r = "Eylül"
elif(r=="10"):
    r = "Ekim"
elif(r=="11"):
    r = "Kasım"
elif(r=="12"):
    r = "Aralık"

print("Tarih:" + e,r,z)


#SORU2
o = int(input("x değerini giriniz: "))
if(o>=16 or o<0):
    print("Girilen sayı 16  ve 16'dan büyük veya negatif olamaz")
    input()
    exit()

if(o>=9 and o<16):
    m = 0
    for r in range(2,(2*o)+1,2):
        m+=r
    print("Toplam: " + str(m))
    input()

elif(o<9 and o>=0):
    e = 3*o
    m = 1

    for r in range(e,0,-1):
        m = r*m
    print("Faktöriyel " + str(e) + ': ' + str(m))
    input()
#SORU3
    o = {
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
  "e": 5,
  "f": 6,
  "g": 7,
  "h": 8,
  "i": 9,
  "j": 10,
  "k": 11,
  "l": 12,
  "m": 13,
  "n": 14,
  "o": 15,
  "p": 16,
  "q": 17,
  "r": 18,
  "s": 19,
  "t": 20,
  "u": 21,
  "v": 22,
  "w": 23,
  "x": 24,
  "y": 25,
  "z": 26,
  "ı":12,
  "ö":15,
  "ş":19,
  "ç":3,
  "ğ":7
}

m = [
    [1,2,-1],
    [2,5,2],
    [-1,-2,2]
]

def sifre(e):
    r=[[0],
        [0],
        [0]]
    for z in range(len(m)):
        for n in range(len(e[0])):
            for g in range(len(e)):
                r[z][n] +=m[z][g]*e[g][n]
    print('\n',r)

r = "omerzenkinom"

z = [];
for i in r:
    z.append(o[i])

j=0
for g in range(len(z)):
    if(g%3 == 0 and g != 0):
        sifre(n) 
        n = [[0],
            [0],
            [0]]
        j=0
    n[j][0] = z[g]
    j+=1
#SORU4
    o = str(1904107502)
m = int(o[len(o)-2:])
e = []

for r in range(2,m+1):
    n = 0;
    for z in range(2,r):
        if(r % z == 0):
            n+=1
            
    if(n==0):
        e.append(r)

print(e)
input()