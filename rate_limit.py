# Implement a rate limiter that does not allow a user to make more that 100 requests per second.
# x times in per second

# is_user_allowed(user)

# function print_hello() { print "hello world" }

# is_user_allowed(fnc)

# client could be asked to stop
# or we can throttle the API within the function

# while(True) is_user_allowed(fnc)
# 1 second a hundred, 2 seconds 200 hundred
# x + t seconds x + 1 + t seconds should allow 100 calls

from collections import deque
import time

def test_is_user_allowed():
    q = deque([])    # timestamp, count
    # count = [0]
    
    def is_user_allowed(fnc):
            # time O(1)
        # space O(1)
        # while q length is smaller than 100
            # append to it
        # if q length is larger than 100
            # remove elements if their timestamp is smaller than time.now() - 1000
        time_now = time.time()

        if len(q) < 3:
            q.append(time_now)
            fnc()
            return True
        else:
            print q[0] < time_now - 1
            if q[0] < time_now - 1:
                q.popleft()
                q.append(time_now)
                fnc()
                return True
            else:
                return False #raise Exception("throttled")

    count = [1000]
    def my_fnc():
        print count[0]
        count[0] += 1

    # print "first test"
    # for i in range(16):
    #     try:
    #         is_user_allowed(my_fnc)
    #     except Exception:
    #         print "throttled: ", i
    
    print "second test"
    for i in range(16):
        if is_user_allowed(my_fnc):
            print "allowed: ", i
        else:
            print "not allowed: ", i
	
        time.sleep(0.2)



    

    # 200 requests within the time range 0,1
    # q = [0, 1 ... 100]
    # when the 101st element arrives
    # 101 102

    


def test():
    print "Hi, I am here. -Can"

    test_is_user_allowed()

    
    assert 1 == 1


if __name__ == "__main__":
    test()
