"""
	
		Каталоги

"""
		import os

	# Создать каталог
		os.mkdir('poems')
		os.mkdir('poems/mcintyre')
		os.path.exists('poems')

	# Удалить:
		os.rmdir('poems')

	# Создержимое каталога:
	 	os.listdir('poems')

	# Изменить каталог:
		os.chdir('poems')


""" 

	Перечисляем совпадающие файлы с помощью функции glob() (Синтаксис Unix, а не все регулярные выражения)
	
		* - совпадает со всем
		? - совпадает с 1 символом
		[abc] -  совпадает с символами a,b и c
		[!abc] -  совпадает со всеми символами, кроме a,b и c

"""

	import glob

	# Файлы и каталоги, наичнающиеся на m
		glob.glob('m*')

	# Файы и каталоги, состоящие из 2х символов:
		glob.glob('??')

	# Слово из 8 букв, начинается на m и заканчивается на e
		glob.glob('m??????e')

	# Начинается на k,l,m , заканчивается на e
		glob.glob('[klm]*e')