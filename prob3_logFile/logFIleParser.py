import os
import re

# Regex used to match relevant loglines (only lines containing warn or error words)
regex = re.compile(r".WARN|ERROR")

# Output file
outFile = os.path.normpath("outPutLogs.log")
# always creating a blank file before writing to it
with open(outFile, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(outFile, "a") as out_file:
    # Open input file in 'read' mode
    with open("inputLogs.log", "r") as in_file:
        # Loop over each log line
        for line in in_file:
            # If log line matches our regex then put into the output file
            if (regex.search(line)):
                out_file.write(line)
