import json,random,datetime,json,time,sys,radar,requests
n=int(sys.argv[1]) #no of times the data has to be printed
sleeptime=int(sys.argv[2])
f=[]
def datafunction():
    def d():

        return str(radar.random_datetime(start='2021-05-24T00:00:00', stop='2022-05-24T23:59:59'))
    k=d()
    # def datafunction():
    l={'Beaconid': random.randint(1,100),
            'date':k,
            'Temperaturedata':{'temperature':random.randint(-80,80)},
            'Batterydata':{'batterydata':{'voltage':random.randint(2500,3100)}}}

    contents = json.dumps(l,indent=3)
    content=json.loads(contents)
    f.append(content)
    
    return f



datafunction()


for i in range(0,n):
    # if i==n:
        print(datafunction())
        time.sleep(sleeptime) 



