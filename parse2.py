import os.path
import errno
import math
import string

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def make_assignFolder(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

initialPath = "C:/Users/Sydney/Desktop/skuhl/spring 16/sonic lab/Portable Python 2.7.6.1/Space Mission Transcripts/"
#response = raw_input("How many hours do you want in each file? ")
response = 6
for folderName in get_immediate_subdirectories(initialPath):
	combinedPath = os.path.join(initialPath, folderName)
	#print combinedPath
	os.chdir(combinedPath)
	#print os.getcwd()
	with open("mission.txt", "rb") as textfile:
		dayTracker = 0
		hourlast = 0
		for row in textfile:
			line = row.split(':')
			spacedItems = row.split('\t')
			timeSegments = spacedItems[0].split(':')
			hour = int(timeSegments[1])
			interval = int(response)
			textonly = row.split('\t')[-1]
			#missionFolder = os.path.join(initialPath, folder)
			speakerName = row.split('\t')[1]
			validFolderForSpeaker = ''.join(c for c in speakerName if c in valid_chars)
			#print combinedPath
			folderPath = os.path.join(combinedPath, validFolderForSpeaker)
			#print combinedPath
			#folderPath = os.path.join(r'C:/Users/Sydney/Desktop/skuhl/spring 16/sonic lab/Portable Python 2.7.6.1/', row.split('\t')[1])
			useFolder = str(folderPath)
			make_assignFolder(folderPath)
			if ((hour == 0) and (hourlast == 23)):
				#print hour
				dayTracker += 1
				#hourTracker = 0
			intervalInName = int(math.floor(hour / interval) * interval)
			fileName = str("day" + str(dayTracker) + "-" + str(intervalInName) + "-" + str(row.split('\t')[1]) + ".txt")
			with open(os.path.join(useFolder, fileName), "ab") as output:
			#with open(str(line[0]) + "-" + str(row.split('\t')[1]) + ".txt", "ab") as output:
				output.write(str(textonly))
			hourlast = hour
os.chdir("C:/Users/Sydney/Desktop/skuhl/spring 16/sonic lab/Portable Python 2.7.6.1")



		