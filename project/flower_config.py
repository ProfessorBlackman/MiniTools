logging = 'INFO'

# view address
# address = '0.0.0.0'
# Run the http server on a given port
# broker_url = 'redis://:password@localhost:6379/0'
broker_url = "redis://localhost:6379"
port = 5672

basic_auth = ["MT:minitools1"]

# Refresh dashboards automatically
auto_refresh = True

# Enable support of X-Real-Ip and X-Scheme headers
xheaders = True

# Time (in seconds) after which offline workers are automatically removed from the Workers view.
purge_offline_workers = 300

# A database file to use if persistent mode is enabled
# db = '/var/flower/db/flower.db'

# Enable persistent mode. If the persistent mode is enabled Flower saves the current state and reloads on restart
persistent = True

# commands to run flower in docker. docker build -t "flower" . $ docker run -d -p=49555:5555 --rm --name flower -e
# CELERY_BROKER_URL=redis://0.0.0.0:6379/0 flower flower --port=5555.

# command to run flower in terminal
# celery -A ImageMatchingPlatformBackend flower --conf=flowerconfig.py
