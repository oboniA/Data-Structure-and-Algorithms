"""
write a recusrive Function that given an input n
sums all the non-negative integers upto n
          sum(0) -> 0
          sum(1) -> 1
          sum(4) -> (1+2+3+4)
          sum(n) -> (1+2+3+.....+n)
"""

def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

if __name__=='__main__':
    print(sum(5))





