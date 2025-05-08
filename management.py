# CSV file management.

import csv
import os

class VoteDataManager:
    def __init__(self, filename):
        self.filename = filename

        if os.path.isfile(self.filename):
            return
        #if file doesn't already exist create one
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["VoterID", "Candidate"])

    def has_voted(self, voter_id):
        #look for ID that was previously used
        with open(self.filename, 'r') as f:
            next(f)
            for line in f:
                pos = line.strip().split(',')
                if len(pos) >= 1 and pos[0] == voter_id:
                    return True
        return False

    #add a new row when necessary
    def record_vote(self, voter_id, candidate):
        with open(self.filename, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([voter_id, candidate])

