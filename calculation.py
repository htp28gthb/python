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
        score = int(input("Score: "))
        scores.append(score)

    # Calculate the average score.
    average_score = get_average_scores(scores)

    # Print the average score.
    print(f"Average score: {average_score}")
