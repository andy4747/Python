from datetime import datetime as dt
import time

hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

website_list = ['facebook.com']

def block_site(start_hour,end_hour):
    start_hour = dt(dt.now().year,dt.now().month,dt.now().day,start_hour) #work start date and time
    end_hour = dt(dt.now().year,dt.now().month,dt.now().day,end_hour) # work start date and time
    current_time = dt.now()
    if start_hour < current_time < end_hour: # if current time is between start_hour and end_hour (Work Hour)
        print("Working Hours")
        with open(hosts_path,'r+') as file: #opening file in read and write mode
            contents = file.read()
            for website in website_list: 
                if website not in contents: # if website is blocked if not already
                    file.write(redirect+"   "+website+"\n")
    else: # if the time is fun hours
        with open(hosts_path,"r+") as file:
            contents = file.readlines()
            file.seek(0) # sets current file path in 0th position in file stream
            for line in contents:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #sets the file size as the currnt file stream position
        print("Fun Hours")
    time.sleep(5)

if __name__ == "__main__":
    block_site(8,16) #Work hours 8:00 AM to 4:00 PM
