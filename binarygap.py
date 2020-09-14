

def solution(N):
    # write your code in Python 3.6
    binary = bin(N).replace("0b", "")
    
    gap = []
    lis = [int(s) for s in binary]
    # import pdb;pdb.set_trace()
    for i in range(0,len(lis)):
        if lis[i] == 0:
            continue
        elif lis[i] == 1:
            if i == len(lis) -1:
                break
            til_end = lis[i:]
            gap.append(find_gap(til_end))           
        
        # if i == len(lis):
    gap = [0 if v is None else v for v in gap]
    # if None in gap:
    #     return 0
    return max(gap)  

def find_gap(end):
    length = len(end) -1
    count=0
    for i in range(1,len(end)):
        if end[i] ==0:
            count+=1
        elif end[i] == 1 or length == i:
            return count   

print(solution(9))
print(solution(15))
print(solution(1041))
print(solution(32))
print(solution(529))
print(solution(20))
