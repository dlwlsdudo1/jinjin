from itertools import permutations
def solution(numbers):
    answer = 0
    num = [] 
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            num.append(int(''.join(j)))
 
    for i in list(set(num)): #중복제거
        if i==2:
            answer+=1
        for j in range(2,i):
            if i%j==0: #나누어떨어지면 -> 소수아님
                break
            elif j==i-1: #소수이면 answer+=1
                answer+=1
                
    return answer
