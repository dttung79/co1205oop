from w10_functions import hello

# capsys = capture system output/error
def test_hello(capsys):
    hello('Alice', 20)
    captured = capsys.readouterr()
    assert captured.out == f'Hello, I am Alice and I am 20 years old.\n'