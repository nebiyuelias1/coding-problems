
def solution(P, S):
    people_count = sum(P)
    seats = sorted(S, reverse=True)
    
    car_count = 0
    while people_count > 0:
        people_count = people_count - seats[car_count]
        car_count = car_count + 1
        
    return car_count