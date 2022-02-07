# divide and conquer algorithm for integer multiplication

from unicodedata import name


def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a == b:
        return a + b
    if a < b:
        return multiply(a, b - a) + a
    if a > b:
        return multiply(a - b, b) + b
  

if __name__ == '__main__':
    print(multiply(10,10))
    print(multiply(10,20))
    print(multiply(10,30))
    print(multiply(10,40))
    print(multiply(10,50))
    print(multiply(10,60))
    print(multiply(10,70))
    print(multiply(10,80))
    print(multiply(10,90))
    print(multiply(10,100))
    print(multiply(10,110))
    print(multiply(10,120))
    print(multiply(10,130))
    print(multiply(10,140))
    print(multiply(10,150))
    print(multiply(10,160))
    print(multiply(10,170))
    print(multiply(10,180))
    print(multiply(10,190))
    print(multiply(10,200))
    print(multiply(10,210))
    print(multiply(10,220))
    print(multiply(10,230))
    print(multiply(10,240))
    print(multiply(10,250))
    print(multiply(10,260))
    print(multiply(10,270))
    print(multiply(10,280))
    print(multiply(10,290))
    print(multiply(10,300))
    print(multiply(10,310))
    print(multiply(10,320))
    print(multiply(10,330))
    print(multiply(10,340))
    print(multiply(10,350))
    print(multiply(10,360))
    print(multiply(10,370))
    print(multiply(10,380))
    print(multiply(10,390))
    print(multiply(10,400))
    print(multiply(10,410))
        

