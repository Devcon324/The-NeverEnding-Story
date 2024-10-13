import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from src.tools import startStory, writeNextStory
from src.update import commitToGithub

load_dotenv()

PATH_TO_README = "./README.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

if __name__ == '__main__':
  """
  Start the story by writing the first story chunk to the README file.
  Once the stroy has started a flag is created to prevent starting the story again.
  Then write the next story chunk to the README file.
  """
  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  if not os.path.exists("story_started.flag"):
      startStory(client, PATH_TO_README)
      with open("story_started.flag", "w") as f:
          f.write("Story started on: " + date)
  else:
    writeNextStory(client, PATH_TO_README)

  # Commit the changes to the README file to the GitHub repository.
  # sudo crontab -e
  # 59 23 * * * cd /mnt/d/GitHub/The-NeverEnding-Story ; /usr/bin/env /usr/bin/python3 /mnt/d/GitHub/The-NeverEnding-Story/main.py
  commitToGithub(PATH_TO_README, date)
