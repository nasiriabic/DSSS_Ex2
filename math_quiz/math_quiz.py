import random

def gen_rand_int(min_val, max_val):
    """
    Generate a random integer between min_val and max_val.

    Parameters:
        min_val (int): Minimum value for the random integer.
        max_val (int): Maximum value for the random integer.

    Returns:
        int: A random integer between min_val and max_val.
    """

    try:
        # Check if min_val and max_val are integers
        if not isinstance(min_val, int) or not isinstance(max_val, int):
            raise ValueError("min_Val and max_Val must be integers.")
        
        # If they are integers, generate random integers
        return random.randint(min_val, max_val)
    
    except ValueError as e:
        # If they are not integers, catch the exception and assign some default random values
        print(f"Error: {e}")
        print("Assigning default random values.")
        return random.randint(1, 5)


    return random.randint(int(min_val), int(max_val))

def gen_rand_operator():
    """
    Generates a random operator: '+', '-', or '*'.

    Returns:
        str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def sub_mul_add(operand1, operand2, operator):
    """
    Performs the Add, Sub, or Mul operation based on the given operator.

    Parameters:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operator (str): The operator ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem string and the correct answer.
    """
    problem = f"{operand1} {operator} {operand2}"
    if operator == '-':
        result = operand1 - operand2
    elif operator == '+':
        result = operand1 + operand2
    else:
        result = operand1 * operand2
    return problem, result

def math_quiz():
    """
    Conducts a math quiz game where the player needs to solve randomly generated math problems.
    """
    grades = 0
    num_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        operand1 = gen_rand_int(1, 10)
        operand2 = gen_rand_int(1, 5.5)
        operator = gen_rand_operator()

        problem, answer = sub_mul_add(operand1, operand2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            grades += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {grades}/{num_questions}")

if __name__ == "__main__":
    math_quiz()
