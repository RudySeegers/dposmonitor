import psycopg2
import time
from config import CONFIG
from slacker import Slacker


slack = Slacker('{}'.format(CONFIG['token']))

def get_missed_blocks():
    conn = psycopg2.connect(
        host='localhost',
        database='{}'.format(CONFIG['database']),
        user='user'.format(CONFIG['user']),
        password=None)

    cursor = conn.cursor()

    cursor.execute("""
              SELECT mem_accounts."missedblocks"
              FROM mem_accounts
              WHERE username = '{}'""".format(CONFIG['delegate']))

    watermark_missedblocks = cursor.fetchone()
    return watermark_missedblocks[0]

def monitor():
    old_missed_blocks = get_missed_blocks()

    while True:
        time.sleep(10)
        new_missed_blocks = get_missed_blocks()

        if new_missed_blocks == old_missed_blocks:
            message = "Human, {} missed a block, please respond".format(CONFIG['delegate'])
            slack.chat.post_message('{}'.format(CONFIG['slackchannel']), message)

        old_missed_blocks = new_missed_blocks
