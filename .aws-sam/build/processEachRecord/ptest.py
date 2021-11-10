import datetime

sf_name = f"StudyMgmt{datetime.datetime.now()}".replace(' ','').replace('-','').replace(':','').replace('.','')
print(sf_name)