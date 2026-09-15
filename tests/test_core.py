from antenna_measurement_cnf.core import hello


def test_hello_returns_hello():
    assert hello() == "Hello"


def test_hello_prints_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello"
