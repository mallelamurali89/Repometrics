import os
from pprint import pprint

class Repometrics:
    all_files = []
    filter_files = {}
    total_filescount = None
    def __init__(self):
        cwd = os.getcwd()
        self.get_allfiles()
        self.total_filescount = len(self.all_files)
        self.organize_files()
        self.calculate_result()


    def get_allfiles(self):
        for path, subdirs, files in os.walk(os.getcwd()):
            for name in files:
                self.all_files.append(os.path.join(path, name))

    def organize_files(self):
        for i in self.all_files:
            filename, file_extension = os.path.splitext(i)
            self.filter_files.setdefault(file_extension, []).append(i)

    def calculate_result(self):
        results = {
        "summary":{},
        "results":[]
        }
        for i,j in self.filter_files.items():
            for k in j:
                results["results"].append({"path":k,"language":i})
            results["summary"][i] = len(self.filter_files[i])/self.total_filescount

        pprint(results)



if __name__ == "__main__":
    Repometrics()
