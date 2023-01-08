import gps 
import time 
session = gps.gps("127.0.0.1", "2947") 
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
        time.sleep(0.5)
    	raw_data = session.next()
	if raw_data['class'] == 'TPV':
	        if hasattr(raw_data, 'lat')& hasattr(raw_data, 'lon'):
			             latitude=raw_data.lat
                longitude=raw_data.lon
        	print("\nLatitude is = \n"+str(latitude))
		print("Longitude is = \n"+str(Longitude))
		response = variable.save_value({'value':10, 'context':{'lat': latitude,'lng': longitude}})
    except KeyError:
	         pass
    except KeyboardInterrupt:
		     quit()
    except StopIteration:
		    session = None
		    print("No incoming data from the GPS module")
