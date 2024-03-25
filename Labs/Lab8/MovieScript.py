class MovieScript(object):
    # begin the class definition
    # declare a data element as a list
    # data = [[script (string)], [duration (int)], [characters (array of strings)]]
    data = [[], [],[]]
    
    # the class constructor
    def __init__(self) :
        # pass
        print ("a class object has been constructed\ n")
    
    # a class member function
    def getScript(self) :
        return self.data[0]

    def getScriptIndex(self, i):
        return self.data[0][i]

    def getDurationIndex(self, i):
        return self.data[1][i]

    def getActorsIndex(self, i):
        return self.data[2][i]


    # a class member function
    def setScript(self, s) :
        self.data[0] = s
    
    def addScene(self, scene, duration, characters):
        # scene is a string, duration is int, actors is array of string
        self.data[0].append(scene)
        self.data[1].append(duration)
        self.data[2].append(characters)

    def __len__(self):
        return len(self.data[0])

# end the class definition
ms = MovieScript()
    