from ...jobs import models


def resolve_job_by_name(name):
    return models.Job.objects.filter(name=name).first()

def resolve_jobs():
    return models.Job.objects.all()
