import os
from telegram.ext import Updater, PicklePersistence

import logging

persistence = PicklePersistence(filename='data')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(os.getenv('BOT_TOKEN'), persistence=persistence, use_context=True)
