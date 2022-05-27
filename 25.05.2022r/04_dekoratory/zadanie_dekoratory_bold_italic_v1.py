#@bold
#@italic

# #PRZYKŁAD:
# def foo(arg):
#     return f'To jest {arg}'
#
# wynik = foo('Ola ma psa')
# print(wynik)
#
# #<b><i>Ola ma psa</i><b>

def bold(f):
    def wrapper(arg):
        napis = f(arg)
        return f'<b>{napis}</b>'
    return wrapper

def italic(f):
    return lambda arg: f'<i>{f(arg)}</i>'


@bold
@italic
def foo(arg):
    return f'To jest {arg}'

foo('Ala')
print(foo('Ola'))


# @foo
# def italic(arg):
#     return f'To jest {arg}'
#
# wynik = foo('Ola ma psa')
# print(wynik)


