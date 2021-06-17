def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 !=0:
            answer += '수'
        else:
            answer += '박'

    return answer
#print(solution(10))
# 수, 박 을 따로 홀수인지 짝수인지 구분지어서 range문 이용해서 값 생성






#n은 길이 10,000이하인 자연수입니다.

#n	return
#3	"수박수"
#4	"수박수박"