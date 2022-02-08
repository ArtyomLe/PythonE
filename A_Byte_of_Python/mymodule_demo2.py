from mymodule import sayhi, __version__ # ипортирует всё что указано
#from mymodule import * # ипортирует всё кроме __version__

sayhi()
print('Версия', __version__)
