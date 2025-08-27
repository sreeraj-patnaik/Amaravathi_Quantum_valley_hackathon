from django.db.models import Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone
from datetime import timedelta
from .models import Backend, Job
from django.shortcuts import render

def dashboard(request):
    backends = Backend.objects.all()
    metrics = []
    now = timezone.now()
    for backend in backends:
        all_jobs = Job.objects.filter(backend=backend)

        # Queue depth = number of jobs in 'queued' or 'running' state right now
        queue_depth = all_jobs.filter(status__in=['queued', 'running']).count()

        # Throughput = jobs completed per hour (last hour)
        one_hour_ago = now - timedelta(hours=1)
        throughput = all_jobs.filter(status='success', completed_at__gte=one_hour_ago).count()

        # Average execution time (for all completed jobs)
        avg_exec_time = all_jobs.filter(status='success', completed_at__isnull=False).aggregate(
            avg_time=Avg(ExpressionWrapper(F('completed_at') - F('submitted_at'), output_field=DurationField()))
        )['avg_time']
        avg_exec_time_secs = avg_exec_time.total_seconds() if avg_exec_time else 0

        # Utilization = sum of execution times / (total possible time window * number of qubits)
        # For simplicity, use last 24h as window
        window_start = now - timedelta(hours=24)
        jobs_last_24h = all_jobs.filter(submitted_at__gte=window_start, completed_at__isnull=False)
        total_exec_time = sum([(job.completed_at - job.submitted_at).total_seconds() for job in jobs_last_24h])
        utilization = total_exec_time / (24*3600*backend.qubit_count) if backend.qubit_count else 0

        metrics.append({
            'backend': backend,
            'queue_depth': queue_depth,
            'throughput': throughput,
            'avg_exec_time_secs': avg_exec_time_secs,
            'utilization': utilization,
        })

    user_jobs = Job.objects.filter(user_id=request.user.username)
    all_jobs = Job.objects.all()

    # Jobs grouped by backend for per-backend pie charts
    jobs_by_backend = {}
    for backend in backends:
        jobs_by_backend[backend.name] = Job.objects.filter(backend=backend)

    return render(request, 'dashboard.html', {
        'backends': backends,
        'metrics': metrics,
        'user_jobs': user_jobs,
        'jobs': all_jobs,
        'jobs_by_backend': jobs_by_backend,
    })