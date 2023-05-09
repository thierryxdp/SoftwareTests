def TipoTriangulo(a,b,c):
    if (a <= 0 or b <= 0 or c <= 0):
        return "invalido"
		
    if (a+b >= c and a+c >= b and b+c >= a):
        if (a==b and b == c):
            return "equilatero"
        if (a==b or a==c or b==c):
            return "isosceles"
        return "escaleno"
    return "invalido"

def TestsAutomation(testFunction, tests):
    successTests = 0
    failedTests = 0
    failedTestsMessages = []

    for index, test in enumerate(tests):
        testInput = test[0]
        expectedValue = test[1]
        result = testFunction(*testInput)
        if (result != expectedValue):
            failedTests += 1
            failedTestsMessages.append("\nTest " + str(index) + " failed.\n    Expected value was: " +  
            str(expectedValue) + " \n    but got this: " + str(result))
        else:
            successTests += 1
    
    print(successTests, "/", len(tests), "tests passed.")
    for failedTestMessage in failedTestsMessages:
        print(failedTestMessage)

# TestsAutomation(
#     TipoTriangulo,
#     [
#         [[0,0,0], "invalido"],
#         [[-1,2,3], "invalido"],
#         [[-2,-4,-9], "invalido"],
#         [[3,4,7], "invalido"],
#         [[3,4,10], "invalido"],
#         [[3,4,5], "escaleno"],
#         [[6,8,7], "escaleno"],
#         [[3,3,4], "isosceles"],
#         [[6,8,6], "isosceles"],
#         [[9,5,5], "isosceles"],
#         [[3,3,3], "equilatero"]
#     ])

# Caso de Testes

# 1) [0,0,0] resultado esperado -> não é triângulo
# 1) resultado da funcao: invalido

# 2) [-1,2,3] resultado esperado -> não é triângulo
# 2) resultado da funcao: invalido

# 3) [-2,-4,-9] resultado esperado -> não é triângulo
# 3) resultado da funcao: invalido

# 4) [3,4,7] resultado esperado -> não é triângulo
# 4) resultado da funcao: escaleno

# 5) [3,4,10] resultado esperado -> não é triângulo
# 5) resultado da funcao: invalido

# 6) [3,4,5] resultado esperado -> triângulo escaleno
# 6) resultado da funcao: escaleno

# 7) [6,8,7] resultado esperado -> triângulo escaleno
# 7) resultado da funcao: escaleno

# 8) [3,3,4] resultado esperado -> triângulo isósceles
# 8) resultado da funcao: isosceles

# 9) [6,8,6] resultado esperado -> triângulo isósceles
# 9) resultado da funcao: isosceles

# 10) [9,5,5] resultado esperado -> triângulo isósceles
# 10) resultado da funcao: isosceles

# 11) [3,3,3] resultado esperado -> triângulo equilátero
# 11) resultado da funcao: equilatero