import psutil

def get_disk_usage():
 #Gets the disk usage of persistent storage.

 mount_path = "<YOUR-PERSISTENT-STORAGE-MOUNT-PATH>"
 usage = psutil.disk_usage(mount_path)

 return {
   "total": usage.total / (1024 ** 3),
   "used": usage.used / (1024 ** 3),
   "free": usage.free / (1024 ** 3)
 }

if __name__ == "__main__":
 disk_info = get_disk_usage()

 print(disk_info)

 threshold_level = 10

 if(disk_info['free'] < threshold_level):
   print('Alert! Disk space is below the set threshold level.')
