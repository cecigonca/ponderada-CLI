from serial.tools import list_ports #to list available serial ports
import pydobot #to control Dobot robots
import inquirer #for creating interactive command-line interfaces
from yaspin import yaspin #to add progress indicators (example: spinners)
import typer #to create command-line applications in an easier way

home_point = {"x":0, "y":0, "z":0,"r":0}  #home point of the robot arm
app = typer.Typer()
spinner = yaspin(text="Em andamento...", color="blue") #show loading indication
available_ports = list_ports.comports() #list of available serial ports

#user to choose a serial port
chosen_port = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]

#initialize pydobot
robot = pydobot.Dobot(port=chosen_port)

class Robot: #class to organize robot's functions
    def turn_on(self):
        robot.suck(True)

    def turn_off(self):
        robot.suck(False)

    def home(self):
        spinner.start()
        robot.move_to(home_point["x"], home_point["y"], home_point["z"], home_point["r"]) 
        spinner.stop()

    def current(self):
        current_position = robot.pose()
        print(f"Posição atual: {current_position}")

    def mover(self, axys: str, distance: float):
        current_position = robot.pose() 
        spinner.start()
        
        
        #define a dictionary mapping each axis to its corresponding position in the robot's pose vector
        axis_mapping = {
            "x": (distance, current_position[1], current_position[2], current_position[3]),
            "y": (current_position[0], distance, current_position[2], current_position[3]),
            "z": (current_position[0], current_position[1], distance, current_position[3]),
            "r": (current_position[0], current_position[1], current_position[2], distance)
        }
    
        robot.move_to(*axis_mapping[axys])
        spinner.stop()

@app.command(name="menu")
def menu():
    robot_instance = Robot()
    options = ["Ligar", "Home", "Posição Atual", "Mover", "Desligar"]

    while True: #prompt the user to choose an action from the menu
        chosen_action = inquirer.prompt([
            inquirer.List("action", message="Escolha uma das opções", choices=options)
        ])["action"]

        #execute the chosen action
        if chosen_action == "Ligar":
            robot_instance.turn_on()
        elif chosen_action == "Home":
            robot_instance.home()
        elif chosen_action == "Posição Atual":
            robot_instance.current()
        elif chosen_action == "Mover":
            axis = input("Digite o eixo no qual você deseja mover a ferramenta do robô (x, y, z, r): ")
            distance = float(input("Digite o valor da distância que você deseja mover o robô: "))
            robot_instance.mover(axis, distance)
        elif chosen_action == "Desligar":
            robot_instance.turn_off()

#start the application
if __name__ == "__main__":
    app()