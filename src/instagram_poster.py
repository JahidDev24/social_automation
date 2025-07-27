import instagrapi
import json
import os
import logging

logging.basicConfig(filename='logs/automation.log', level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
       with open('config/config.json', 'r') as f:
           return json.load(f)

def login():
       config = load_config()['platforms']['instagram']
       cl = instagrapi.Client()
       cl.delay_range = [1, 5]
       try:
           cl.login(config['username'], config['password'])
           logging.info("Successfully logged into Instagram")
           return cl
       except Exception as e:
           logging.error(f"Instagram login failed: {e}")
           raise

def post_content(cl, post_path, video_path, caption="Daily Tech Update! #TechNews #Innovation"):
       config = load_config()
       if config['test_mode']:
           logging.info("Test mode: Skipping Instagram upload")
           logging.info(f"Generated content saved: {post_path}, {video_path}")
           return
       
       try:
           if post_path and os.path.exists(post_path):
               cl.photo_upload(post_path, caption=caption)
               logging.info("Instagram post uploaded")
               os.remove(post_path)
           
           if video_path and os.path.exists(video_path):
               cl.video_upload(video_path, caption=caption.replace("Update", "Reel"))
               logging.info("Instagram reel uploaded")
               os.remove(video_path)
       except Exception as e:
           logging.error(f"Instagram upload failed: {e}")