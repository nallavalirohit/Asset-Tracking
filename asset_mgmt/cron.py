from django_cron import Job,cronScheduler
import django_cron.base
#class MyCronJob(CronJobBase):
#    RUN_EVERY_MINS = 2 # every 2 hours
#
#    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
##    code = 'my_app.my_cron_job'    # a unique code
#
#    def do(self):
#        print "===================="    # do your thing here
class Check(Job):

#    run_every = 60 # run every day

    def job(self):
        print "99999"

cronScheduler.register(Check)

class Check1(Job):

     # run every day

    def job(self):
        print "99999"

cronScheduler.register(Check1)