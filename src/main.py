from core.logger import Logger
from api.angel_client import AngelClient
from api.account import Account

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

        account = Account(client)

        profile = account.get_profile()

        if profile:
            print("\n" + "=" * 60)
            print("ACCOUNT PROFILE")
            print("=" * 60)
            print(f"Name      : {profile['data']['name']}")
            print(f"Client ID : {profile['data']['clientcode'][:2]}****")
            email = profile["data"].get("email")

            if not email:
                email = "Not Available"
                print(f"Email     : {email}")
            print("=" * 60)

        else:
            Logger.error("Unable to login.")


if __name__ == "__main__":
    main()