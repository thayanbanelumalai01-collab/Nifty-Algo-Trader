from core.logger import Logger


def print_banner():
    print("=" * 60)
    print("               NIFTY ALGO TRADER")
    print("=" * 60)


def print_banner():
    print("=" * 60)
    print("               NIFTY ALGO TRADER")
    print("=" * 60)


def main():
    print_banner()

    Logger.info("Application Started")
    Logger.info("Version : 0.0.1")
    Logger.info("Status : Ready")


if __name__ == "__main__":
    main()