"""Configuration for browser in different environments."""
import os

def get_cloud_browser_args():
    """Return browser launch arguments for cloud environments."""
    return [
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-setuid-sandbox",
        "--no-sandbox",
        "--no-zygote",
        "--single-process",
        "--deterministic-fetch",
        "--disable-features=IsolateOrigins,site-per-process",
    ]

def is_cloud_environment():
    """Detect if running in a cloud environment."""
    return os.environ.get('STREAMLIT_SERVER_HEADLESS', 'false').lower() == 'true'
