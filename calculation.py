def get_average_scores(scores):
    """
    Calculates the average of a list of scores.
    Args:
      scores: A list of scores.
    Returns:
      The average of the scores.
    """

    total_score = sum(scores)
    number_of_scores = len(scores)
    return total_score / number_of_scores


if __name__ == "__main__":
    # Get the scores from the user.
    scores = []
    candidate = int(input("Number of candidates: "))
    for i in range(candidate):
        while True:
            score = int(input("Score: "))
            if 100 <= score <= 999:
                scores.append(score)
                break  # Exit the loop if the score is valid
            else:
                print("Score must be in the range of 100 and 999")

    # Calculate the average score.
    average_score = get_average_scores(scores)

    # Print the average score.
    print(f"Average score: {average_score:1.2f}")
