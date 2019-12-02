This project doesn't work (yet). I'm trying to figure out how to set up Now ZEIT to host this properly as a bunch of serverless functions before proceeding with actual functionality.

The plan is to have:
 - users register with the app through OAuth (Google will limit user count due to sensitive API requests without a full-blown domain).
 - the app obtains access tokens, encrypts them and stores on Google-side via the optional payload argument.
 - the app subscribes to event changes in the source calendar
 - on event change, it decrypts the access tokens, refreshes if needed and adds a copy of the event to the target calendar.
 - how to specify source and target calendars is an open question. This could be done by the user just after authentication (though it sounds fragile) or through a specially formatted calendar event (requires the user to follow the formatting, quite fragile as well.
