from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import TextClip, ColorClip
import os
import logging

logging.basicConfig(filename='logs/automation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_image(content, output_path="output/images/post_image.jpg"):
    try:
        img = Image.new('RGB', (1080, 1080), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        try:
                font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 40)
        except:
              font = ImageFont.load_default()
           
        lines = content.split('\n')
        y_text = 100
        for line in lines:
           draw.text((50, y_text), line, font=font, fill=(0, 0, 0))
           y_text += 50
           os.makedirs(os.path.dirname(output_path), exist_ok=True)
           img.save(output_path)
           logging.info(f"Image created: {output_path}")
           return output_path
    except Exception as e:
       logging.error(f"Image creation failed: {e}")
       return None

def create_video(content, output_path="output/videos/reel_video.mp4"):
       try:
           txt_clip = TextClip(content, fontsize=40, color='white', size=(1080, 1920), bg_color='black')
           duration = min(len(content) // 20, 15)
           txt_clip = txt_clip.set_duration(duration)
           
           os.makedirs(os.path.dirname(output_path), exist_ok=True)
           txt_clip.write_videofile(output_path, fps=24)
           logging.info(f"Video created: {output_path}")
           return output_path
       except Exception as e:
           logging.error(f"Video creation failed: {e}")
           return None