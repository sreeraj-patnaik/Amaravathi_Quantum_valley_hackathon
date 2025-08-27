from django.core.management.base import BaseCommand
from index.models import Backend, Job
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the DB with rich sample quantum data'

    def handle(self, *args, **kwargs):
        Backend.objects.all().delete()
        Job.objects.all().delete()
        b1 = Backend.objects.create(name='ibmq_5036', device_type='Hardware', qubit_count=12, operational=True)
        b2 = Backend.objects.create(name='ibmq_5011A', device_type='Simulator', qubit_count=7, operational=True)
        now = timezone.now()
        # Jobs for all users, both completed and in-queue
        Job.objects.create(backend=b1, job_id='J001', user_id='alice', status='success',
                           submitted_at=now - timedelta(hours=2), completed_at=now - timedelta(hours=1, minutes=50))
        Job.objects.create(backend=b1, job_id='J002', user_id='bob', status='queued',
                           submitted_at=now - timedelta(minutes=5), completed_at=None)
        Job.objects.create(backend=b1, job_id='J003', user_id='carol', status='success',
                           submitted_at=now - timedelta(hours=1, minutes=50), completed_at=now - timedelta(hours=1, minutes=40))
        Job.objects.create(backend=b1, job_id='J004', user_id='dave', status='failed',
                           submitted_at=now - timedelta(hours=1, minutes=30), completed_at=now - timedelta(hours=1, minutes=25))
        Job.objects.create(backend=b2, job_id='J005', user_id='erin', status='success',
                           submitted_at=now - timedelta(minutes=40), completed_at=now - timedelta(minutes=30))
        Job.objects.create(backend=b2, job_id='J006', user_id='alice', status='running',
                           submitted_at=now - timedelta(minutes=16), completed_at=None)
        Job.objects.create(backend=b2, job_id='J007', user_id='bob', status='queued',
                           submitted_at=now - timedelta(minutes=10), completed_at=None)
        self.stdout.write(self.style.SUCCESS("Rich sample data loaded"))