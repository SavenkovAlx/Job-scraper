from flask import Flask, render_template, request, redirect, send_file
from djinni import get_jobs as dj_get_jobs
from so import get_jobs as so_get_jobs
from exporter import save_to_csv

app = Flask('JobParser')

db = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report')
def report():
    keyword = request.args.get('keyword')
    if keyword is not None:
        keyword = keyword.lower()
        getDb = db.get(keyword)
        if getDb:
            jobs = getDb
        else:
            jobs = dj_get_jobs(keyword) + so_get_jobs(keyword)
            db[keyword] = jobs
    else:
        return redirect('/')
    return render_template('report.html', searchBy=keyword, resultsNumber=len(jobs), jobs=jobs)


@app.route('/export')
def export():
    try:
        keyword = request.args.get('keyword')
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_csv(jobs)
        return send_file('jobs.csv')
    except:
        return redirect('/')


app.run()
