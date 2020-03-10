import sys
import os
import datetime
import schedule
import time

def job():
  now = datetime.datetime.now().time().isoformat(timespec='minutes')
  os.system("osascript -e 'display notification \"" + str(now) + "\"'")
  exit()

def main():
  args = sys.argv
  schedule.every().day.at(args[1]).do(job)

  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == '__main__':
    main()
