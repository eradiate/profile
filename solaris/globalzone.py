#!/usr/bin/env python

import subprocess
import sys

def get_zone():
  servers = {}
  zones = subprocess.Popen('/usr/sbin/zoneadm list -p',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
  (run_zones,e)=zones.communicate()
  run_zones = run_zones.rstrip()
  current_zones = run_zones.split('\n')
 
  global_name = socket.gethostname()
 
  #process only servers that are non global
  for zone in current_zones:
    if re.search(r'global',zone): continue
    server = zone.split(':')
    servers[server[1]] = server[3]
 
  print "updating global names for all the containers"
 
  for k,v in servers.items():
    global_path = v + "/root/etc/globalname"
    #global_path = "test"
    print "updating following paths",global_path
    print "global_path",global_path
    with open(global_path,"w") as gf:
      gf.write(global_name+"\n")
 
  print  "globals updated"
 
def main():
  get_zone()
 
 
if __name__ == "__main__":
  # can only be run on globals
  isglobal = subprocess.Popen('/usr/bin/zonename',stdout=subprocess.PIPE,shell=True)
  (global_test,e) = isglobal.communicate()
  global_test = global_test.rstrip()
  if global_test == "global":
    print "yes it's global"
    main()
  else:
    print "This script should only be run on a global server."
    sys.exit(1)
