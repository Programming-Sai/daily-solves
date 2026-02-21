def minMovesToSeat(seats, students):
    students.sort()
    seats.sort()
    moves=0
    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])
    return moves