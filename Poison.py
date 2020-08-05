class Poison:
    poisonMsg = "done"

    @staticmethod
    def isPoisonMsg(msg):
        return str(msg) == Poison.poisonMsg
