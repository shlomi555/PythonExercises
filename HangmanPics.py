def HangmanPic(lives):
    list = [''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      // 
     |
     |___''',
            '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___''',
            '''
      _______
     |/      |
     |      (_)
     |     
     |      
     |
     |___''',
            '''
      _______
     |/      
     |      
     |     
     |      
     |
     |___''',
            '''

     |/      
     |      
     |     
     |      
     |
     |___
            '''
            ]
    print(list[lives])