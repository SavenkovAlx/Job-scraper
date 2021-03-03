from djinni import get_jobs as dj_get_jobs
from so import get_jobs as so_get_jobs
from save import save_to_csv

dj_jobs = dj_get_jobs()
so_jobs = so_get_jobs()


jobs = dj_jobs + so_jobs

save_to_csv(jobs)
