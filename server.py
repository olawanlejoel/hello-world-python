import psutil
import os
import json
import requests

def get_disk_usage():
 #Gets the disk usage of persistent storage.

 mount_path = "/var/lib/data"
 usage = psutil.disk_usage(mount_path)

 return {
   "total": usage.total / (1024 ** 3),
   "used": usage.used / (1024 ** 3),
   "free": usage.free / (1024 ** 3)
 }

def send_slack_alert(disk_usage_info):
  endpoint = os.environ.get('SLACK_WEBHOOK_URI')

  # Create a Slack message attachment
  attachment = {
    	"text": "Disk Space Usage",
    	"fields": [
        	{
            	"title": "Used",
            	"value": str(disk_usage_info['used']),
            	"short": True
        	},
        	{
            	"title": "Free",
            	"value": str(disk_usage_info['free']),
            	"short": True
        	},
        	{
            	"title": "Total",
            	"value": str(disk_usage_info['total']),
            	"short": True
        	}
    	]
	}
 
  # Create the main message payload
  payload = {
	"attachments": [attachment]
	}
 
  # Convert the payload to JSON format
  json_data = json.dumps(payload)
 
  headers = {
    	"Content-type": "application/json"
	}
 
  requests.post(endpoint, data=json_data, headers=headers)

if __name__ == "__main__":
 disk_info = get_disk_usage()

 print(disk_info)

 threshold_level = 10

 if(disk_info['free'] < threshold_level):
   print('Alert! Disk space is below the set threshold level.')

send_slack_alert(disk_info)