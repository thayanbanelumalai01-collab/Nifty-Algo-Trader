from core.logger import Logger
from api.angel_client import AngelClient


def print_banner():
    print("=" * 60)
    print("               NIFTY ALGO TRADER")
    print("=" * 60)


def main():
    print_banner()

    Logger.info("Application Started")
    Logger.info("Version : 0.0.1")
    Logger.info("Status : Ready")

    client = AngelClient()

    session = client.login()

    if session:
        Logger.info("Application initialized successfully.")
    else:
        Logger.error("Unable to login.")


if __name__ == "__main__":
    main()