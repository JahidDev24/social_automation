import requests
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/automation.log'),
        logging.StreamHandler()
    ]
)

def load_config():
    with open('config/config.json', 'r') as f:
        return json.load(f)

def generate_fallback_content(platform):
    """Generate fallback content if API fails."""
    return (
        f"Tech Update for {platform.capitalize()}\n"
        "Exciting news in tech! AI is transforming industries with new innovations.\n"
        "Stay tuned for more updates! #TechNews"
    )

def generate_content(platform="instagram"):
    config = load_config()
    try:
        url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {config['xai_api_key']}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant creating engaging social media content."
                },
                {
                    "role": "user",
                    "content": (
                        f"Generate a short tech news summary (100-150 words) or a creative tech idea "
                        f"for a {platform} post/reel. Include a catchy headline and format for social media engagement."
                    )
                }
            ],
            "model": "grok-4-latest",
            "stream": False,
            "temperature": 0
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        content = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No content generated")
        logging.info(f"Content generated for {platform}")
        return content
    except Exception as e:
        logging.error(f"Content generation failed for {platform}: {str(e)}")
        logging.info(f"Using fallback content for {platform}")
        return generate_fallback_content(platform)