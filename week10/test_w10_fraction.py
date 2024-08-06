from w10_fraction import Fraction

def test_fraction_01(capsys):
    f = Fraction(1, 2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '1/2'

def test_fraction_02(capsys):
    f = Fraction(-1, 2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '-1/2'

def test_fraction_03(capsys):
    f = Fraction(1, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '-1/2'

def test_fraction_04(capsys):
    f = Fraction(-1, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '1/2'

def test_fraction_05(capsys):
    f = Fraction(0, 2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '0/2'

def test_fraction_06(capsys):
    f = Fraction(0, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '0/2'

def test_fraction_07():
    try:
        f = Fraction(1, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero.'
        assert True
    except Exception:
        assert False

def test_fraction_08():
    try:
        f = Fraction(-1, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero.'
        assert True
    except Exception:
        assert False

def test_fraction_09():
    try:
        f = Fraction(0, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero.'
        assert True
    except Exception:
        assert False
    