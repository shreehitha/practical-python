# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    shares = []
    sum = 0
    for line in f:
        x = float(line.split(',')[1])
        y = float(line.split(',')[2])
        z = round(x*y, 2)
        sum = sum + z
        print(sum)
    print(sum)   

 
    