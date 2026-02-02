import os
from dotenv import load_dotenv

load_dotenv()

GESTURE_MAP = {
    'thumbs_up': 'yes',
    'thumbs_down': 'no',
    'open_palm': 'hello',
    'fist': 'stop',
    'pointing': 'what'
}

CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.7))
TIMEOUT_SECONDS = float(os.getenv('TIMEOUT_SECONDS', 4.0))
SESSION_ID = os.getenv('SESSION_ID', "session_001")
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
GESTURE_COOLDOWN_SECONDS = float(os.getenv('GESTURE_COOLDOWN_SECONDS', 2.5))

if not WEBHOOK_URL:
    print("Warning: WEBHOOK_URL not found in environment variables.")