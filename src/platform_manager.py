import json
import logging
from instagram_poster import login as instagram_login, post_content as instagram_post

logging.basicConfig(filename='logs/automation.log', level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
       with open('config/config.json', 'r') as f:
           return json.load(f)

def get_platform_client(platform):
       config = load_config()['platforms']
       if platform == "instagram" and config['instagram']['enabled']:
           return instagram_login()
       # Add future platforms here (e.g., snapchat_login, linkedin_login)
       return None

def post_to_platform(platform, client, post_path, video_path, caption):
       if platform == "instagram":
           instagram_post(client, post_path, video_path, caption)
       # Add future platforms here (e.g., snapchat_post, linkedin_post)