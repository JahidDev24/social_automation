import schedule
import random
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='logs/automation.log', level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')

def schedule_daily_post(job):
       hour = random.randint(8, 22)
       minute = random.randint(0, 59)
       post_time = f"{hour:02d}:{minute:02d}"
       schedule.every().day.at(post_time).do(job)
       logging.info(f"Scheduled post for {post_time}")