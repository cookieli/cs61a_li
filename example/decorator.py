def printbug(func):
    def __decorator(user):
        print('enter the login')
        func(user)
        print('exit the login')
    return __decorator

@printbug
def login(user):
    print('in login' + user)

def printdebug_level(level): #add wrapper to receive decorator's parameter
    def printbug(func):
        def __decorator(user):
            print('enter the login, and debug level is:' + str(level)) #print debug level
            func(user)
            print('exit the login')
        return __decorator
    return printbug    #return origin decorator


@printdebug_level(level=5)    #decorator parameter, debug level set to 5
def login(user):
    print('in login:' + user)

def printbug(func):
    def __decorator(user):
        print('enter the login')
        result = func(user)
        print('exit the login')
        return result
    return __decorator
@printbug
def login(user):
    print('in login' + user)
    if user == "jatsz":
        msg = "success"
    else:
        msg = "fail"
    return msg

def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator

def others(func):
    def __decorator():
        print('***other decorator***')
        func()
    return __decorator

@others
@printdebug
def login():
    print('in login:')

@printdebug
@others
def logout():
    print('in logout:')