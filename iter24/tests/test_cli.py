from cli.runner import run

def test_dry_run_no_exec(capsys):
    run({"dry_run": True, "cmd": "deploy"})
    assert "[DRY RUN]" in capsys.readouterr().out

# iteration 24
