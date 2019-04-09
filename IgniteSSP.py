print('IgniteSSP2018 | Created by TJ.THANAPAT')

def intersect(a, b):
    return list(set(a) & set(b))

class booth:
    def __init__(self,R1,R2,R3,R4):
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.R4 = R4

    def printDetail(self): #Print The List of UserName for Each Rounds
        print("Details")
        print("R1: " + str(self.R1))
        print("R2: " + str(self.R2))
        print("R3: " + str(self.R3))
        print("R4: " + str(self.R4))

    def printMaxRound(self): #Print The Max Round(s)
        A = len(self.R1)
        B = len(self.R2)
        C = len(self.R3)
        D = len(self.R4)
        List4items = [A,B,C,D]
        MaxValue = max(List4items)
        List = List4items
        print("MaxPPLRound (" + str(MaxValue) + ")")
        BoothRound = []
        for i in range(4):
            if (List[i] == MaxValue):
                if (i == 0):
                    BoothRound.extend(["R1"])
                elif (i == 1):
                    BoothRound.extend(["R2"])
                elif (i == 2):
                    BoothRound.extend(["R3"])
                elif (i == 3):
                    BoothRound.extend(["R4"])
        print(BoothRound)
        return MaxValue

    def printMinRound(self): #Print The Min Round(s)
        A = len(self.R1)
        B = len(self.R2)
        C = len(self.R3)
        D = len(self.R4)
        List4items = [A,B,C,D]
        MinValue = min(List4items)
        List = List4items
        print("MinPPLRound (" + str(MinValue) + ")")
        BoothRound = []
        for i in range(4):
            if (List[i] == MinValue):
                if (i == 0):
                    BoothRound.extend(["R1"])
                elif (i == 1):
                    BoothRound.extend(["R2"])
                elif (i == 2):
                    BoothRound.extend(["R3"])
                elif (i == 3):
                    BoothRound.extend(["R4"])
        print(BoothRound)
        return MinValue


    def printBoothWeight(self): #Print BoothWeight
        A = len(self.R1)
        B = len(self.R2)
        C = len(self.R3)
        D = len(self.R4)
        List4items = [A, B, C, D]
        MaxValue = max(List4items)
        MinValue = min(List4items)
        print("BoothWeight: " + str(MaxValue - MinValue))
        return MaxValue - MinValue

    def getBoothWeight(self): #Get Value of BoothWeight
        A = len(self.R1)
        B = len(self.R2)
        C = len(self.R3)
        D = len(self.R4)
        List4items = [A, B, C, D]
        MaxValue = max(List4items)
        MinValue = min(List4items)
        return MaxValue - MinValue

    def getListRoundSorted(self): #Get ListRound sorted by Num of User in ascending order
        A = len(self.R1)
        B = len(self.R2)
        C = len(self.R3)
        D = len(self.R4)

        ListRound = ['R1','R2','R3','R4']
        ListRoundVal = [A, B, C, D]

        ListRoundSorted = []
        ListRoundValSorted = sorted(ListRoundVal)
        SetRoundValSorted = list(set(ListRoundValSorted))
        NumofRoundVal = len(set(ListRoundValSorted))
        for i in range(NumofRoundVal):
            if SetRoundValSorted[i] == ListRoundVal[0]:
                ListRoundSorted.extend([ListRound[0]])
            if SetRoundValSorted[i] == ListRoundVal[1]:
                ListRoundSorted.extend([ListRound[1]])
            if SetRoundValSorted[i] == ListRoundVal[2]:
                ListRoundSorted.extend([ListRound[2]])
            if SetRoundValSorted[i] == ListRoundVal[3]:
                ListRoundSorted.extend([ListRound[3]])
        return ListRoundSorted




G01 = booth([],[],[],[])
G02 = booth([],[],[],[])
G03 = booth([],[],[],[])
G04 = booth([],[],[],[])
G05 = booth([],[],[],[])
G06 = booth([],[],[],[])
G07 = booth([],[],[],[])
G08 = booth([],[],[],[])
G09 = booth([],[],[],[])
G10 = booth([],[],[],[])
G11 = booth([],[],[],[])
G12 = booth([],[],[],[])
G13 = booth([],[],[],[])
G14 = booth([],[],[],[])
G15 = booth([],[],[],[])
G16 = booth([],[],[],[])
G17 = booth([],[],[],[])
G18 = booth([],[],[],[])
G19 = booth([],[],[],[])
G20 = booth([],[],[],[])
G21 = booth([],[],[],[])
#Command new 'Booth' when new booth option was added

