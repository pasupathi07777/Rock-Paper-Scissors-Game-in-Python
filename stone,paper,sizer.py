print("\t \t \t \t Welcome To Rock Paper Scissor Game \n \nTotal Ten Rounds")
totao_round=0
computer_point=0
human_point=0


while totao_round<=10:
      
          
          if totao_round ==10:
              print("\n\tGame Over")
              if human_point>computer_point:
                  print(f"\n\tHuman point:{human_point}\n\tCongratulation Human U Are Winner")
                  break
              else :
                print(f"\n\tComputer point{computer_point} \n\tComputer Is Winner")
                break
          print(f"reamining rounds = {10-totao_round} human points = {human_point}  computer point = {computer_point}")
          
         
              


          
          
          
          
  
  
          a1=["r","p","z"]
          import random
          computer=random.choice(a1)
          human=input("Rock For r,Paper For p,Scissor for z :")
          print(human)
       
          if human=="":
            while True:
                human=input("Enter Again :")
                if human!="":
                    break
          
          if (human=="r"and computer=="z"):
            print(f"Human = {human} \nComputer = {computer}")
            print("Human Wins 1 Point")
            human_point=human_point+1
            print(f"Human Point:{human_point} \nComputer Point:{computer_point}, ")
            totao_round =totao_round+1
            print(f"Reamining Rounds {10-totao_round}")

           

            
            
          elif (human=="p"and computer=="r"):
            print(f"Human = {human} \nComputer = {computer}")
            print("Human Wins 1 Point")
            human_point=human_point+1
            
            print(f"Human Point:{human_point} \nComputer Point:{computer_point}, ")
            totao_round =totao_round+1
            print(f"Reamining Rounds {10-totao_round}")

          
          elif (human=="z"and computer=="p"):
              print(f"Human = {human} \nComputer = {computer}")
              print("Human wins 1 Point")
              human_point=human_point+1
              
              print(f"Human Point:{human_point} \nComputer Point:{computer_point} ")
              totao_round =totao_round+1
              print(f"Reamining Rounds {10-totao_round}")
          
        

          elif (human==computer):
              print(f"Human = {human} \nComputer = {computer}")
              print("Tie Both 0 Point To Each")
            
              print(f"Human Point:{human_point} \nComputer Point:{computer_point} ")
              totao_round =totao_round+1
              print(f"Reamining Rounds {10-totao_round}")
         
          else:
            print(f"Human = {human} \nComputer = {computer}")
            print("Computer win 1 Point")
            computer_point=computer_point+1
            print(f"Human point:{human_point} \nComputer Point:{computer_point} ")
            totao_round =totao_round+1
            print(f"Reamining rounds {10-totao_round}")
            

          






     






     

          


        
        
          
    


    
    


    

    
            



    

    
