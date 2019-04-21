import time


class Scheduler:
    def add_interval_job(self, job, interval):
        job_output = job()
        time.sleep(interval)
        return job_output
