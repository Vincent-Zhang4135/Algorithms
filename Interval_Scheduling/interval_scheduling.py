################################
#
# The Interval Scheduling Problem goes as follows: 
# Suppose we have a list of jobs, each with a start time and an end time. 
# More formally, like J, the list of jobs, = the following:
# {(s_i, f_i) | 1 <= i <= n}, where each pair, (s_i, f_i), represents the start
# and finish time respectively. The goal is that no interval can overlap with another
# just like how we cannot be working the same jobs at once. 
# 
# How can we go about solving the problem like this? It turns out that a greedy approach
# is sufficient, and the greedy solution up to k will always be at least as good as the 
# optimal solution.
#
################################
from operator import itemgetter
import examples

# for each job J, index 0 is the ID, index 1 is the start time, index 2 is the finish time
def interval_scheduling(J):
    most_jobs = []
    J = (sorted(J, key=itemgetter(2)))
    last_finish = 0
    for i, job in enumerate(J):
        # if the job start time is after the last job finish
        # we are greedily choosing jobs based on how early they finish
        if job[1] >= last_finish:
            most_jobs.append(job)
            # set the last_finish to the current job's finish
            last_finish = job[2]
            
    return [len(most_jobs), most_jobs]
            
    

if __name__ == '__main__':
    print(interval_scheduling(examples.J1))
    print(interval_scheduling(examples.J2))