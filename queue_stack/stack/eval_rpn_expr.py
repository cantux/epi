digits = [chr(a) for a in range(48,58)]
print digits

chars = [chr(a) for a in range(91 - 26, 91)]
print chars
operators = {
        '+': lambda a, b: a + b, 
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
        }

def eval_exp(exp):

    tokens = exp.split(',')
    aux = []
    for x in tokens:
        if x in operators:
            aux.append(
                    operators[x](
                        aux.pop(), 
                        aux.pop()
                        )
                    )
        else:
            aux.append(int(x))

    return aux[0]

def test():
    print eval_exp("3,4,+")


if __name__ == "__main__":
  test()

