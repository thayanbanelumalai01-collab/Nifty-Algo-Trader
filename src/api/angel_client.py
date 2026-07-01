from SmartApi import SmartConnect
from dotenv import load_dotenv
import pyotp
import os

from core.logger import Logger


class AngelClient:

    def __init__(self):
        # Load variables from .env
        load_dotenv()

        self.api_key = os.getenv("API_KEY")
        self.client_id = os.getenv("CLIENT_ID")
        self.mpin = os.getenv("MPIN")
        self.totp_secret = os.getenv("TOTP_SECRET")

        # Validate environment variables
        if not all([
            self.api_key,
            self.client_id,
            self.mpin,
            self.totp_secret
        ]):
            raise ValueError("Missing one or more environment variables in .env")

        self.smart_api = SmartConnect(api_key=self.api_key)

        # Session variables
        self.session = None
        self.jwt_token = None
        self.refresh_token = None
        self.feed_token = None

        Logger.info("AngelClient initialized successfully.")

    def login(self):
        """
        Login to Angel One SmartAPI
        """
        try:
            otp = pyotp.TOTP(self.totp_secret).now()

            session = self.smart_api.generateSession(
                clientCode=self.client_id,
                password=self.mpin,
                totp=otp
            )

            if session.get("status"):
                self.session = session
                self.jwt_token = session["data"]["jwtToken"]
                self.refresh_token = session["data"]["refreshToken"]
                self.feed_token = session["data"]["feedToken"]

                Logger.info(f"Login successful. Welcome {session['data']['name']}")
                client_id = session["data"]["clientcode"]
                Logger.info(f"Client ID: {client_id[:2]}****")

            else:
                Logger.error(f"Login failed: {session.get('message', 'Unknown error')}")
            return session

        except Exception as e:
            Logger.error(f"Login failed: {e}")
            return None