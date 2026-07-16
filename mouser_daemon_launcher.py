"""Qt-free entry point for the resident macOS daemon."""
from core.log_setup import setup_logging

setup_logging()

from core.macos_daemon import main


if __name__ == "__main__":
    raise SystemExit(main())
