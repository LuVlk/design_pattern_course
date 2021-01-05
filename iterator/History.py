from typing import List


class History:
    """ a History for storing object states in a dictionary

        classmethods:
        - push(state: object)
        - pop(obj: object = None)
    """

    def __init__(self) -> None:
        self.__states: dict = {}
        self.__last_pushed: str = ""

    def push(self, state: object):
        """ adds a state to the history depending on the object type """

        obj_type = str(type(state))

        if obj_type in self.__states:
            self.__states[obj_type].append(state)
        else:
            self.__states.update({obj_type: [state]})

        self.__last_pushed = obj_type

    def pop(self, obj: object = None) -> object:
        """ returns and deletes the last state depending on the object type.

            If no argument is given, it returns the last state of the
            last object that has been added.

            If the history is empty, None will be returned.
        """

        try:
            if obj is None:
                return self.__states[self.__last_pushed].pop()

            obj_type = str(type(obj))
            return self.__states[obj_type].pop()

        except IndexError:
            return None

        except KeyError:
            return None

    def get_states(self, obj: object = None) -> List[object]:
        """ returns the stored states depending on the object type.

            If no argument is given, it returns the stored states of the
            last object that has been added.

            If the history is empty, a list of None will be returned.
        """

        try:
            if obj is None:
                return self.__states[self.__last_pushed]

            obj_type = str(type(obj))
            return self.__states[obj_type]

        except IndexError:
            return [None]

        except KeyError:
            return [None]
