from django.db import models

class Backend(models.Model):
    name = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=32)  # hardware/simulator
    qubit_count = models.IntegerField()
    operational = models.BooleanField(default=True)

class Job(models.Model):
    backend = models.ForeignKey(Backend, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=128, unique=True)
    user_id = models.CharField(max_length=128, default="User")  # or ForeignKey to your user model
    submitted_at = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32)  # success/failed/running/queued

    @property
    def execution_time(self):
        if self.completed_at and self.submitted_at:
            return (self.completed_at - self.submitted_at).total_seconds()
        return None