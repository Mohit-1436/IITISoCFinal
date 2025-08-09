# config/config.py

import os
from dotenv import load_dotenv
from pathlib import Path

class Config:
    """
    Handles loading and accessing configuration settings.
    Prioritizes environment variables set directly in the system.
    """
    def __init__(self):
        # Path to the .env file for local development
        dotenv_path = Path(__file__).parent.parent / '.env'
        
        # Load environment variables from .env file only if it exists
        if dotenv_path.exists():
            load_dotenv(dotenv_path=dotenv_path)

        # Load all environment variables from the system into a dictionary
        self.settings = {key: value for key, value in os.environ.items()}

    def get(self, key, default=None):
        """
        Retrieves a configuration value by key.
        """
        return self.settings.get(key, default)

    def validate_config(self):
        """
        Validates that essential API keys and settings are present.
        """
        print("Validating configuration...")
        required_keys = [
            'ALPHA_VANTAGE_API_KEY',
            'NEWS_API_KEY',
            'FRED_API_KEY',
            'DATABASE_PATH'
        ]
        
        missing_keys = [key for key in required_keys if not self.get(key)]
        
        if missing_keys:
            print(f"❌ Missing required configuration keys: {', '.join(missing_keys)}")
            # In a production environment, you might want to raise an exception here.
            return False
            
        print("All essential keys found.")
        return True

# Create a single instance of the Config class to be used across the application
config = Config()
