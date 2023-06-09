import datetime
from sql_db import SqlRequests
from db_conn import BotConnection


database = SqlRequests()
bot = BotConnection().bot


class Reminds:

    def remind_dates(self):
        users = database.get_all_users()  # получаю список всех user_id <и кол-во дней, за которое юзер получает уведомления
        for user_id in users:
            dates_to_remind = database.get_remind_date(user_id)  # для каждого пользователя получаю список
            if len(dates_to_remind) > 0:
                bot.send_message(user_id, 'Reminding about your upcoming dates:')
                for date in dates_to_remind:
                    bot.send_message(user_id, f'In {int(date[3])} days comes "{date[0]}" date, which starts on {date[1]}')
            # else:
            #     bot.send_message(user, "Don't have any new dates comes in {user[1]}")
        print(f'\n{str(datetime.datetime.now())}: Выполнена ежедневная джоба по отправке уведомлений')

    def remind_hours(self):
        users = database.get_all_users()
        for user_id in users:
            hours_to_remind = database.get_remind_hours(user_id)
            if len(hours_to_remind) > 0:
                bot.send_message(user_id, f'Upcoming events in next 3 hours:')
                for event in hours_to_remind:
                    bot.send_message(user_id, f'Soon comes "{event[0]}" event, \nwhich starts in {event[1]}'
                                              f'\nuntil event: {int(event[3])} hours and {int(event[4])} minutes')
            # else:
        print(f'\n{str(datetime.datetime.now())}: Выполнена ежечасная джоба по отправке уведомлений')