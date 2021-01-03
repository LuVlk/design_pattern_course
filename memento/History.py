class History:

    def __init__(self):
        self.__states = {}
        self.__lastPushed = ""

    def push(self, state: object):
        objType = str(type(state))

        if objType in self.__states:
            self.__states[objType].append(state)
            return
        else:
            self.__states.update({objType: [state]})
            self.__lastPushed = objType

    def pop(self, obj: object = None):
        try:
            if obj is None:
                lastState = self.__states[self.__lastPushed].pop()   
                return lastState
            
            else:
                objType = str(type(obj))
                lastState = self.__states[objType].pop()
                return lastState

        except IndexError:
            return None