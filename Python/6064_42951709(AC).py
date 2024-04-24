a,b,c= map(int,input().split())
c = (a if a<b else b) if ((a if a<b else b)<c) else c
print(c)
Wed Jul  2 15:00:28     2025 - forcing change for commit
