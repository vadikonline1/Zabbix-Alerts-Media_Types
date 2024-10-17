#!/usr/bin/env python3
#python3 /usr/lib/zabbix/alertscripts/zbxTT.py "YOUR_CHAT_ID" "subject" "message"

import requests
import sys

class TelegramNotifier:
    def __init__(self, token, chat_id, parse_mode='markdownv2'):
        self.token = token
        self.chat_id = chat_id
        self.parse_mode = parse_mode
        self.message = ""

    def escape_markup(self, text):
        if self.parse_mode == 'markdownv2':
            return (text.replace('_', '\\_')
                        .replace('*', '\\*')
                        .replace('[', '\\[')
                        .replace(']', '\\]')
                        .replace('(', '\\(')
                        .replace(')', '\\)')
                        .replace('~', '\\~')
                        .replace('`', '\\`')
                        .replace('>', '\\>')
                        .replace('#', '\\#')
                        .replace('+', '\\+')
                        .replace('-', '\\-')
                        .replace('=', '\\=')
                        .replace('|', '\\|')
                        .replace('{', '\\{')
                        .replace('}', '\\}')
                        .replace('.', '\\.')
                        .replace('!', '\\!'))
        return text

    def send_message(self, message_thread_id=None):
        params = {
            'chat_id': self.chat_id,
            'text': self.message,
            'disable_web_page_preview': True,
            'disable_notification': False
        }
        if message_thread_id:
            params['message_thread_id'] = message_thread_id
        if self.parse_mode:
            params['parse_mode'] = self.parse_mode

        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        response = requests.post(url, json=params)
        if response.status_code != 200:
            raise Exception(f"Error sending message: {response.text}")

def main():
    try:
        token = 'YOUR_BOT_TOKEN'
        chat_id = sys.argv[1] if len(sys.argv) > 1 else '{ALERT.SENDTO}'
        subject = sys.argv[2] if len(sys.argv) > 2 else '{ALERT.SUBJECT}'
        message = sys.argv[3] if len(sys.argv) > 3 else '{ALERT.MESSAGE}'
        event_tags = sys.argv[4] if len(sys.argv) > 4 else ''

        tags = {}
        if event_tags.strip():
            for tag in event_tags.split(','):
                key_value = tag.split(':')
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip()
                    if key.startswith('MessageThreadId'):
                        tags.setdefault(key, []).append(value)

        notifier = TelegramNotifier(token, chat_id)
        notifier.message = f"{subject}\n{message}"
        message_thread_ids = [val for key in tags for val in tags[key]]
        notifier.message = notifier.escape_markup(notifier.message)

        for thread_id in message_thread_ids:
            if thread_id:
                notifier.send_message(message_thread_id=thread_id)

        return 'OK'
    except Exception as error:
        raise Exception(f'Sending failed: {error}')

if __name__ == "__main__":
    print(main())
