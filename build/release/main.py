import os
from msvcrt import getch
from libs.index import index
import libs.scores as scores
import libs.utils as utils

def main():
    rootDir = os.environ["HOMEPATH"]
    indexFilePath = os.path.join(rootDir, 'indexed')

    if not os.path.isfile(indexFilePath):
        index()

    old_len = 0
    curr_len = 0

    while True:
        if(not old_len < curr_len):
            folders = utils.initFoldersList(indexFilePath)

        result = 'None'

        q = input()
		
        print(':')

        old_len = curr_len
        curr_len = len(q)

        basic_rx = utils.generateBasicRegex(q)
        sub_rx = utils.generateSubRegex(q)

        folders = scores.updateScores(basic_rx, sub_rx, folders)
        folders = scores.advancedScoreUpdate(q, folders)
        folders = utils.sort(folders)

        utils.printFolders(folders)
        result = utils.foldersString(folders)

main()