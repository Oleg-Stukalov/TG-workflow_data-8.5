from aiogram import Bot, Dispatcher
from config_data.config import load_config
#from temp import print_func, MyTrueFilter
import temp

config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

some_var_1 = 1
some_var_2 = 'Some text'

#dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})
dp['my_int_var'] = some_var_1
dp['my_text_var'] = some_var_2
print(dp.workflow_data)
del dp['my_int_var']
print(dp.workflow_data)
#dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})
#print(dp.workflow_data['my_int_var'])
#print(dp.workflow_data['my_text_var'])
#print_func(dp.workflow_data['my_int_var'], dp.workflow_data['my_text_var'])
