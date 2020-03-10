import sys
import os
import datetime
import schedule
import time

def job():
  now = datetime.datetime.now().time().isoformat(timespec='minutes')
  os.system("osascript -e 'display dialog \"" + str(now) + "\" with text buttons {\"close\"} default button 1'")
  exit()

def main():
  args = sys.argv
  if args[1] == "now":
    job()
  else:
    schedule.every().day.at(args[1]).do(job)

    while True:
      schedule.run_pending()
      time.sleep(5)

if __name__ == '__main__':
    main()
