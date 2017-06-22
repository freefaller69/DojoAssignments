class Call(object):
    def __init__(self, id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.id = id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display_call(self):
        print "ID:",self.id
        print "Name:",self.caller_name
        print "Phone:",self.caller_phone_number
        print "Time:",self.time_of_call
        print "Reason:",self.reason_for_call
        print "-" * 20

class CallCenter(object):
    def __init__(self, calls = None):
        if calls == None:
            self.calls = []
        else:
            self.calls = calls
        self.queue_size = len(self.calls)

    def add(self, new_call):
        self.calls.append(new_call)

    def remove(self):
        pass

    def info(self):
        print self.queue_size


call1 = Call(11,"David", "206-555-1212", "09:22", "bill inquiry")
call2 = Call(12,"Jennifer", "425-555-1212", "13:04", "complaint")
call3 = Call(13,"Tanya", "360-555-1212", "19:51", "troubleshooting")

call1.display_call()
call2.display_call()
call3.display_call()
