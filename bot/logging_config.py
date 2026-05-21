import os, logging, time
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "trading_bot.log"

LOG_MODE = os.getenv("LOG_MODE", "minimal").lower()

_file_fmt   = "%(asctime)s IST  │  %(levelname)-8s  │  %(message)s"
_screen_fmt = "%(asctime)s IST  │  %(message)s"

_file_dtfmt   = "%Y-%m-%d %I:%M:%S %p"
_screen_dtfmt = "%I:%M:%S %p"


class ISTFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        tm = time.localtime(record.created)
        if datefmt:
            return time.strftime(datefmt, tm)
        return time.strftime("%Y-%m-%d %I:%M:%S %p", tm)


def setup_logging():
    file_fmt = _file_fmt
    screen_fmt = _screen_fmt
    file_dtfmt = _file_dtfmt
    screen_dtfmt = _screen_dtfmt

    file_formatter   = ISTFormatter(file_fmt,   datefmt=file_dtfmt)
    screen_formatter = ISTFormatter(screen_fmt, datefmt=screen_dtfmt)

    # used to silence library noise
    for lib in ("urllib3", "requests", "binance"):
        logging.getLogger(lib).setLevel(logging.WARNING)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    for h in root.handlers[:]:
        root.removeHandler(h)

    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(file_formatter)
    root.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(screen_formatter)
    root.addHandler(sh)


def get_logger(name):
    return logging.getLogger(name)