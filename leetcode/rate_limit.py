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

## remember CAP theorem: "a quick reCAP haha"
## consistency: will all executions of reads and writes seen by all nodes be atomic or linearizably consistent.
## availability: will a request made to the data store always eventually complete. a system is available iff all messages have a valid response but allows unbounded amount of delay.
## partition tolerence: network(internal messaging between distributed data) is allowed to drop any messages. 
### partiton ex: if the system is dependent on a single component and it fails, messages between some components will be lost/dropped.

## CAP gaurantees that there is some circumstance(let's call it critical condition) in which a system must give up C or A. 
## It doesn't say how likely the critical condition is. A single inconsistent read or unavailable write means that we reached it
## Until critical condition system can be available and consistent.

## You cannot build or choose partition tolerence.
## if your system may experience partitions, you cannot always be C and A
## YOU CANNOT CHOOSE IF YOUR SYSTEM WILL HAVE PARTITIONS. EITHER IT WILL OR IT WONT depending on the topology and dependence.
## If you have a single application with a single dtabase, you can say you have partition tolerence but then it wouldn't be a distributed system eh
## hence YOU CANNOT CA in distributed systems!! only cp or ap

# we have to choose between consistency and availability.
# replicate data so that we have high availability, we now have the problem of synchronization.
# put some cache in front of it.
# put some smart routing depending on your users.
# keep a hot cache of more active users etcetc

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
import threading
import time

class RateLimiter(object):
    def __init__(self, ul_dict, time_window_seconds):
        """
        @desc constr
        @param ul_dict hashmap of unique user ids to their limits
        """
        # create a dictionary of users, their max limits, request queue and a lock for that request queue
        self.u_q = {u: (l, deque(), threading.Lock()) for (u, l) in ul_dict.items()} 
        self.time_window_seconds = time_window_seconds
        self.lock = threading.Lock() # make it a thread safe service
    
    def addUser(user_id, user_limit):
        with self.lock:
            self.u_q.update({user_id: (user_limit, 0, deque(), threading.Lock())})

    def removeUser(self, user_id):
        with self.lock:
            del self.u_q[user_id]

    def isAllowed(self, user_id, *args):
        """
        @desc check if user is allowed to make a request.
                evict on every request
        @param user_id
        @param args list of test argiments. currently used for specifying the arrival of a request
        """
        user_data = self.u_q[user_id]
        with user_data[2]:
            req_queue = user_data[1]
            current_time = args[0] if args else time.time()
            RateLimiter.evict(req_queue, self.time_window_seconds, current_time)

            limit = user_data[0]
            if len(req_queue) >= limit:
                raise RateLimiter.ApiRateLimitReachedException("user: {user_id}, exceeded limit: {limit}".format(user_id=user_id, limit=limit))
            else:
                req_queue.append(current_time)
    
    @staticmethod
    def evict(req_queue, time_window_seconds, current_time):
        """
        @desc evict request entries from the queue if they are older than current_time - time_window
                test use first list argument
        """
        if req_queue: 
            # if the first entry in the queue is smaller then 
            if req_queue[0] <= current_time - time_window_seconds:
                while req_queue.popleft() <= current_time - time_window_seconds:
                    continue

    class ApiRateLimitReachedException(Exception):
        pass

def test():
    ul_dict = {"can": 5, "murat": 5}
    rl = RateLimiter(ul_dict, 10)
    def test_run(**args):
        try:
            rl.isAllowed(args["u_id"], args["time"])
        except RateLimiter.ApiRateLimitReachedException, e:
            print "thread {0} raised ex".format(args["time"])
            
    # can makes 1 request every second. since time_window is set to 10 seconds. 
    # He will not be allowed 5 requests but be allowed the last one.
    can_threads = [threading.Thread(target=test_run, kwargs={"u_id": "can", "time": i}) for i in range(11)]
    
    # murat makes 1 request every 2 second. Since his limit is 6 and time window is 10 seconds all of his requests will be allowed.
    murat_threads = [threading.Thread(target=test_run, kwargs={"u_id": "murat", "time": i*2}) for i in range(11)]
    
    for i in range(11):
        can_threads[i].start()
        murat_threads[i].start()


if __name__ == "__main__":
    test()


