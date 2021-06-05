import re

#Вариант2

#2
#Написать регулярное выражение для проверки адреса электронной почты.
# В электронном адресе допустимы латинские символы верхнего и нижнего регистров, цифры, 
#точки, дефисы, подчёркивания.
li = ['abc.test@gmail.com', 'xyz@test.in', 'test.firstanalyticsvidhya.com']
for val in li:
    if re.match(r'\S+@\w+.\w+', val) and len(val) >0 :
        print ('yes')
    else:
            print ('no')

#3
#   Написать регулярное выражение, которое из текстовой строки выделяет положительное десятичное число.
# Число может содержать дробную часть, отделяемую точкой. Число должно отделяться от текста пробелами.

result = re.findall(r'\s\d+.\d*\W', ' fdfwew 124 fewjdn 2.45 fdfswe1444 fegqrty 2555.00000 123yuik fg665yj')
print (result)

#7
#Из кода html-страницы выделить тег img (изображение) со всем его содержимым.
result = re.findall(r'\s*<a href="/a/\S+.php" target="_blank"><img alt="\S+" src="http://\S+.png"></a>\s*',
                    ' <a href="/a/index.php" target="_blank"><img alt="title" src="http://test/image.png"></a>'
                    '<a href="/a/index.php" target="_blank"><img alt="title"></a>')
print (result)