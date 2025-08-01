def calcSum(a , b):
    sum = a + b
    print(sum)
calcSum(5, 10)
calcSum(0, 90)
calcSum(2, 20)

def print_hello():
    print("Hello World")

print_hello()
print_hello()
print_hello()
print_hello()

print('apnacollege' , end=" ")
print("zohaibkacollege")

def cal_product(a= 2, b=6):
    print(a * b)
    return a * b
    
cal_product()

cities = ["FSBD", "lhr", "multan", "ISBD"]
Heros = ['thorr','Arfa Karim','shakh_ti','raja','raho','sani','R nait']

def print_len(list):
    print(len(list))

print(cities)
print(Heros)

# Q: 1  
# WAP to program to find the factoiral of N,: N is the paraMeter

def call_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= 1
        print(fact)

    call_fact(5)

# WAF to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =",inr_val, "INR")

converter(500)