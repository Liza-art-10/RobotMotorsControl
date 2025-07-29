class MotorController:
    def __init__(self):
        self.speed = 0
    
    def set_speed(self, value):
        """Установка скорости двигателя"""
        self.speed = value
        print(f"Скорость установлена: {self.speed}%")
    
    def emergency_stop(self):
        """Аварийная остановка"""
        self.speed = 0
        print("ДВИГАТЕЛИ ОСТАНОВЛЕНЫ")

if __name__ == "__main__":
    controller = MotorController()
    controller.set_speed(50)
    controller.emergency_stop()
