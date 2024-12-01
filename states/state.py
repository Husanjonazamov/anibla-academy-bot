from aiogram.dispatcher.filters.state import State, StatesGroup





class Register(StatesGroup):
    name = State()
    phone = State()
    
    
class NameChange(StatesGroup):
    name = State()
    
    
class PhoneChange(StatesGroup):
    phone = State()
    
    
class Homeworks(StatesGroup):
    file = State()