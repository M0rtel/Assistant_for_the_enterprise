# Тут мы импортируем все хендлеры для личной переписки с пользователем
from .start import dp
from .buttons_who_are_you import dp
from .buttons_data_time import dp
from .work_sewing import dp
from .work_blanks import dp
from .orders_command import dp
from .orders_command import dp
from .buttons_del_save_message import dp
from .button_del_add_dressmarker import dp

from .error import dp

__all__ = ['dp']  # Список параметров, которые можно импортировать из папки users
