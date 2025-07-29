import time

class MotorController:
    def __init__(self):
        self.speed = 0
    
    def set_speed(self, value):
        self.speed = value
        print(f"Скорость установлена: {self.speed}%")
    
    def emergency_stop(self):
        self.speed = 0
        print("ДВИГАТЕЛИ ОСТАНОВЛЕНЫ")
    
    def smooth_acceleration(self, target_speed, duration=3.0):
        """Плавное изменение скорости"""
        step = 1 if target_speed > self.speed else -1
        print(f"Плавный разгон с {self.speed}% до {target_speed}%...")
        
        for speed in range(self.speed, target_speed, step):
            self.speed = speed
            print(f"Текущая скорость: {speed}%")
            time.sleep(duration / abs(target_speed - self.speed))
        
        self.speed = target_speed

if __name__ == "__main__":
    controller = MotorController()
    controller.smooth_acceleration(75)
    controller.emergency_stop()
