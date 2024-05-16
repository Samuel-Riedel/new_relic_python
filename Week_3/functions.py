#Comprehensive Exercise - Function Module

def car(**kwargs):
 result = (
        f"The car was manufactured by: {kwargs['manufactured']}\n"
        f"The model is: {kwargs['model']}\n"
        f"Color is: {kwargs['color']}\n"
        f"It was manufactured in the year: {kwargs['year']}\n"
        f"Does it have autopilot: {kwargs['autopilot']}\n"
    )
 print(result)

car(manufactured="Toyota \n",  model="Corolla \n",  color="Red\n",  year="1999\n",  autopilot="True\n")
