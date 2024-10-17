# Zabbix-Notification-Telegram-Topic

This Python script is a Telegram notifier designed to send messages to a specified chat using the Telegram Bot API. It takes command-line arguments for the chat ID, message subject, message content, and optional event tags. The script handles Markdown formatting and allows for threading of messages by including a message thread ID. If an error occurs during message sending, it raises an exception with a relevant error message.
This code snippet processes event tags for the Telegram notifier script. Here's a breakdown of its principles:
1. **Initialization**: An empty dictionary `tags` is created to store parsed key-value pairs.
2. **Stripping Input**: It checks if `event_tags` is not empty (after stripping whitespace).
3. **Splitting Tags**: The input string is split by commas to handle multiple tags.
4. **Key-Value Parsing**: Each tag is split by a colon (`:`) into a key and value:
   * It ensures that there are exactly two parts (a key and a value).
   * Both the key and value are stripped of surrounding whitespace.
5. **Filtering by Key**: It specifically looks for keys that start with `'MessageThreadId'`:
   * If found, it appends the value to a list in the `tags` dictionary, creating a new entry if necessary.
This approach allows the script to gather relevant message thread IDs, which can be used to send messages in a specific thread in Telegram.

Zabbix Settings Media Types
-
Create new media types
1. **Name**: Telegram_Topic
2. **Type**: Scrypt
3. **Script name**: zbxTT.py
4. **Script parameters**:
   1. {ALERT.SENDTO}
   2. {ALERT.SUBJECT}
   3. {ALERT.MESSAGE}
   4. {EVENT.TAGS}
   5. {ITEM.ID}
