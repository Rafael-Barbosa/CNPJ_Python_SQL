from crontab import CronTab

cron = CronTab(user='username') # Coloque seu usuário
job = cron.new(command='python main.py -d')

# comando no contrab 0 3 20 * *
job.every(3).hours()
job.every(20).day()

cron.write()
