def solution(answers):
    student_answers = []
    student_answers.append([1, 2, 3, 4, 5]) # no.1
    student_answers.append([2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]) # no.2
    student_answers.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]) # no.3

    count = [0, 0, 0]

    for i in range(3):
        for o in range(len(answers)):
            if student_answers[i][o%len(student_answers[i])] == answers[o]:
                count[i] += 1
    
    
    
    answers = []
    for i in range(3):
        if count[i] == max(count):
            answers.append(i + 1)
    return answers

#answers	return
#[1,2,3,4,5]	[1]
#[1,3,2,4,2]	[1,2,3]
