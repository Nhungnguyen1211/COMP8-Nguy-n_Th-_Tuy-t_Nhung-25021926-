n=int(input())
if 0<=n<=1:
    so_tien=9
elif n<=5:
    so_tien=9+(n-1)*5
elif n<=19:
    so_tien=9+4*5+(n-5)*3
else:
    so_tien=9+4*5+14*3+(n-19)*2
print(so_tien)