

import shutil


def disk_info():
    disk = shutil.disk_usage(".")
    disk_used = round((( disk.free ) / 1024**3),2)
    disk_total = round(((  disk.total ) / 1024**3),2 )
    free_disk = round((( disk_used / disk_total ) * 100),2)
    
    context = f"{disk_used} / {disk_total} ({free_disk}% free)"

    return context



disk = disk_info()

print(disk)
