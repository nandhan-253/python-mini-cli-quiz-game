# Python Quiz Application

## Overview

This is a basic command-line quiz program written in Python. It presents multiple-choice questions to the user, evaluates their answers, and calculates a final score based on correct responses.

---

## Features

* Multiple-choice questions
* User input handling
* Answer validation
* Score tracking
* Final percentage calculation
* Displays user guesses and correct answers

---

## Technologies Used

* Python (Core concepts: loops, lists/tuples, conditionals)

---

## Project Structure

```
quiz.py   # Main Python script
README.md # Project documentation
```

---

## How It Works

1. Questions and options are stored in tuples.
2. The program loops through each question.
3. User inputs their answer (A, B, or C).
4. The program checks if the answer is correct.
5. Score is updated accordingly.
6. At the end:

   * All guesses are displayed
   * Correct answers are shown
   * Final percentage score is calculated

---

## How to Run

1. Make sure Python is installed.
2. Save the script as `quiz.py`.
3. Run the program:

```bash
python quiz.py
```

---

## Example Output

```
1) In human anatomy, what does the 'hallux' refer to?
A. foot
B. big toe
C. shoulder
Enter your guess: B
You guessed B! is correct
```

---

## Scoring

* Each correct answer increases the score.
* Final score is calculated as:

```
(score / total_questions) * 100
```

---

## Future Improvements

* Add more questions dynamically
* Randomize questions
* Add a timer for each question
* Create a GUI version using Tkinter or web app

---

## Author

Dev

---
