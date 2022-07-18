def getDate():
    import datetime
    presentdate=datetime.datetime.now
    return str(presentdate().date())

def getTime():
    import datetime
    presenttime=datetime.datetime.now
    return str(presenttime().time())
