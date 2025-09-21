import os
from pathlib import Path
import pytest
from terminal import Terminal
from commands.ls import LsCommand
from commands.mkdir import MkdirCommand
from commands.cd import CdCommand
from commands.pwd import PwdCommand
from commands.rm import RmCommand

def run_cmd_and_capture(cmd_obj, args, terminal, capsys):
    cmd_obj.execute(args, terminal)
    captured = capsys.readouterr()
    return captured.out.strip()

def test_mkdir_and_ls_and_cd_and_pwd(tmp_path, capsys):
    t = Terminal(project_root=tmp_path)
    # make dir
    mk = MkdirCommand()
    mk.execute(["foo"], t)
    # ls should show foo
    ls = LsCommand()
    out = run_cmd_and_capture(ls, [], t, capsys)
    assert "foo" in out
    # cd into foo
    cd = CdCommand()
    cd.execute(["foo"], t)
    # pwd should show '.' or relative path
    pwd = PwdCommand()
    out = run_cmd_and_capture(pwd, [], t, capsys)
    assert out in (".", "foo")

def test_rm_file(tmp_path, capsys):
    t = Terminal(project_root=tmp_path)
    # create file
    file = tmp_path / "a.txt"
    file.write_text("hello")
    ls = LsCommand()
    out = run_cmd_and_capture(ls, [], t, capsys)
    assert "a.txt" in out
    # rm it
    rm = RmCommand()
    rm.execute(["a.txt"], t)
    out = run_cmd_and_capture(ls, [], t, capsys)
    assert "a.txt" not in out
