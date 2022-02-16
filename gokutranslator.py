class GokuTranslator:
    def __init__(self,posPath):
        self.posPath=posPath
    def normalizeRow(self,row):
        if row.find('#')>=0:
            return row.strip()[:-(len(row)-row.find('#'))]
        else:
            return row.strip()
    def getInstructions(self):
        instructions={}
        lines=open(self.posPath,'r').readlines()
        lastInstuction=""
        clickCount=0
        sleepCount=0
        for i in lines:
            normalizedLine=self.normalizeRow(i)
            if len(normalizedLine)<=0:
                pass
            elif normalizedLine.find(':')>=0:
                lastInstuction=normalizedLine[:-(len(normalizedLine)-normalizedLine.find(':'))]
                instructions[lastInstuction]={}
            else:
                splittedLine=normalizedLine.split()
                if(len(splittedLine))>1:
                    if splittedLine[1].find(',')>=0:
                        splittedLine[1]=splittedLine[1].split(',')
                        clickCount+=1
                        splittedLine[0]=f"{splittedLine[0]}{clickCount}"
                        splittedLine[1][0]=int(splittedLine[1][0])
                        splittedLine[1][1]=int(splittedLine[1][1])
                    elif not splittedLine[1]=='goku':
                        sleepCount+=1
                        splittedLine[0]=f"{splittedLine[0]}{sleepCount}"
                        splittedLine[1]=float(splittedLine[1])
                    instructions[lastInstuction][splittedLine[0]]=splittedLine[1]
                else:
                    instructions[lastInstuction][splittedLine[0]]=splittedLine[0]
        return instructions

if __name__ == "__main__":
    g=GokuTranslator('scripts/dbl.txt')
    print(g.getInstructions())