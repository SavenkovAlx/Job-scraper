import csv


def save_to_csv(jobs):
    with open('jobs.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'company', 'location', 'link'])
        for job in jobs:
            writer.writerow([job['title'], job['company'],
                            job['location'], job['link']])
