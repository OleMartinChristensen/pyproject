# test_with_pytest.py
from .context import hello


def test_always_passes():
    assert True


def test_hello_world(capsys):
    hello.hello_world()
    out, _ = capsys.readouterr()
    assert out == "Hello World\n"


def test_puss(capsys):
    hello.puss()
    out, _ = capsys.readouterr()
    assert out == "puss Sonja\n"
