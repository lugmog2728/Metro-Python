def parseFile(fileToParse):
        objects = []
        with open(fileToParse, 'r') as file :
                lines = file.readlines()
                for line in lines:
                        fields = line.strip().split(' ')
                        object = []
                        for field in fields:
                                object.append(field)
                        objects.append(object)
        return objects

                