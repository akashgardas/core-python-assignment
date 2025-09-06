# Handles where no ratings are avialable
def calc_pos_feedback(ratings: list) -> float:
    '''
        Calculates the percentage of positive feedback ratings
        Returns: Positive Feedback Percentage
    '''
    if len(ratings) == 0:
        return None

    return (ratings.count(4) + ratings.count(5)) / len(ratings) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

pos_feedback = calc_pos_feedback(ratings)
print(f'Positive Feedback: {pos_feedback}')