def printAllBoothsDetails():
    print('\n')
    print('G01')
    G01.printDetail()
    print('\nG02')
    G02.printDetail()
    print('\nG03')
    G03.printDetail()
    print('\nG04')
    G04.printDetail()
    print('\nG05')
    G05.printDetail()
    print('\nG06')
    G06.printDetail()
    print('\nG07')
    G07.printDetail()
    print('\nG08')
    G08.printDetail()
    print('\nG09')
    G09.printDetail()
    print('\nG10')
    G10.printDetail()
    print('\nG11')
    G11.printDetail()
    print('\nG12')
    G12.printDetail()
    print('\nG13')
    G13.printDetail()
    print('\nG14')
    G14.printDetail()
    print('\nG15')
    G15.printDetail()
    print('\nG16')
    G16.printDetail()
    print('\nG17')
    G17.printDetail()
    print('\nG18')
    G18.printDetail()
    print('\nG19')
    G19.printDetail()
    print('\nG20')
    G20.printDetail()
    print('\nG21')
    G21.printDetail()
    print('\n')


ListUserName = []
DBUser = []

def printUserDetail(UserName):
    NumOfUserInDB = len(DBUser)

    for i in range(NumOfUserInDB):
        UserDetail = DBUser[i]
        if UserDetail[0] == UserName:
            print("UserName: " + UserName)
            UserBooth = UserDetail[1]
            print("R1:" + UserBooth[0] + " | R2:" + UserBooth[1] + " | R3:" + UserBooth[2] + " | R4:" + UserBooth[3])



def printAllUserDetail():
    NumOfUserInDB = len(DBUser)
    for i in range(NumOfUserInDB):
        UserDetail = DBUser[i]
        UserName = UserDetail[0]
        printUserDetail(UserName)

ListBoothOptions = ['G01','G02','G03','G04','G05','G06','G07','G08','G09','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20','G21']
#Add new 'item' when new booth option was added

def inputUser():
    ##Funtion for Get inputs from User, including UserName and SelectedBooths
    print('\nEnter your name')
    while True:
        user_Name = input("Name: ")

        #Check whether user_name is not duplicated
        if intersect([user_Name],ListUserName) == []:
            ListUserName.extend([user_Name])
            break
        print("This name has created!")

    print('Enter 4 booths you interested')
    while True:
        user_Booths = input("Selected Booths: ")
        user_Booths = user_Booths.upper()  # Capitalize the letter
        userSB = user_Booths.split()  # Split str into list

        #Check whether user enters 4 booths and not enter the same booths
        if len(set(userSB)) == 4:
            for i in range(4):
                if (userSB[i] == '01') or (userSB[i] == '1'):
                    userSB[i] = 'G01'
                elif (userSB[i] == '02') or (userSB[i] == '2'):
                    userSB[i] = 'G02'
                elif (userSB[i] == '03') or (userSB[i] == '3'):
                    userSB[i] = 'G03'
                elif (userSB[i] == '04') or (userSB[i] == '4'):
                    userSB[i] = 'G04'
                elif (userSB[i] == '05') or (userSB[i] == '5'):
                    userSB[i] = 'G05'
                elif (userSB[i] == '06') or (userSB[i] == '6'):
                    userSB[i] = 'G06'
                elif (userSB[i] == '07') or (userSB[i] == '7'):
                    userSB[i] = 'G07'
                elif (userSB[i] == '08') or (userSB[i] == '8'):
                    userSB[i] = 'G08'
                elif (userSB[i] == '09') or (userSB[i] == '9'):
                    userSB[i] = 'G09'
                elif userSB[i] == '10':
                    userSB[i] = 'G10'
                elif userSB[i] == '11':
                    userSB[i] = 'G11'
                elif userSB[i] == '12':
                    userSB[i] = 'G12'
                elif userSB[i] == '13':
                    userSB[i] = 'G13'
                elif userSB[i] == '14':
                    userSB[i] = 'G14'
                elif userSB[i] == '15':
                    userSB[i] = 'G15'
                elif userSB[i] == '16':
                    userSB[i] = 'G16'
                elif userSB[i] == '17':
                    userSB[i] = 'G17'
                elif userSB[i] == '18':
                    userSB[i] = 'G18'
                elif userSB[i] == '19':
                    userSB[i] = 'G19'
                elif userSB[i] == '20':
                    userSB[i] = 'G20'
                elif userSB[i] == '21':
                    userSB[i] = 'G21'

                # Command new 'elif' when new booth option was added

            if len(intersect(userSB, ListBoothOptions)) == 4:
                break
        print('You must enter 4 different booths!')

    user_SelectedBooths = userSB
    user_SelectedBooths = sorted(user_SelectedBooths)  # Sort items in ascending order A-Z
    print("\nName: " + user_Name)
    print("SelectedBooths: " + str(user_SelectedBooths))
    return [user_Name, user_SelectedBooths]


