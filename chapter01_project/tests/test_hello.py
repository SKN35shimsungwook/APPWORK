"""외부 프로세스로 hello.py 실행 결과를 검사한다."""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_hello_output():
    # 프로젝트의 실습 파일이 존재하는지 확인한다.
    script = ROOT / "hello.py"
    assert script.is_file(), f"실습 파일이 없습니다: {script}"
    # 현재 uv 환경의 Python을 이용해 별도 프로세스로 실행한다.
    # 한글 Windows 기본 인코딩(cp949)과 섞이지 않도록 입출력을 UTF-8로 맞춘다.
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                            capture_output=True, text=True, encoding="utf-8",
                            env={**os.environ, "PYTHONIOENCODING": "utf-8"}, check=False)
    assert result.returncode == 0, result.stderr
    assert "프로젝트: chapter01-development" in result.stdout
    assert "Python 버전: 3.12" in result.stdout
