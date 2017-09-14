

def now():
	print('2017-4-4')

f = now

print(f())

a = now.__name__
print(a)


#假设我们要增强now()函数的功能，
#比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper