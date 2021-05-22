def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        number = phone_book[i]
        number2 = phone_book[i+1]
        if number == number2[:len(number)]:
            answer = False
    return answer
