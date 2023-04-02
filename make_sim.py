import numpy as np

def simple_exponential_queue(arrival_rate, service_rate, num_events_upper_bound = 10000):
    events = np.cumsum(np.random.exponential(1/(arrival_rate + service_rate), num_events_upper_bound))
    probabilities = np.array([service_rate,arrival_rate])
    probabilities /= np.sum(probabilities)
    deltas = np.random.choice([-1,1],p=probabilities,replace=True,size=num_events_upper_bound)

    n = 0
    for i,delta in enumerate(deltas):
        if n + delta < 0:
            deltas[i] = 0
        else:
            n = n + delta

    valid_events = (deltas != 0)

    return events[valid_events],deltas[valid_events]

def utilisation_rate(events, deltas):
    return sum(np.diff(events) * (np.cumsum(deltas)[:-1] > 0)) / events[-1]

def mean_waiting_time(events, deltas):
    arrivals = events[deltas>0]
    departures = events[deltas<0]
    ad = zip(arrivals,departures)
    w = np.array([t[1]-t[0] for t in ad])
    return np.mean(w)

def mean_queue_len(events, deltas):
    return sum(np.diff(events) * np.cumsum(deltas)[:-1]) / events[-1]
