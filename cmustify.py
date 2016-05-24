import sys
import time
import notify2


class Cmustify(object):

    # Dictionary that will contain our parsed-out data.
    cmus_info = {'status': "",
                 'url': "",
                 'file': "",
                 'artist': "",
                 'album': "",
                 'discnumber': "",
                 'tracknumber': "",
                 'title': "",
                 'date': "",
                 'duration': "",
                 'break': ""}

    def __init__(self, status_data=None):
        self.data = {}
        self.status_data = status_data
        if self.status_data:
            self.parse_data(self.status_data)

    def parse_data(self, raw_data):
        """ Parse cmus data """
        # Our temporary collector list.
        collector = []

        data = raw_data.split()

        # add break key to obtain the last element
        data.append("break")

        # Loop through cmus data and write it to our dictionary.
        last_found = "status"
        for value in data:
            collector.append(value)
            # We check if the value match a cmus key
            for key in self.cmus_info:
                # If a match has been found, record the data
                if key == value:
                    collector.pop()
                    self.data[last_found] = " ".join(collector)
                    collector = []
                    last_found = key

    def get_data(self, key):
        try:
            return self.data[key]
        except KeyError:
            return None

    def format_notification_body(self):
        notification_body = ""
        if self.get_data("title"):
            notification_body = self.get_data("title")
        else:
            notification_body = "Unknown"

        if self.get_data("album") and self.get_data("artist"):
            notification_body += " by " + self.get_data('artist') + ', ' + \
                                 self.get_data('album')
        elif self.get_data("artist"):
            notification_body += " by " + self.get_data('artist')

        return notification_body

    def display_song(self):
        """Display the song data using notify-send."""
        if self.get_data("status") == "playing":
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
                text_body = self.format_notification_body()
                # Check if we have a notify_body to avoid
                # putting a "by" at the end
                if text_body:
                    notification = notify2.Notification(
                                    "Cmustify - current song", text_body, "")
                    notification.set_urgency(notify2.URGENCY_LOW)
                    notification.show()
            return True
        else:
            return False

    def print_usage(self):
        print("Usage informations will be print")


def main():
    cmustify = Cmustify()
    try:
        # See if script is being called by cmus before proceeding.
        if sys.argv[1].startswith("status"):
            cmustify.parse_data(sys.argv[1])
            cmustify.display_song()
    except:
        cmustify.print_usage()

if __name__ == "__main__":
    main()
