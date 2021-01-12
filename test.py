
def is_adult(age):
    return age>18

def test_is_adult():
    assert is_adult(19)

x = input()


def test_first_pytest():
    result=int(x)>0
    assert result