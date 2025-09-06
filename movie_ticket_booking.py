# track - available, booked seats
# book, cancel tickets

class Theatre:
    '''
        Theatre class that controls ticket booking and cancelling along with feature of checking seat availability
        Method: book_ticket, cancel_ticket, get_available_seats
    '''

    total_seats = 10
    booked_seats = []
    available_seats = None
    
    def __init__(self, total_seats=10):
        '''
            Initializes the number of seats in the Theatre and initializes the available seats for booking
        '''
        self.total_seats = total_seats
        self.available_seats = [i for i in range(1, self.total_seats + 1)]
    
    # Prevents booking already booked seat
    def book_ticket(self, seat: int) -> None:
        '''
            Books the seat if it is available
        '''

        if seat not in self.booked_seats:
            self.booked_seats.append(seat)
            self.available_seats.remove(seat)
        else:
            print(f'Seat {seat} is already booked')

    def cancel_ticket(self, seat: int) -> None:
        '''
            Cancels an already booked seat
        '''

        if seat in self.booked_seats:
            self.booked_seats.remove(seat)
            self.available_seats.append(seat)
        else:
            print(f'Seat {seat} is not booked yet')
    
    def get_available_seats(self) -> list:
        '''
            Returns: A list of available seats for booking
        '''
        
        return sorted(self.available_seats)

# Testing
total_seats = 10
booking_seats = [2, 5, 7, 2]
cancelling_seats = [2, 7, 3]

theatre = Theatre()
# Booking
for seat in booking_seats:
    theatre.book_ticket(seat)

# Available Seats
print(f'Available Seats: {theatre.get_available_seats()}')

# Cancelling
for seat in cancelling_seats:
    theatre.cancel_ticket(seat)

# Available Seats
print(f'Available Seats: {theatre.get_available_seats()}')