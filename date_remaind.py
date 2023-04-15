from func_for_scheduler import remind_dates, remind_hours
import schedule
from multiprocessing import *


def start_process():  # Запуск Process
    Process(target=ScheduleInfinite.start_schedule, args=()).start()


class ScheduleInfinite:

    def start_schedule():
        schedule.every(1).day.at('00:00').do(remind_dates)
        schedule.every(1).hour.at(':00').do(remind_hours)

        print(schedule.get_jobs())

        while True:
            schedule.run_pending()
