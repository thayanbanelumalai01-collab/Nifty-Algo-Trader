from core.logger import Logger


class Account:

    def __init__(self, angel_client):
        """
        Initialize the Account module.
        """
        self.client = angel_client
        self.smart_api = angel_client.smart_api

        Logger.info("Account module initialized.")

    def get_profile(self):
        """
        Fetch account profile.
        """
        try:
            profile = self.smart_api.getProfile(self.client.refresh_token)

            if profile.get("status"):
                Logger.info("Account profile fetched successfully.")
            else:
                Logger.error("Failed to fetch account profile.")

            return profile

        except Exception as e:
            Logger.error(f"Error fetching profile: {e}")
            return None