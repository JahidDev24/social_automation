import time
import schedule
from datetime import datetime
from content_generator import generate_content
from media_creator import create_image, create_video
from platform_manager import get_platform_client, post_to_platform
from scheduler import schedule_daily_post
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/automation.log'),
        logging.StreamHandler()
    ]
)

def run_single_test(platforms=['instagram']):
    """Run a single test cycle for content generation and media creation."""
    logging.info("Starting single test cycle")
    for platform in platforms:
        try:
            logging.info(f"Testing platform: {platform}")
            # client = get_platform_client(platform)
            # if not client:
            #     logging.error(f"No client for {platform}. Check config.json.")
            #     continue
            
            # Generate content
            content = generate_content(platform)
            logging.info(f"Generated content for {platform}: {content[:50]}...")

            # Create media
            post_path = create_image(content, f"output/images/post_image_{platform}.jpg")
            video_path = create_video(content, f"output/videos/reel_video_{platform}.mp4")
            
            if post_path and os.path.exists(post_path):
                logging.info(f"Image created at: {post_path}")
            else:
                logging.error(f"Image creation failed for {platform}")
            
            if video_path and os.path.exists(video_path):
                logging.info(f"Video created at: {video_path}")
            else:
                logging.error(f"Video creation failed for {platform}")
            
            # Post content (skipped in test mode)
            post_to_platform(platform, client, post_path, video_path, "Test Post! #TechNews")
        
        except Exception as e:
            logging.error(f"Test cycle failed for {platform}: {str(e)}")
    logging.info("Test cycle completed")

def main():
    """Main function for scheduling posts."""
    def job():
        for platform in ['instagram']:  # Add future platforms here
            try:
                client = get_platform_client(platform)
                if client:
                    content = generate_content(platform)
                    post_path = create_image(content, f"output/images/post_image_{platform}.jpg")
                    video_path = create_video(content, f"output/videos/reel_video_{platform}.mp4")
                    post_to_platform(platform, client, post_path, video_path, "Daily Tech Update! #TechNews #Innovation")
            except Exception as e:
                logging.error(f"Scheduled job failed for {platform}: {str(e)}")

    schedule_daily_post(job)
    
    logging.info("Starting scheduler")
    while True:
        schedule.run_pending()
        time.sleep(60)
        if datetime.now().hour == 0 and datetime.now().minute == 0:
            schedule.clear()
            schedule_daily_post(job)
            time.sleep(3600)

if __name__ == "__main__":
    logging.info("Script started")
    run_single_test()
    # Uncomment to enable scheduling
    # main()