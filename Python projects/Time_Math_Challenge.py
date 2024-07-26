import random
import time
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

total_questions = 10
point = 0

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer
while True:
    mode = input("If you are ready, press q to start: ").lower()
    if mode == 'q':
        break

timer_start = time.time()

for i in range(total_questions):
    expression, answer = generate_problem()
    
    user_answer = input("Question number " + str(i + 1) + " : " + expression + " =  ")
        
    if user_answer == str(answer):
        point += 10
        print("That is a correct answer")
    else:
        print("That is an incorrect. The correct answer is", answer)


timer_end = time.time()

total_time = round(timer_end - timer_start, 2)

print("Congratulation! You finished in", total_time, "seconds.",
      "Your score is", point)