def randomRound(Listof4SelectedBooths):

    ##Srarting Function for Rearange Booths by BoothWeight##
    ##reorderListbyBoothWeight(Listof4SelectedBooths)

    List = Listof4SelectedBooths #List of 4 SelectedBooths by User
    ListBoothWeight = [] #List of BoothWeight of SelectedBooths

    #Receive BoothWeight of SelectedBooths
    for i in range(4):
        if List[i] == "G01":
            ListBoothWeight.extend([G01.getBoothWeight()])
        elif List[i] == "G02":
            ListBoothWeight.extend([G02.getBoothWeight()])
        elif List[i] == "G03":
            ListBoothWeight.extend([G03.getBoothWeight()])
        elif List[i] == "G04":
            ListBoothWeight.extend([G04.getBoothWeight()])
        elif List[i] == "G05":
            ListBoothWeight.extend([G05.getBoothWeight()])
        elif List[i] == "G06":
            ListBoothWeight.extend([G06.getBoothWeight()])
        elif List[i] == "G07":
            ListBoothWeight.extend([G07.getBoothWeight()])
        elif List[i] == "G08":
            ListBoothWeight.extend([G08.getBoothWeight()])
        elif List[i] == "G09":
            ListBoothWeight.extend([G09.getBoothWeight()])
        elif List[i] == "G10":
            ListBoothWeight.extend([G10.getBoothWeight()])
        elif List[i] == "G11":
            ListBoothWeight.extend([G11.getBoothWeight()])
        elif List[i] == "G12":
            ListBoothWeight.extend([G12.getBoothWeight()])
        elif List[i] == "G13":
            ListBoothWeight.extend([G13.getBoothWeight()])
        elif List[i] == "G14":
            ListBoothWeight.extend([G14.getBoothWeight()])
        elif List[i] == "G15":
            ListBoothWeight.extend([G15.getBoothWeight()])
        elif List[i] == "G16":
            ListBoothWeight.extend([G16.getBoothWeight()])
        elif List[i] == "G17":
            ListBoothWeight.extend([G17.getBoothWeight()])
        elif List[i] == "G18":
            ListBoothWeight.extend([G18.getBoothWeight()])
        elif List[i] == "G19":
            ListBoothWeight.extend([G19.getBoothWeight()])
        elif List[i] == "G20":
            ListBoothWeight.extend([G20.getBoothWeight()])
        elif List[i] == "G21":
            ListBoothWeight.extend([G21.getBoothWeight()])
        # Command new 'elif' when new booth option was added

    #Reorder SelectedBooths by BoothWeights
    ListSorted = [] #List of 4 SelectedBooths sorted by BoothWeights
    ListBoothWeightSorted = sorted(ListBoothWeight, reverse=True)#Sort ListBoothWeight in descending order
    SetBoothWeightSorted = sorted(list(set(ListBoothWeightSorted)), reverse=True)
    NumofBoothWeight = len(set(ListBoothWeightSorted))
    for i in range(NumofBoothWeight):
        if SetBoothWeightSorted[i] == ListBoothWeight[0]:
            ListSorted.extend([List[0]])
        if SetBoothWeightSorted[i] == ListBoothWeight[1]:
            ListSorted.extend([List[1]])
        if SetBoothWeightSorted[i] == ListBoothWeight[2]:
            ListSorted.extend([List[2]])
        if SetBoothWeightSorted[i] == ListBoothWeight[3]:
            ListSorted.extend([List[3]])

    ##return ListSorted

    ##Ending Function for Rearange Booths by BoothWeight##


    ##Starting Function for Random Round of each SelectedBooths##
    ##randomRound(Listof4SelectedBoothsSorted)
    ##ListSorted = Listof4SelectedBoothsSorted

    ListBoothsRound = []

    def randomboothround (ListRoundSorted,ListBoothsRound):
        lstR = ListRoundSorted
        lstBooth = ListBoothsRound
        if intersect([lstR[0]],lstBooth) == []:
            lstBooth.extend([lstR[0]])
        elif intersect([lstR[1]],lstBooth) == []:
            lstBooth.extend([lstR[1]])
        elif intersect([lstR[2]],lstBooth) == []:
            lstBooth.extend([lstR[2]])
        elif intersect([lstR[3]],lstBooth) == []:
            lstBooth.extend([lstR[3]])

    for i in range(4):
        if ListSorted[i] == "G01":
            lstRG01 = G01.getListRoundSorted()
            randomboothround(lstRG01,ListBoothsRound)
        elif ListSorted[i] == "G02":
            lstRG02 = G02.getListRoundSorted()
            randomboothround(lstRG02, ListBoothsRound)
        elif ListSorted[i] == "G03":
            lstRG03 = G03.getListRoundSorted()
            randomboothround(lstRG03, ListBoothsRound)
        elif ListSorted[i] == "G04":
            lstRG04 = G04.getListRoundSorted()
            randomboothround(lstRG04, ListBoothsRound)
        elif ListSorted[i] == "G05":
            lstRG05 = G05.getListRoundSorted()
            randomboothround(lstRG05, ListBoothsRound)
        elif ListSorted[i] == "G06":
            lstRG06 = G06.getListRoundSorted()
            randomboothround(lstRG06, ListBoothsRound)
        elif ListSorted[i] == "G07":
            lstRG07 = G07.getListRoundSorted()
            randomboothround(lstRG07, ListBoothsRound)
        elif ListSorted[i] == "G08":
            lstRG08 = G08.getListRoundSorted()
            randomboothround(lstRG08, ListBoothsRound)
        elif ListSorted[i] == "G09":
            lstRG09 = G09.getListRoundSorted()
            randomboothround(lstRG09, ListBoothsRound)
        elif ListSorted[i] == "G10":
            lstRG10 = G10.getListRoundSorted()
            randomboothround(lstRG10, ListBoothsRound)
        elif ListSorted[i] == "G11":
            lstRG11 = G11.getListRoundSorted()
            randomboothround(lstRG11, ListBoothsRound)
        elif ListSorted[i] == "G12":
            lstRG12 = G12.getListRoundSorted()
            randomboothround(lstRG12, ListBoothsRound)
        elif ListSorted[i] == "G13":
            lstRG13 = G13.getListRoundSorted()
            randomboothround(lstRG13, ListBoothsRound)
        elif ListSorted[i] == "G14":
            lstRG14 = G14.getListRoundSorted()
            randomboothround(lstRG14, ListBoothsRound)
        elif ListSorted[i] == "G15":
            lstRG15 = G15.getListRoundSorted()
            randomboothround(lstRG15, ListBoothsRound)
        elif ListSorted[i] == "G16":
            lstRG16 = G16.getListRoundSorted()
            randomboothround(lstRG16, ListBoothsRound)
        elif ListSorted[i] == "G17":
            lstRG17 = G17.getListRoundSorted()
            randomboothround(lstRG17, ListBoothsRound)
        elif ListSorted[i] == "G18":
            lstRG18 = G18.getListRoundSorted()
            randomboothround(lstRG18, ListBoothsRound)
        elif ListSorted[i] == "G19":
            lstRG19 = G19.getListRoundSorted()
            randomboothround(lstRG19, ListBoothsRound)
        elif ListSorted[i] == "G20":
            lstRG20 = G20.getListRoundSorted()
            randomboothround(lstRG20, ListBoothsRound)
        elif ListSorted[i] == "G21":
            lstRG21 = G21.getListRoundSorted()
            randomboothround(lstRG21, ListBoothsRound)
        # Command new 'elif' when new booth option was added

    ##Ending Function for Random Round of each SelectedBooths##


    ListBoothsRoundSorted = sorted(ListBoothsRound)
    ListResorted = []
    for i in range(4):
        if ListBoothsRoundSorted[i]== ListBoothsRound[0]:
            ListResorted.extend([ListSorted[0]])
        elif ListBoothsRoundSorted[i]== ListBoothsRound[1]:
            ListResorted.extend([ListSorted[1]])
        elif ListBoothsRoundSorted[i]== ListBoothsRound[2]:
            ListResorted.extend([ListSorted[2]])
        elif ListBoothsRoundSorted[i]== ListBoothsRound[3]:
            ListResorted.extend([ListSorted[3]])
    ListBoothsRound = ListBoothsRoundSorted
    ListSorted = ListResorted

    return [ListSorted, ListBoothsRound]


