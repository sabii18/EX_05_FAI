<h1>ExpNo 5 : Implement Simple Hill Climbing Algorithm</h1>

<h3>Name: SABEESHWARAN. P          </h3>
<h3>Register Number:  212225230234          </h3>

<h3>Aim:</h3>
<p>Implement Simple Hill Climbing Algorithm and generate a string by mutating a single character at each iteration.</p>

<h2>Theory:</h2>
<p>
Hill climbing is a variant of Generate and Test in which feedback from
the test procedure is used to help the generator decide which direction
to move in the search space. Feedback is provided in terms of a heuristic
function. The algorithm continuously improves the current solution until
the goal state is reached or no better neighboring state is found.
</p>

<h2>Algorithm:</h2>

<ol>
    <li>Generate a random string of the same length as the target string.</li>
    <li>Evaluate the initial state using a fitness function.</li>
    <li>If the current string matches the target string, stop the algorithm.</li>
    <li>Otherwise, select a character position and mutate the character.</li>
    <li>Evaluate the new string using the fitness function.</li>
    <li>If the new string has a better fitness score, accept it as the current state.</li>
    <li>If the new string is not better, retain the current state and try another mutation.</li>
    <li>Repeat until the fitness score becomes zero.</li>
    <li>Display the final string and its fitness score.</li>
</ol>

<hr>

<h2>Steps Applied:</h2>

<h3>Step-1</h3>
<p>Generate a random string of length equal to the given target string.</p>

<h3>Step-2</h3>
<p>Mutate the randomized string by changing one character at a time.</p>

<h3>Step-3</h3>
<p>Evaluate the fitness function or heuristic function by calculating the difference between the current string and the target string.</p>

<h3>Step-4</h3>
<p>Repeat Steps 2 and 3 until the fitness score becomes zero, indicating that the target string has been generated.</p>

<hr>



<h2>Python Program</h2>

<pre><code>
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
</code></pre>

<hr>

<h2>Output:</h2>
Score: 643  Solution :  8RzF:oG ]%;CPORRMe!zGvk<br>
Score: 609  Solution :  8RzF:oG ]%;CPqRRMe!zGvk<br>
Score: 604  Solution :  8RzF:oG ]%;CPqRRMe!zGqk<br>
Score: 594  Solution :  8RzF:oG ]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
....................................................<br>
..................................................<br>
................................................<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 0  Solution :  Artificial Intelligence<br>


<h2>Sample Input</h2>

<h3>Sample String:</h3>

<pre>
Artificial Intelligence
</pre>

<hr>

<h2>Sample Output</h2>

<img width="500" height="443" alt="image" src="https://github.com/user-attachments/assets/7ea6b7b7-88d2-490b-ab5f-d6e3a2f88dce" />




<hr>

<h2>Result</h2>

<p>Thus, the Simple Hill Climbing Algorithm was implemented successfully in Python 3 to generate the target string by mutating one character at a time and evaluating the fitness function until the score reached zero.</p>
