maxsize = 5

def createStack():
    final_stack = []
    return final_stack

def isFull(stack):
    if(len(stack) == maxsize):
        print("OverFlow condition, can't insert further")


    return len(stack) == maxsize


def push(stack, val):
    if isFull(stack):
        return

    stack.append(val)
    print('The value {} has been pushed'.format(val))

def peek(stack):
    if isFull(stack) == 0:
        print('Stack is pretty empty boi !')
        return

    print(stack[len(stack)-1])

stack = createStack()


push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
push(stack, 60)
push(stack, 70)

peek(stack)