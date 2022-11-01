#Square pattern
print('Square Pattern')
for i in range(0,5):
    for j in range(0,5):
        print('*',end = ' ')
    print()

print('Square Pattern Simplier')
n=5
print(f"{'* '*n}\n"*n)


#Hollow Square pattern
print('----------------------')
print('Hollow Square Pattern')
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end = ' ')
        else:
            print(' ',end = ' ')
    print()

#Left Triangle pattern
print('----------------------')
print('Left Triangle Pattern')
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end = ' ')
    print()

#Right Triangle pattern
print('----------------------')
print('Right Triangle Pattern')
n=5
for i in range(n):
    for j in range(1,i+1):
        print('*', end = ' ')
    print()

