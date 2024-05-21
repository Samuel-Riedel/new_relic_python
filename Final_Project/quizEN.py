
class QuestionEnglish:
    def __init__(self,prompt,option,answer):
        self.prompt = prompt 
        self.option = option
        self.answer = answer

    def is_correct(self,user_answer):
            user_answer == self.answer


class QuestionSpanish:
     def __init__(self, prompt, option,answer):
          self.prompt = prompt
          self.option = option
          self.answer = answer
    
     def is_correct(self, user_answer):
      user_answer == self.answer