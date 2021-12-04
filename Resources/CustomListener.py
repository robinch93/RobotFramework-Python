import os, shutil
from os import path
import webbrowser

class CustomListener:
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.current_dir = os.getcwd()
        self.output_dir = path.join(self.current_dir, "outputs")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def close(self):
        self.moveAllReportFiles()
        self.openReports("log.html")
    
    def moveOutputFiles(self,filename):
        shutil.move(path.join(self.current_dir, filename), path.join(self.output_dir, filename))

    def moveAllReportFiles(self):
        self.moveOutputFiles("log.html")
        self.moveOutputFiles("output.xml")
        self.moveOutputFiles("report.html")

    def openReports(self, filename):
        webbrowser.open("file://" + path.join(self.output_dir, filename))