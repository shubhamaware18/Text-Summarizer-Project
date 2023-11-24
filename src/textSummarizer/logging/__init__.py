import os
import sys
import logging

# Define the logging format string
logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

# Set up the directory for logs and the log file path
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    # Set up logging handlers for both a file and the console
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger with the specified name
logger = logging.getLogger('textSummarizerLogger')
