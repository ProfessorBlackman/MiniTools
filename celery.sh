poetry run celery -A project worker -l INFO -n worker1@%n -c 2 -f logs/worker1.log