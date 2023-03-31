import numpy as np

simple_exponential_queue(arrival_rate, service_rate, num_arrivals):
    arrival_intervals = np.random.exponential(1/arrival_rate, num_arrivals)
    service_intervals = np.random.exponential(1/service_rate, num_arrivals)

    arrival_times, service_times = np.cumsum(arrival_intervals), np.cumsum(service_intervals)
    
    return arrival_times, service_times
