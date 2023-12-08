
from engine_service_criteria import EngineServiceCriteria
from battery_service_criteria import BatteryServiceCriteria

class Car:
    def __init__(self, last_service_date,engine: EngineServiceCriteria, battery: BatteryServiceCriteria):
        self.last_service_date = last_service_date
    
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.service_criteria.needs_service()
    
    def get_service_criteria(self):
        return self.service_criteria.get_service_criteria()
