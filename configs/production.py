import multiprocessing

# Server Socket

# bind = ['0.0.0.0:8080']

# The maximum number of pending connections.
# backlog = 2048

# Worker Processes

# workers = multiprocessing.cpu_count() * 2 + 1

# Other options: eventlet, gevent, tornado, gthread
worker_class = 'sync'

# The maximum number of requests a worker will process before restarting.
# Disable automatic worker restarts by giving 0.
max_requests = 0


# Workers silent for more than this many seconds are killed and restarted.
timeout = 30

# workers still alive after the timeout.
graceful_timeout = 30
