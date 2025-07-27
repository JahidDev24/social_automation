# Social Media Automation Project

Automates daily Instagram posts/reels with tech content using Grok (xAI API). Designed for future expansion to Snapchat, LinkedIn, Facebook, etc.

## Setup
1. Install dependencies: `pip3 install -r requirements.txt`
2. Install ffmpeg: `brew install ffmpeg`
3. Copy a .ttf font to `assets/fonts/`
4. Update `config/config.json` with Instagram and xAI API credentials
5. Run: `python3 src/main.py`

## Testing
- Set `"test_mode": true` in `config.json` to save content locally
- Check `output/images/` and `output/videos/` for generated files
- Logs: `logs/automation.log`
- Run tests: `python3 tests/test_content.py`

## Future Upgrades
- Add platform modules in `src/platforms/`
- Update `platform_manager.py` and `config.json` for new platforms

## Notes
- Use a test Instagram account
- Get xAI API key from https://x.ai/api