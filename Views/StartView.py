class StartView:
    DEFAULT_SEQUENCE = ''

    def get_input(self, message:str):
        inputSequence = input(message)

        if inputSequence == self.DEFAULT_SEQUENCE:
            return False

        return inputSequence

    def varify_input_sequence(self, inputSequence):
        hasWhitespace = False
        for i in range(0, len(inputSequence)):
            current = int(inputSequence[i])
            
            if inputSequence[i] == self.DEFAULT_SEQUENCE:
                hasWhitespace = True
                continue 
            elif current < 1 or current > 8:
                return False

        return True and hasWhitespace


    def print_message(self, message:str):
        print(message)