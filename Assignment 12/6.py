class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours % 24, total_minutes % 60)

    def __sub__(self, other):
        total_minutes_self = self.hours * 60 + self.minutes
        total_minutes_other = other.hours * 60 + other.minutes
        total_minutes_diff = (total_minutes_self - total_minutes_other) % (24 * 60)
        return Time(total_minutes_diff // 60, total_minutes_diff % 60)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

t1 = Time(10, 30)
t2 = Time(2, 45)

print(f"Time 1: {t1}")
print(f"Time 2: {t2}")
print(f"Addition: {t1 + t2}")
print(f"Subtraction: {t1 - t2}")
