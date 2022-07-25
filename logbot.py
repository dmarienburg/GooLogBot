from json import load
from json import dumps
import os

from httplib2 import Http

from Library.methods.read_logs import read_logs

class LogBot():
    def __init__(self, **kwargs):
        """
        :param url: string -
            This should be the url provided when you create the webhook for the 
            bot in your inteded google chat room

        :param script_name: string - 
            default = 'School Communications'

        :param levels: list(string) -
            The logging event level(s) which the bot will enter into chats.

            Known levels: NOTSET, INFO, DEBUG, WARNING, ERROR, CRITICAL

        :param path: string -
            An os.path like string object.
        """
        self.url = kwargs.get("url")
        self.script_name = kwargs.get("script_name", "SchoolCommunications")
        self.levels = kwargs.get("levels", ["CRITICAL"])
        self.log_results = read_logs(kwargs.get("path"), self.levels)

    def send_chat(self, text):
        """Post the value of the text param to chat

        :param text: string
        """
        http_obj = Http()
        response = http_obj.request(
            uri=self.url,
            method="POST",
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=dumps({"text": text})
        )

    def create_message_body(self):
        """Split the logs into 4096 character chunks. This is the max chat size 
        that google allows.
        """
        # Join all the log entries into a single string variable
        full_text = "\n".join([entry for entry in self.log_results])

        # Slice the full_text var into 4096 character chunks.
        for text_slice in range(0, (len(full_text)//4096)+1):
            self.send_chat(full_text[text_slice*4096:(text_slice+1)*4096])

        # If the number of characters in the text is not divisible by 4096 then
        # also make sure that the remainder of the log entries get into the chat
        if len(full_text) % 4096 != 0:
            self.send_chat(full_text[len(full_text)//4096:])

    def create_chats(self):
        """Run the process of saying what script is being reported on and then 
        start the log entries
        """
        log_count = len(self.log_results)
        if log_count == 0:
            self.send_chat(
                f"No log entries at "
                f"{' and '.join([level for level in self.levels])} found for "
                f"the {self.script_name} script"
            )
        else:
            self.send_chat(
                f"Starting Log messages from {self.script_name}" \
                f"\n\nThere are {len(self.log_results)} entries at the "\
                f"{' and '.join(self.levels)} logging levels\n\n"
            )
            self.create_message_body()
            self.send_chat(f"End of logs for {self.script_name}")

