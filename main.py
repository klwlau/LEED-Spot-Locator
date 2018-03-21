from matplotlib import rcParams
from UsedFunc import *
import glob
import datetime
import time

rcParams['figure.figsize'] = [10., 8.]


def mainLoop():
    #init first row in CSV file
    writeBufferArray = [["File Name","Number of Spots","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C","Am","x_0","y_0","sigma_x","sigma_y","theta","A","B","C"]]
    counter = 0;
    fileAmount = len(fileList)
    for fileName in fileList:
        counter += 1
        templist, numberOfSpots = findSpot(fileName, 5, mask, scaleFactor=1, showSpots=False)
        writeBufferArray.append(templist)

        print(counter, ",", numberOfSpots, ",", fileName, ",", counter / fileAmount * 100, "%")
        if counter % writeBuffer == 0:
            saveToCSV(writeBufferArray, CSVName)
            writeBufferArray = []
        if counter == fileAmount:
            saveToCSV(writeBufferArray, CSVName)

print("---Initializing---")
start_time = time.time()


#setup
timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H%M')
CSVName = timeStamp + ".csv"
folderName= parameterList["folderName"]
# int parameter, make Mask, read file name in folder
if not folderName:
    fileList=glob.glob("./*.tif")
else:
    fileList = glob.glob("./" + folderName + "/*.tif")

setPicDim(fileList[0])  # to set the picWidth,picHeight for findSpot function
mask = makeMask(parameterList["maskConfig"]["mask_x_center"], parameterList["maskConfig"]["mask_y_center"]
                , parameterList["maskConfig"]["innerRadius"], parameterList["maskConfig"]["outerRadius"])  # int mask
writeBuffer = 50


if parameterList["testMode"]:
    findSpot(fileList[9], 20, mask, scaleFactor=1,showSpots=True,plotSensitivity=4)
else:
    mainLoop()


print("--- %s Minutes ---" % ((time.time() - start_time)/60))
print("done")
