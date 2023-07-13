import rospkg
import subprocess
import os

# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()

print('\033[93mYOU NEED TO HAVE A ROSCORE RUNNING!\033[0m')

# Get the file path to the default pcd file created by smb_slam
mapPath = input('path to .pcd file: ')
# mapPath = '/home/jonas/rss/maps_slam/sim_maps/map.pcd'

# Get the path to the script
smb_nav_path = rospack.get_path('smb_navigation')

# Make the script executable
os.system('chmod +x ' + smb_nav_path + '/script/pcd_to_gridmap.sh') 

# Set the arguments and run the script
output_path = input('path to output folder: ')
run_rviz = 'true'

command_string = smb_nav_path + '/script/pcd_to_gridmap.sh ' + mapPath + ' ' + output_path + ' ' + run_rviz
os.system(command_string) 
