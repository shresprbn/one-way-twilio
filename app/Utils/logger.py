import logging
import os

def setup_logger(log_folder,log_file_prefix, level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Get a list of existing log files
    existing_logs = [f for f in os.listdir(log_folder) if f.startswith(log_file_prefix) and f.endswith('.log')]
    
    # Find the highest numbered log file
    highest_number = max([int(f[len(log_file_prefix)+1:-4]) for f in existing_logs] or [0])
    
    # Create the new log file name
    log_file_number = highest_number + 1
    log_file = os.path.join(log_folder, f"{log_file_prefix}_{log_file_number}.log")

    # Create a file handler
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
