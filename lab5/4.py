def calculate_expression(expression):
    """
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    test_expression = expression
    test_expression = test_expression[:-1]
    test_expression = test_expression.split(" ")

    if "додати" in test_expression:
        test_expression.remove("додати")
    if "відняти" in test_expression:
        test_expression.remove("відняти")
    if "плюс" in test_expression:
        test_expression.remove("плюс")
    if "мінус" in test_expression:
        test_expression.remove("мінус")
    if "помножити" in test_expression:
        test_expression.remove("помножити")
    if "поділити" in test_expression:
        test_expression.remove("поділити")
    if "Скільки" in test_expression:
        test_expression.remove("Скільки")
    if "на" in test_expression:
        test_expression.remove("на")
    if "буде" in test_expression:
        test_expression.remove("буде")

    try:
        for i in range(len(test_expression)):
            test_expression[i] = int(test_expression[i])
    except:
        return "Неправильний вираз!"
        
    try:
        expression = expression[13:-1]
        expression = expression.replace("відняти", "-")
        expression = expression.replace("мінус", "-")
        expression = expression.replace("додати", "+")
        expression = expression.replace("плюс", "+")
        expression = expression.replace("помножити на", "*")
        expression = expression.replace("поділити на", "/")
        expression = expression.split(" ")

        for i in range(len(expression)):
            try:
                expression[i] = int(expression[i])
            except:
                continue

        while len(expression) > 1:
            try:
                if expression[1] == "+":
                    result = expression[0] + expression[2]
                    for i in range(3):
                        expression.pop(0)
                    expression.insert(0, result)

                if expression[1] == "-":
                    result = expression[0] - expression[2]
                    for i in range(3):
                        expression.pop(0)
                    expression.insert(0, result)

                if expression[1] == "*":
                    result = expression[0] * expression[2]
                    for i in range(3):
                        expression.pop(0)
                    expression.insert(0, result)

                if expression[1] == "/":
                    result = expression[0] / expression[2]
                    for i in range(3):
                        expression.pop(0)
                    expression.insert(0, result)
            except:
                break
    except:
        return "Неправильний вираз!"
    return int(expression[0])

print(calculate_expression("Скільки буде 8 мінус 3?"))
print(calculate_expression("Скільки буде 7 додати 3 помножити на 5?"))
print(calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?"))