def insertUser (userName,ListSortedAndListBoothsRound):
    ListSorted = ListSortedAndListBoothsRound[0]
    ListBoothsRound = ListSortedAndListBoothsRound[1]

    userName = userName

    DBUser.extend([[userName,ListSorted]])

    def insertDBBooth (BoothName,userName,i,ListBoothsRound):
        BoothG = BoothName
        userName = userName
        i = i
        ListBoothsRound = ListBoothsRound

        if ListBoothsRound[i] == 'R1':
            BoothG.R1.extend([userName])
        elif ListBoothsRound[i] == 'R2':
            BoothG.R2.extend([userName])
        elif ListBoothsRound[i] == 'R3':
            BoothG.R3.extend([userName])
        elif ListBoothsRound[i] == 'R4':
            BoothG.R4.extend([userName])


    for i in range(4):
        if ListSorted[i] == 'G01':
            insertDBBooth(G01, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G02':
            insertDBBooth(G02, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G03':
            insertDBBooth(G03, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G04':
            insertDBBooth(G04, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G05':
            insertDBBooth(G05, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G06':
            insertDBBooth(G06, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G07':
            insertDBBooth(G07, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G08':
            insertDBBooth(G08, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G09':
            insertDBBooth(G09, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G10':
            insertDBBooth(G10, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G11':
            insertDBBooth(G11, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G12':
            insertDBBooth(G12, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G13':
            insertDBBooth(G13, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G14':
            insertDBBooth(G14, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G15':
            insertDBBooth(G15, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G16':
            insertDBBooth(G16, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G17':
            insertDBBooth(G17, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G18':
            insertDBBooth(G18, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G19':
            insertDBBooth(G19, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G20':
            insertDBBooth(G20, userName, i, ListBoothsRound)
        elif ListSorted[i] == 'G21':
            insertDBBooth(G21, userName, i, ListBoothsRound)
        # Command new 'elif' when new booth option was added





#TestUserSelected = ['G01','G02','G03','G04']
#Test = randomRound(TestUserSelected)
#insertUser('Elon',Test)
#insertUser('Elon',randomRound(['G01','G02','G03','G04']))

'''
#Add New User manually.
while True:
    print('Do you want to add new user?')
    response = input('Y/N: ')
    if response.upper() == 'N':
        break
    elif response.upper() == 'Y':
        userInput = inputUser()  # Run Fuction for input
        userName = userInput[0]
        userSelectedBooths = userInput[1]
        userRandomRound = randomRound(userSelectedBooths)
        insertUser(userName, userRandomRound)
        print(userRandomRound)
        print('\n')
'''

insertUser('u01',randomRound(['G03', 'G10', 'G18', 'G20']))
insertUser('u02',randomRound(['G13', 'G14', 'G15', 'G17']))
insertUser('u03',randomRound(['G07', 'G09', 'G13', 'G18']))
insertUser('u04',randomRound(['G01', 'G04', 'G07', 'G09']))
insertUser('u05',randomRound(['G08', 'G09', 'G13', 'G17']))

insertUser('u06',randomRound(['G03', 'G09', 'G15', 'G17']))
insertUser('u07',randomRound(['G09', 'G10', 'G11', 'G20']))
insertUser('u08',randomRound(['G01', 'G07', 'G10', 'G17']))
insertUser('u09',randomRound(['G04', 'G12', 'G15', 'G17']))
insertUser('u10',randomRound(['G06', 'G07', 'G15', 'G17']))

insertUser('u11',randomRound(['G12', 'G15', 'G17', 'G20']))
insertUser('u12',randomRound(['G01', 'G09', 'G15', 'G20']))
insertUser('u13',randomRound(['G10', 'G17', 'G18', 'G20']))
insertUser('u14',randomRound(['G07', 'G10', 'G17', 'G20']))
insertUser('u15',randomRound(['G10', 'G12', 'G17', 'G18']))

insertUser('u16',randomRound(['G03', 'G17', 'G18', 'G20']))
insertUser('u17',randomRound(['G01', 'G02', 'G16', 'G20']))
insertUser('u18',randomRound(['G08', 'G12', 'G17', 'G21']))
insertUser('u19',randomRound(['G03', 'G09', 'G17', 'G19']))
insertUser('u20',randomRound(['G01', 'G02', 'G17', 'G18']))

insertUser('u21',randomRound(['G10', 'G12', 'G17', 'G21']))
insertUser('u22',randomRound(['G04', 'G13', 'G16', 'G17']))
insertUser('u23',randomRound(['G12', 'G17', 'G20', 'G21']))
insertUser('u24',randomRound(['G09', 'G15', 'G17', 'G20']))
insertUser('u25',randomRound(['G04', 'G13', 'G16', 'G21']))

insertUser('u26',randomRound(['G04', 'G12', 'G20', 'G21']))
insertUser('u27',randomRound(['G01', 'G09', 'G12', 'G17']))
insertUser('u28',randomRound(['G01', 'G07', 'G17', 'G20']))
insertUser('u29',randomRound(['G01', 'G04', 'G06', 'G14']))
insertUser('u30',randomRound(['G01', 'G04', 'G07', 'G09']))




printAllBoothsDetails()

print("DBUser = " + str(DBUser))

print("")

printAllUserDetail()








