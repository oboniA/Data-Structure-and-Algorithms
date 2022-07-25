"""
    Write a function that takes two inputs n and m,
    and outputs the number of unique paths
    from the top left corner to bottom right corner of an n X m grid.

    Constrains: Can only move down, or right. 1 unit at a time

Formula:
grid(n, m) = 1 if (n=1 or m=1)
             grid(n, m-1) + grid(n-1, m)
"""


def grid(n, m):
     if n == 1 or m == 1 :
         return 1
     else:
         return grid(n, m-1) + grid(n-1, m)

if __name__=='__main__':
    print(grid(3, 3))