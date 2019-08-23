# Rate limiting: 
# given a list of users, their limits, see if the user can continue with that request.

# Sliding log
# keep a queue of requests and users. on every request, remove the elements that are not within the last hour and update the users' current limit
# users' limits are kept in a dictionary
# alternatively keep requests of users in separate queues, remove the elements that are not within the last hour
## one optimization is to only update the current request count when we hit the limit.
### another optimization is to use a index on the queue to search the time with extra O(n) space
### OR, use the fast pointer algorithm: http://www.ijcsit.com/docs/Volume%205/vol5issue02/ijcsit20140502215.pdf OR skip list??
### once the hour limit is found, drop all the elements before it.

# what's the complexity for each transaction:
# brute force: checks each entry in the queue

# tracking this in a db will introduce a huge response delay 
# so it makes sense to aim towards an in-memory centric application with scheduled backups for redundancy

# we are losing cache locality with using a queue and a dictionary.
# we should consider implementing an extension module hash table and std::vector
# metrics of user behavior:
# does the limit ever change, if not
# how often does the number of users change.

# how to introduce a new user
# make some back of the envolope calculations assuming the profile of the requests.

# what the memory footprint will look like:
# for 1M users with 10K max limits: around ~80GB. sounds reasonable but how could we distribute the load:

## remember CAP theorem: 
## consistency: will all executions of reads and writes seen by all nodes be atomic or linearizably consistent.
## availability: will a request made to the data store always eventually complete. a system is available iff all messages have a valid response but allows unbounded amount of delay.
## partition tolerence: network is allowed to drop any messages. 
### partiton ex: if the system is dependent on a single component and it fails, messages between some components will be lost/dropped.

## CAP gaurantees that there is some circumstance(let's call it critical condition) in which a system must give up C or A. 
## It doesn't say how likely the critical condition is. A single inconsistent read or unavailable write means that we reached it
## Until critical condition system can be available and consistent.

## You cannot build or choose partition tolerence.
## if your system may experience partitions, you cannot always be C and A

## YOU CANNOT CA!! you can only cp or ap

## but whai??
##

# consistency, availability, partition tolerence where we can only choose 2 out of the 3.

# we have to choose between consistency and availability.
# let's make case for both.
# provide partition tolerence by replicating the backup database.
# AP: availability & partition tolerence
# 

# hw/vm elasticity / performance metrics? (auto instance invocation upon increased load)

# imagine wrapping this as a middleware.
# if you want to globally limit the rates, simply introduce a single user. for group limiting, add groups as users

# how to deploy this middleware?
# migrate databases
# how critical is this functionality? if it is important, we are surely replacing a service.
# start with a single application server instance, monitor and make sure the behavior is matching the expected calculations slowly let it in.

# can be extended to specify time frames for every limit but this version excludes them for brevity.
# reconsider load distribution if time frames and max rates change.

from collections import deque

class RateLimiter(object):
    def __init__(self, ul_dict):
        # create a dictionary of users, their max limits, current limits and their requests in the last hour
        self.u_q = {u: (l, 0, deque()) for (u, l) in ul_dict.items()} 

    def isAllowed(self, user):
        """
        """



def test():
    pass

if __name__ == "__main__":
    test()


