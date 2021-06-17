def solution(a, b):
    answer = 0
    if a == b: # a = b
        return a 
    elif a > b: 
        for i in range(b, a+1): # b ~ a+1  i
            answer += i        # i = answer
        return answer
    else:
        for i in range(a, b+1): # a ~ b+1
            answer += i        
        return answer

# print(solution(5, 3))



    
#a	b	return
#3	5	12
#3	3	3
#5	3	12