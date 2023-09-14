import os
from datetime import datetime


class Log:
    """Class to configure log settings"""

    CURRENT_DATE = datetime.now()

    def __init__(self):
        self._log_date = self.CURRENT_DATE.strftime("%d%m%Y%H%M%S")
        self._log_name = f"log_{self._log_date}.txt"
        self._log_directory = os.path.join(os.getcwd(), "log", "logs-files")
        self._log_path = os.path.join(self._log_directory, self._log_name)
        self._status = False

    def start_log(self) -> None:
        """Method to start the log file"""
        if not os.path.isdir(self._log_directory):
            os.makedirs(self._log_directory)

        access_date = self.CURRENT_DATE.strftime("%d/%m/%Y %H:%M:%S")

        if not os.path.exists(self._log_path):
            initial_content = [
                f"{'*'*70}\n",
                f"{'*'*1}{' '*22}Online Store Microservice{' '*21}{'*'*1}\n",
                f"{'*'*1}{' '*2}Access: {access_date}{' '*39}{'*'*1}\n",
                f"{'*'*70}\n",
            ]

            with open(self._log_path, "w") as log_file:
                log_file.writelines(initial_content)

        self._status = True

    def add_message(self, message: str) -> None:
        """Method to add a message to the log file"""
        if self._status is False:
            self.start_log()

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(self._log_path, "a") as log_file:
            new_content = f"\n{date}| {message}"
            log_file.write(new_content)
