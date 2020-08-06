# Cmpsc 132
# Smmer 2020
# Omer Canca
# Stats Final


def calcBaseballStats():
    def getFileName(path):


        # Split over slashes
        split = path.split('\\')

        # Find the file extension
        for i in range(len(split)):

            if '.' in split[i]:

                index = i
            
        # Return the index with the dot extension
        return str( split[i] )

    def openFile(path):


        # Default directories:
        directory_path = '/Users/omercanca/Desktop/Final/Final_Stats.txt'
        folder_path = '/Users/omercanca/Desktop/Final/Final_Stats.txt'

        try:
            with open(path) as fileRead:

                fileName = getFileName(path)

                return path, fileName

        except FileExistsError:

            print('\nFile does not exist')

        except FileNotFoundError or PermissionError:

            print('\n> Incorrect path')
            print('\tUsing default path:', folder_path)

            with open(folder_path) as fileRead:

                fileName = getFileName(folder_path)

                return folder_path, fileName

    def parseFile(path, fileName):

        with open(path) as fileObject:

            data = []
            dataNew = []

            print('\n> Reading', fileName, '\n')

            # Initially read to use eof while loop
            buffer = str(fileObject.readline())         # Read file line into temporary <buffer> string

            # Eof while loop
            while buffer != '':

                buffer = buffer.split()                 # Split <buffer> over space
                data.append(buffer)                     # Store <buffer> string in <data> list
                buffer = str(fileObject.readline())     # Read file line into temporary <buffer> string

            for i in range(len(data)):

                if '//' not in data[i]:

                    # This is not a commented line

                    if len(data[i]) == 2:

                        # This is a name line (first + last)

                        dataNew.append( str( data[i][0] + ' ' + data[i][1] ))

                    if len(data[i]) == 5:

                        # This is a data line

                        lst = []

                        for j in range(len(data[i])):

                            if ',' in data[i][j]:

                                # Split over commas
                                temp = data[i][j].split(',')

                                # Remove commas
                                temp.pop()

                            # Replace & convert to int
                            lst.append( int(temp[0]) ) 

                        dataNew.append(lst)

            return dataNew

    def calculate(data):


        for i in range(1, len(data) ):

            BA = int(( data[i][1] / data[i][0] ) * 1000 )

            OBP = int(( ( data[i][1] + data[i][4]) / ( data[i][0] + data[i][4]) ) *1000 )

            data[i].append(BA)
            data[i].append(OBP)

        return data

    def printStats(stats):

        print('\tPlayer:\t', stats[0], '\n')

        print('\tGame:\tAB:\tHit:\tHR:\tSO:\tWalk:\tBA:\tOBP:')

        for i in range(1, len(stats)):

            print('\t', i,'\t', stats[i][0], '\t', stats[i][1], '\t', stats[i][2], '\t', stats[i][3], '\t', stats[i][4], '\t', stats[i][5], '\t', stats[i][6])

        print('\n> End of Program')

    def main():

        # Take input
        path = str(input('\nEnter the path of the data file:\n'))

        # Open file in read mode
        path, fileName = openFile(path)

        # Parse the data
        rawData = parseFile(path, fileName)

        # Calculate Statistics
        statistics = calculate(rawData)

        # Print data
        printStats(statistics)


    # Call main

    main()
calcBaseballStats()
