
def find_repeat(numbers:list) -> list:
    print(numbers)
    arr = []
    repeat = []
    str_numbers = "".join(str(x) for x in numbers)
    print(str_numbers)
    for c in str_numbers:
        if c not in repeat:
            print("{} in {} = {}".format(c,str_numbers, str_numbers.split(c)))
            if len(str_numbers.split(c)) > 2:
                repeat.append(c)
    print(repeat)

def found_multiple_of_five(number:int) -> bool:
    up = number
    down = number
    step_up, step_down = 0,0
    for i in range(5):
        if up%5 != 0:
            up += 1
            
            step_up += 1
        else:
            return number + step_up
        
        if down %5 != 0:
            down -=1
            step_down +=1
        else:
            return number - step_down
        
                
            
def smalletDictionaryOrder(A:list, B:list)-> list:
    tamA, tamB = len(A), len(B)
    tam = tamA if tamA < tamB else tamB
    if tam > 0:
        for i in range(tam):
            if A[i] != B[i]:
                return A if A[i] < B[i] else B
    else:
        return []
    
    return A if tamA < tamB else B

if __name__ == "__main__":
    # test = [5,3,2,1,1,2]
    # find_repeat(test)
    
    testA = [-3,9,4,8,15]
    testB = [-3,10]
    print(smalletDictionaryOrder(testA, testB))
    
    print(found_multiple_of_five(8))
    