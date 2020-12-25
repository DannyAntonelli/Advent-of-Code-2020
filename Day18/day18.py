with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 18!")
print("="*30)

def getEx(expression):
    parenthesis = 1
    i = 0

    while parenthesis != 0:
        if expression[i] == "(":
            parenthesis += 1
        elif expression[i] == ")":
            parenthesis -= 1

        i += 1

    return expression[:i-1]

def evaluate(expression, precedence=False):
    start = expression.find("(") + 1
    while start != 0:
        subEx = getEx(expression[start:])
        subExPar = "(" + subEx + ")"
        expression = expression.replace(subExPar, evaluate(subEx, precedence))
        start = expression.find("(") + 1

    if not precedence:
        expressionList = expression.split(" ")

        if len(expressionList) == 1:
            return expressionList[0]
        else:
            operator = expressionList[1]
            num1 = int(expressionList[0])
            num2 = int(expressionList[2])
            
            if operator == "+":
                result = num1 + num2
            else:
                result = num1 * num2

            subEx = expressionList[0] + " " + operator + " " + expressionList[2]
            expression = expression.replace(subEx, str(result), 1)
            return evaluate(expression)
    
    else:
        expressions = expression.split("*")
        result = 1
        for exp in expressions:
            result *= int(evaluate(exp.strip()))
        return str(result)


result1 = 0
result2 = 0
for line in lines:
    result1 += int(evaluate(line))
    result2 += int(evaluate(line, True))

# Part one
print("Solution #1:", result1)

# Part two
print("Solution #2:", result2)