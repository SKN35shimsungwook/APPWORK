"""CLI 입출력에 대한 pytest 테스트."""
from catalog.cli import main

def test_cli_list(tmp_path, capsys):
    code = main(["--data", str(tmp_path / "products.json"), "list"])
    assert code == 0
    assert "무선 키보드" in capsys.readouterr().out

def test_cli_order(tmp_path, capsys):
    code = main(["--data", str(tmp_path / "products.json"), "order", "1", "2"])
    assert code == 0
    assert "63,000원" in capsys.readouterr().out

def test_cli_error(tmp_path, capsys):
    code = main(["--data", str(tmp_path / "products.json"), "order", "99", "1"])
    assert code == 1
    assert "오류:" in capsys.readouterr().out
