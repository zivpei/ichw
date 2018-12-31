"""wcount.py: count words from an Internet file.

__author__ = "Liu Xingpei"
__pkuid__  = "1800011711"
__email__  = "zivpei@pku.edu.cn"
"""


import sys
from urllib.request import urlopen
# 此处import error 是为了能catch住URLError
from urllib import error


def wcount(lines, topn=10, dic={}):
	"""此函数能实现数词功能
	"""

	# 此处字典务必务必要复制
	copied_dic = dic.copy()

	# 用字典的形式记录文本中的单词（换成小写）的个数
	for word in lines.split():
		copied_dic[word.lower()] = copied_dic.get(word.lower(), 0) + 1

	# 按照单词出现的次数，以降序排序
	sorted_dic = sorted(copied_dic.items(), key=lambda kv: kv[1], reverse=True)

	# 返回前n个高频词
	return sorted_dic, topn


def print_(wcount):
	"""此函数将wcount返回的值打印出来
	"""

	sorted_dic, topn = wcount
	for i in range(topn):
		mat = "{:20}{:20}"
		print(mat.format(sorted_dic[i][0], str(sorted_dic[i][1])))


def main():
	try:
		with urlopen(sys.argv[1]) as doc:
			docstr = doc.read().decode()
			# 此处拷贝是为了保证遍历对象不发生改变

			# 注意在try-except结构里面，变量不是局部的！(That's good!)
			a = docstr

			# 用for循环将文本中的非字母元素全部换为空格，方便split()
			for string in docstr:
				if string.isalpha() == False:
					a = a.replace(string, " ")

		# 如果用户输入了topn
		if len(sys.argv) == 3:
			# 如果用户输入的topn小于文本中出现的单词数，则可以按要求打印前n个高频词
			if int(sys.argv[2]) <= len(wcount(a)[0]):
				print_(wcount(a, topn=int(sys.argv[2])))

			# 如果用户输入的topn大于文本中出现的单词数，则打印文本中所有单词及其出现次数	
			else:
				n = len(wcount(a)[0])
				print_(wcount(a, topn=n))
				print("Since the 'topn' you've input is out of range, " + 
				"we then printed all the words contained in this article!")

		# 如果用户没输入topn，则只打印前10个高频词
		else:
			print_(wcount(a))
			print("The words showed above are the ten which appeared in this txt most frequently.")

	# 对HTTPError进行提示		
	except error.HTTPError as err:
		print(err)

	# 对普通的URLError进行提示	
	except error.URLError as err:
		print(err)

	# 对ValueError进行提示	
	except ValueError as err:
		print(err)

	# 如果用户除了文件名外没有在终端输入其他元素（url），则对其给予提示
	except IndexError:
		print('Usage: {} url [topn]'.format(sys.argv[0]))
		print('  url: URL of the txt file to analyze ')
		print('  topn: how many (words count) to output. If not given, will output top 10 words')
		sys.exit(1)



if __name__ == "__main__":
	main()
