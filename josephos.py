def josephos(n,k):
    if n==1:
        return 0
    return (josephos(n-1,k)+k)%n
print(josephos(7,3))

output:
    3
