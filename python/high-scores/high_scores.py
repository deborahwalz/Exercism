def latest(scores):
    """
    Return the last added score.
    """
    return scores[-1]


def personal_best(scores):
    """
    Return the highest score from the list.
    """
    return max(scores)


def personal_top_three(scores):
    """
    Return the three highest scores.
    """
    return sorted(scores, reverse=True)[:3]