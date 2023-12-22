def calculate(avg_score, max_score, base):
    avg_score = max(0, min(avg_score, max_score))
    percentage = (avg_score / max_score) * 100
    scholarship = percentage * base
    return scholarship