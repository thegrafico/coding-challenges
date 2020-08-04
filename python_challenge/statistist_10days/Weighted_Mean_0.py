# Enter your code here. Read input from STDIN. Print output to STDOUT
# tam = input()
# xi = input()
# wi = input()
xi = '10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10'
wi = '1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'
xi = xi.split()
wi = wi.split()


xi = [float(x) for x in xi]
wi = [float(w) for w in wi]

result = []
for i in range(len(xi)):
    result.append(xi[i] * wi[i])

xi = sum(result)
wi = sum(wi)

print(xi,wi)
result = xi/wi

print(round(result,1))