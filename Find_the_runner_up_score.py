if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=set(arr)
    l=list(a)
    sortarr=sorted(l)
    b=sortarr[-2]
    print(b)
