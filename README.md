# Zabbix-Notification-Telegram-Topic

Main Uses
-
* **Monitoring Notifications**: Used to send automatic notifications via Telegram when issues or anomalies are detected in systems monitored by Zabbix.
* **Quick Visualization**: Provides a quick way to view relevant charts directly in Telegram, facilitating rapid responses from IT teams.
* **Automation**: Can be integrated into automated workflows to improve incident management.

This script is useful for technical support teams that want to stay informed about the status of their systems and respond quickly to issues.

**Send Notification in Telegram "Message Thread ID" (Topic), if trigger or item set tag with value `MessageThreadId: chat_id`. Ex: _MessageThreadId: 2_**

Zabbix Settings Media Types
-
Create new media types
1. **Name**: Telegram_Topic
2. **Type**: Scrypt
3. **Script name**: zbxTT.py (_name file that is used_)
4. **Script parameters**: ("here you can indicate direct values ​​or global macros, you already choose as you wish")
   1. `{$ZABBIX.URL}` - use global macros or your_values
   2. `{$ZABBIX.UI.USER}` - use global macros or your_values
   3. `{$ZABBIX.UI.PASS}` - use global macros or your_values
   4. `{$ZABBIX_TELEGRAM_TOKEN}` - use global macros or your_values
   5. `{ALERT.SENDTO}` - zabbix macros are used, do not modify (recommended)
   6. `{ALERT.SUBJECT}` - zabbix macros are used, do not modify (recommended)
   7. `{ALERT.MESSAGE}` - zabbix macros are used, do not modify (recommended)
   8. `{EVENT.TAGS}` - zabbix macros are used, do not modify (recommended)
   9. `{ITEM.ID}` - zabbix macros are used, do not modify (recommended)
   10. set the default value "**1**" or any value that all messages that do not have the tag: `**MessageThreadId**`, will be sent in the topic with the indicated cheat ID. (Ex: `-100123456789_1`, set the value after the _ character)
![image](https://github.com/user-attachments/assets/3bd80a80-a5d2-4796-9a51-308f10432d2c)
5. Alerts -> Media types -> Message templates (you can create your own template and/or customize it with parameters from zabbix) view detail: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media 

