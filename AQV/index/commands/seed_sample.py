from django.core.management.base import BaseCommand
from index.models import Backend, Job
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the DB with a rich, varied set of sample quantum data for all metrics'

    def handle(self, *args, **kwargs):
        Backend.objects.all().delete()
        Job.objects.all().delete()
        now = timezone.now()
        # Backends
        b1 = Backend.objects.create(name='ibmq_5036', device_type='Hardware', qubit_count=12, operational=True)
        b2 = Backend.objects.create(name='ibmq_5011A', device_type='Simulator', qubit_count=7, operational=True)
        b3 = Backend.objects.create(name='aqv_hybrid_7', device_type='Hybrid', qubit_count=20, operational=False)
        b4 = Backend.objects.create(name='noisy_sim_3', device_type='NoisySimulator', qubit_count=5, operational=True)

        # Jobs for ibmq_5036
        Job.objects.create(backend=b1, job_id='J001', user_id='alice', status='success',
                           submitted_at=now - timedelta(hours=3), completed_at=now - timedelta(hours=2, minutes=45))
        Job.objects.create(backend=b1, job_id='J002', user_id='bob', status='queued',
                           submitted_at=now - timedelta(minutes=15), completed_at=None)
        Job.objects.create(backend=b1, job_id='J003', user_id='carol', status='running',
                           submitted_at=now - timedelta(minutes=20), completed_at=None)
        Job.objects.create(backend=b1, job_id='J004', user_id='dave', status='failed',
                           submitted_at=now - timedelta(hours=5), completed_at=now - timedelta(hours=4, minutes=55))
        Job.objects.create(backend=b1, job_id='J005', user_id='erin', status='success',
                           submitted_at=now - timedelta(hours=1, minutes=50), completed_at=now - timedelta(hours=1, minutes=30))
        Job.objects.create(backend=b1, job_id='J006', user_id='frank', status='queued',
                           submitted_at=now - timedelta(minutes=7), completed_at=None)
        Job.objects.create(backend=b1, job_id='J007', user_id='grace', status='cancelled',
                           submitted_at=now - timedelta(hours=7), completed_at=now - timedelta(hours=6, minutes=55))
        Job.objects.create(backend=b1, job_id='J008', user_id='heidi', status='error',
                           submitted_at=now - timedelta(days=1), completed_at=now - timedelta(days=1, minutes=-2))
        Job.objects.create(backend=b1, job_id='J009', user_id='alice', status='success',
                           submitted_at=now - timedelta(minutes=70), completed_at=now - timedelta(minutes=55))
        Job.objects.create(backend=b1, job_id='J010', user_id='bob', status='running',
                           submitted_at=now - timedelta(minutes=5), completed_at=None)
        Job.objects.create(backend=b1, job_id='J011', user_id='carol', status='success',
                           submitted_at=now - timedelta(hours=13), completed_at=now - timedelta(hours=12, minutes=45))

        # Jobs for ibmq_5011A
        Job.objects.create(backend=b2, job_id='J101', user_id='alice', status='running',
                           submitted_at=now - timedelta(minutes=12), completed_at=None)
        Job.objects.create(backend=b2, job_id='J102', user_id='bob', status='queued',
                           submitted_at=now - timedelta(minutes=4), completed_at=None)
        Job.objects.create(backend=b2, job_id='J103', user_id='dave', status='success',
                           submitted_at=now - timedelta(hours=2), completed_at=now - timedelta(hours=1, minutes=55))
        Job.objects.create(backend=b2, job_id='J104', user_id='erin', status='failed',
                           submitted_at=now - timedelta(hours=7), completed_at=now - timedelta(hours=6, minutes=50))
        Job.objects.create(backend=b2, job_id='J105', user_id='frank', status='success',
                           submitted_at=now - timedelta(minutes=90), completed_at=now - timedelta(minutes=60))
        Job.objects.create(backend=b2, job_id='J106', user_id='grace', status='error',
                           submitted_at=now - timedelta(days=2), completed_at=now - timedelta(days=2, minutes=-3))
        Job.objects.create(backend=b2, job_id='J107', user_id='heidi', status='cancelled',
                           submitted_at=now - timedelta(days=1, hours=3), completed_at=now - timedelta(days=1, hours=2, minutes=50))
        Job.objects.create(backend=b2, job_id='J108', user_id='alice', status='queued',
                           submitted_at=now - timedelta(minutes=2), completed_at=None)

        # Jobs for aqv_hybrid_7
        Job.objects.create(backend=b3, job_id='J201', user_id='carol', status='queued',
                           submitted_at=now - timedelta(minutes=3), completed_at=None)
        Job.objects.create(backend=b3, job_id='J202', user_id='dave', status='running',
                           submitted_at=now - timedelta(minutes=30), completed_at=None)
        Job.objects.create(backend=b3, job_id='J203', user_id='erin', status='success',
                           submitted_at=now - timedelta(hours=5), completed_at=now - timedelta(hours=4, minutes=52))
        Job.objects.create(backend=b3, job_id='J204', user_id='frank', status='failed',
                           submitted_at=now - timedelta(hours=8), completed_at=now - timedelta(hours=7, minutes=55))
        Job.objects.create(backend=b3, job_id='J205', user_id='grace', status='success',
                           submitted_at=now - timedelta(hours=2, minutes=10), completed_at=now - timedelta(hours=2))
        Job.objects.create(backend=b3, job_id='J206', user_id='heidi', status='error',
                           submitted_at=now - timedelta(days=3), completed_at=now - timedelta(days=3, minutes=-1))
        Job.objects.create(backend=b3, job_id='J207', user_id='alice', status='cancelled',
                           submitted_at=now - timedelta(hours=15), completed_at=now - timedelta(hours=14, minutes=55))
        Job.objects.create(backend=b3, job_id='J208', user_id='bob', status='success',
                           submitted_at=now - timedelta(hours=6), completed_at=now - timedelta(hours=5, minutes=55))

        # Jobs for noisy_sim_3
        Job.objects.create(backend=b4, job_id='J301', user_id='alice', status='success',
                           submitted_at=now - timedelta(hours=3), completed_at=now - timedelta(hours=2, minutes=50))
        Job.objects.create(backend=b4, job_id='J302', user_id='bob', status='running',
                           submitted_at=now - timedelta(minutes=19), completed_at=None)
        Job.objects.create(backend=b4, job_id='J303', user_id='carol', status='queued',
                           submitted_at=now - timedelta(minutes=1), completed_at=None)
        Job.objects.create(backend=b4, job_id='J304', user_id='dave', status='failed',
                           submitted_at=now - timedelta(hours=9), completed_at=now - timedelta(hours=8, minutes=58))
        Job.objects.create(backend=b4, job_id='J305', user_id='erin', status='error',
                           submitted_at=now - timedelta(days=1, hours=5), completed_at=now - timedelta(days=1, hours=5, minutes=-2))
        Job.objects.create(backend=b4, job_id='J306', user_id='frank', status='success',
                           submitted_at=now - timedelta(minutes=55), completed_at=now - timedelta(minutes=51))
        Job.objects.create(backend=b4, job_id='J307', user_id='grace', status='queued',
                           submitted_at=now - timedelta(minutes=6), completed_at=None)
        Job.objects.create(backend=b4, job_id='J308', user_id='heidi', status='cancelled',
                           submitted_at=now - timedelta(hours=16), completed_at=now - timedelta(hours=15, minutes=55))

        self.stdout.write(self.style.SUCCESS("Rich and varied sample data loaded!"))