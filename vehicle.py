class Vehicle:

    def __init__(self, max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model1 = Vehicle(180,18)
model2 = Vehicle(200,20)

print("mode1 speed:", model1.max_speed)
print("mode2 speed:", model2.max_speed)
print("mode1 mileage:", model1.mileage)
print("mode2mileage:", model2.mileage)