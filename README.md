# Log Parser and Analyzer

This tools works by feeding the parser logs (brute-force attempts, suspicious sudo usage, login outside hours and access to suspicious end points) and then all this are converted into a format that is readable, the readable format is feedeed into the log analayzer which then analzyes it for us to which (Groups it by IP address, user, or time), Count repeated actions (e.g., failed logins from one IP) and set thresholds to trigger alert after it is analyzed it generates a readable format for us.
