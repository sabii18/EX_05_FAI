
import random
import string

def fitness(current, target):
    score = 0
    for a, b in zip(current, target):
        score += abs(ord(a) - ord(b))
    return score

def hill_climbing(target):
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    current = ''.join(
        random.choice(characters) for _ in range(len(target))
    )

    score = fitness(current, target)
    print("Score:", score, " Solution :", current)

    while score > 0:
        improved = False

        for i in range(len(target)):
            if current[i] == target[i]:
                continue

            candidate_char = target[i]
            candidate = current[:i] + candidate_char + current[i + 1:]
            candidate_score = fitness(candidate, target)

            if candidate_score < score:
                current = candidate
                score = candidate_score
                improved = True
                print("Score:", score, " Solution :", current)

                if score == 0:
                    break

        if not improved:
            break

    if score == 0:
        print("Target string generated successfully!")
    else:
        print("Local optimum reached.")

target = input("Enter the target string: ")
hill_climbing(target)
