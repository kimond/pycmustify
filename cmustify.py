#! /usr/bin/env python
import sys
import time
import notify2

def print_usage():
   """Display usage info and exit."""
   print "Print usage todo"

def status_data(item):
   """Return the requested cmus status data."""

   # We loop through cmus status data and use each of its known data
   # types as 'delimiters', collecting data until we reach one,
   # inserting it into the dictionary -- rinse and repeat.

   # cmus helper script provides our data as argv[1].
   cmus_data = sys.argv[1]

   # Split the data into an easily-parsed list.
   cmus_data = cmus_data.split()

   if not "date" in cmus_data:
       cmus_data.append("date")

   # Our temporary collector list.
   collector = []

   # Dictionary that will contain our parsed-out data.
   cmus_info = {'status':"",
                'url': "",
                'file':"",
                'artist':"",
                'album':"",
                'discnumber':"",
                'tracknumber':"",
                'title':"",
                'date':"",
                'duration':""}

   # Loop through cmus data and write it to our dictionary.
   last_found = "status"
   for value in cmus_data:
       collector.append(value)
       # Check to see if cmus value matches dictionary key.
       for key in cmus_info:
           # If a match has been found, record the data.
           if key == value:
               collector.pop()
               cmus_info[last_found] = " ".join(collector)
               collector = []
               last_found = key

   # Return whatever data main() requests.
   return cmus_info[item]

def display_song():
   """Display the song data using notify-send."""

   # We only display a notification if something is playing.
   if status_data("status") == "playing":

       # Check to see if title data exists before trying to display it.
       # Display "Unknown" otherwise.
       if status_data("title") != "":
           notify_summary = status_data("title")
       else:
           notify_summary = "Unknown"

       # Check to see if album data exists before trying to
       # display it. Prevents "Artist, " if it's blank.
       if status_data("album") != "":
           notify_body = status_data("artist") + ', ' + \
                         status_data("album")
       else:
           notify_body = status_data("artist")

       # Create our temporary file if it doesn't exist yet.
       open("/tmp/cmus_desktop_last_track", "a").write("4")

       # Check to see when we got our last track from cmus.
       last_notice = open("/tmp/cmus_desktop_last_track", "r").read()

       # Write time stamp for current track from cmus.
       last_notice_time = str(time.time())
       open("/tmp/cmus_desktop_last_track", "w").write(last_notice_time)

       # Calculate seconds between track changes.
       track_change_duration = round(time.time() - float(last_notice))

       # Display current track notification only if 5 seconds have
       # elapsed since last track was chosen.
       if track_change_duration > 5:
           # Execute notify2 to create the notification
           notify2.init("cmus-display")
           text_body = notify_summary
           # Check if we have a notify_body to avoid putting a "by" at the end
           if notify_body:
               text_body = text_body + " by " + notify_body
           notification = notify2.Notification("Cmustify - current song", text_body, "")
           notification.set_urgency(notify2.URGENCY_LOW)
           notification.show()

def main():
   try:
       # See if script is being called by cmus before proceeding.
       if sys.argv[1].startswith("status"):
           display_song()
   except:
       print_usage()

if __name__ == "__main__":
   main()
