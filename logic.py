import re
import csv
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from vote_history import Ui_Dialog
from management import VoteDataManager


class VotLogic:
    def __init__(self,ui):
        """
                Getting ready the voting logic class.
        """
        self.ui = ui
        self.data = VoteDataManager('votes.csv')
        self.ui.statusLabel.setVisible(False)
        """
        Connect the buttons.
        """
        self.ui.submitButton.clicked.connect(self.submit_vote)
        self.ui.viewHistoryButton.clicked.connect(self.show_vote_history)

    def submit_vote(self):
        """
        When the user click submit, this runs and checks inputs and save the vote if valid
         """
        voter_id = self.ui.idInput.text().strip()
        candidate = None
        if self.ui.radioJane.isChecked():
            candidate = "Jane"
        elif self.ui.radioJonh.isChecked():
            candidate = "Jonh"

        if voter_id == '':
            self.show_message("Enter Valid ID", "red")
            return
        if candidate is None:
            self.show_message("Please Choose a Candidate", "orange")
            return
        if self.data.has_voted(voter_id):
            self.show_message("You already voted!", "red")
        else:
            self.data.record_vote(voter_id, candidate)
            self.show_message(f"Thanks! You voted for {candidate}", "green")
            self.clear_inputs()

    def show_message(self, message, color):

            self.ui.statusLabel.setText(message)
            self.ui.statusLabel.setStyleSheet(f"color: {color}; font-weight: bold;")
            self.ui.statusLabel.setVisible(True)

    def clear_inputs(self):
        """
        Resets the form spot
        """
        self.ui.idInput.clear()
        # had issues with radio buttons resetting, so did this:
        self.ui.radioJane.setAutoExclusive(False)
        self.ui.radioJonh.setAutoExclusive(False)
        self.ui.radioJane.setChecked(False)
        self.ui.radioJonh.setChecked(False)
        self.ui.radioJane.setAutoExclusive(True)
        self.ui.radioJonh.setAutoExclusive(True)

    @staticmethod
    def show_vote_history():
            dialog = QDialog()
            history_ui = Ui_Dialog()
            history_ui.setupUi(dialog)

            try:
                with open("votes.csv", "r") as f:
                    reader = csv.reader(f)
                    headers = next(reader, [])
                    data = list(reader)

                    history_ui.VoteHistoryWindow.setColumnCount(len(headers))
                    history_ui.VoteHistoryWindow.setRowCount(len(data))
                    history_ui.VoteHistoryWindow.setHorizontalHeaderLabels(headers)

                    for r in range(len(data)):
                        for c in range(len(data[r])):
                            item = QTableWidgetItem(data[r][c])
                            history_ui.VoteHistoryWindow.setItem(r, c, item)

            except FileNotFoundError:
                history_ui.VoteHistoryWindow.setRowCount(0)
                history_ui.VoteHistoryWindow.setColumnCount(0)

            history_ui.closeButton.clicked.connect(dialog.close)
            dialog.exec()

