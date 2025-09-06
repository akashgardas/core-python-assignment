def calc_fare(trip_dist, base_fare=50, dist_fare=10) -> float:
    '''
        Calculates the total fare amount based on the base fare and the distance fare
        Returns: Total Fare Amount
    '''

    total_amt = base_fare + trip_dist * dist_fare
    return total_amt

trips = [5, 10, 3]  # Distances in km

total_fare = 0
for trip in range(1, len(trips) + 1):
    fare_amt = calc_fare(trips[trip - 1])
    total_fare += fare_amt
    print(f'Trip {trip}: ${fare_amt}')

print(f'Total Fare: ${total_fare}')    
