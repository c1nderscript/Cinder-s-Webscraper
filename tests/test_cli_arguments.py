from cinder_web_scraper.main import parse_arguments


def test_cli_default():
    args = parse_arguments([])
    assert not args.cli and not args.gui


def test_cli_flag():
    args = parse_arguments(['--cli'])
    assert args.cli is True
