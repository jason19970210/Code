# Python

Using `UTF-8`,`Unicode Strings`

### Contents

+ #### [Comment](#Comment)
+ #### [Data Type](#Python_Data_Type)
	+ #### [Number](#Number)
		+ ##### [類別宣告](#類別宣告)
		+ ##### [Functions For Number](#Functions_For_Number)
			+ [Math](#Python_Math)
			+ [Random](#Python_Random)
			+ [Trigonometric Function](#Python_Trigonometric_Function)
		+ #### [String](#String)
			+ #### [Functions For String](#Functions_For_String)
		+ #### [List](#List)
		+ #### [Tuple](#Tuple)
		+ #### [Set](#Set)
		+ #### [Dictionary](#Dictionary)
			+ ##### [利用 Value 反查 Key](#value_key)
			+ ##### [檢查 Dict 中有無包含特定的 Key](#dict_key)
		+ #### [運算子](#cal)
			+ ##### [算數邏輯](#calculate)
			+ ##### [比較邏輯](#compare)
			+ ##### [賦值邏輯](#give_value)
			+ ##### [二進位邏輯](#binary_logic)
			+ ##### [邏輯閘](#logic_gate)
			+ ##### [成員](#member)
		+ #### [Input](#Python_input)
		+ #### [If-Else Function](#Python_If_Else)
		+ #### [For Loop Function](#Python_Loop_Function)
		+ #### [Import](#Python_Import)
		+ #### [Function](#Python_Function)
	+ #### [爬蟲](#Python_Scapying)
	+ #### [AIY Goolge Voice Kit](#Python_VoiceKit)





<a name="Comment" />

### Comment
+ 單行註解：`# 註解`
+ 多行註解：
	<pre><code>
	```
	註解 
	```
	</code></pre>

<a name="Python_Data_Type" />

### Data Type
+ 標準資料型態：`Number`, `String`, `List`, `Tuple`(元組), `Sets`(集合), `Dictionary`
+ 檢視資料型態
	- print(type(a))
	- isinstance(a,int)

	```
	a = 111
	print(type(a))
	isinstance(a,int)

	Output:
	Line[1]: <class 'int'>
	Line[2]: True
	```
<a name="Number" />

+ Number : `int`, `float`, `bool`, `complex`(複數)

	<a name='類別宣告' />

	+ 類別宣告
		- int(x)
		- float(x)
		- complex(x)
		- complex(x,y)
			> 將 x 和 y 轉換到一個複數，實數部分為 x, 虛數部分為 y,  x 和 y 是數字表達式

	<a name='Functions_For_Number'>

	+ Functions For Number

		<a name='Python_Math' />

		+ Math
			- abs(x)
				> 取絕對值
			- fabs(x)
				> 取絕對值(float)
			- ceil(x)
				> 無條件進位
			- floor(x)
				> 無條件捨去, 高斯
			- log(x)
				> 取對數值
			- log10(x)
				> 取以10為底的對數值
			- sqrt(x)
				> 取平方根
			- max(a,b)
				> a, b 的最大值
			- min(a,b)
				> a, b 的最小值

		<a name='Python_Random' />

		+ Random
			- choice(seq)
				> 從序列的元素中隨機挑選一個元素

				```python
				random.choice(range(10))
				// 從 0～9 之間挑一個整數
				```
			- random()
				> 隨機生成一個實數, 介在[0,1)
			- shuffle(lst)
				> 將序列的所有元素隨機排序
			- uniform(x,y)
				> 隨機生成一個實數, 介在[x,y]
			- random.randint(x,y)
				> 隨機生成一個int整數, 介在[x,y]
			- random.sample(sequence,length)
				> 可以從指定的序列中，隨機的截取指定長度的片段，不修改原序列
				```
				>>> lst = random.sample('abcd1234',4)
				>>> strs = ''.join(lst)
				>>> strs
				'a432'
				```

		<a name='Python_Trigonometric_Function' />

		+ Trigonometric Function (三角函數)

<a name="String" />

+ String
	+ Word
		```
		word = ' 字符串 '
		```
	+ Sentence
		```
		" This is sentence. "
		```
	+ Paragraph
		```
		"""这是一个段落，
		可以由多行组成"""
		```
	+ 字符串格式化
		```
		print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

		Output:
		我叫 小明 今年 10 岁!
		```

	<a name='Functions_For_String' />

	+ Functions For String
		+ capitalize()
			> 將字符串的第一個字符轉換為大寫
		+ isalnum()
			> 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
		+ isalpha()
			> 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
		+ isdigit()
			> 如果字符串只包含数字则返回 True 否则返回 False
		+ islower()
			> 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
		+ isnumeric()
			> 如果字符串中只包含数字字符，则返回 True，否则返回 False
		+ isspace()
			> 如果字符串中只包含空白，则返回 True，否则返回 False
		+ len(string)
			> 返回字符串长度
		+ lower()
			> 转换字符串中所有大写字符为小写
		+ lstrip()
			> 截掉字符串左边的空格或指定字符

<a name="List" />

+ List


<a name="Tuple" />

+ Tuple

<a name="Set" />

+ Set  
	無序, 不重複元素的序列  
	+ 創建空集合：set()


<a name="Dictionary" />

+ Dictionary
	+ 映射類型：key:value, 鍵值:變數
	+ dict = {}
		> 建立空的dict
	+ del dict[key]
		> 刪除特定的 key-value pair
	+ dict[key]=value
		> 若key不存在 則增加這組pair  若key已存在 則更新這組pair

	```python
	dict = {}
	dict['one'] = "1"
	dict['2'] = "two"

	tinydict = {'name':'runnob','code':1,'site':'www.runnob.com'}

	print(dict['one'])
	print(dict['2'])
	print(tinydict)
	print(tinydict.keys())
	print(tinydict.values())

	## Output
	1
	two
	{'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
	dict_keys(['name', 'site', 'code'])
	dict_values(['runoob', 'www.runoob.com', 1])

	- - - -

	table = {}
	
	for inputTimes in range(0,5)
		k = input('輸入字串：')
		v = int(input('輸入整數：'))
		
		table[k] = v
		print(end='\n')
	print(table)
	

	## Output
	輸入字串：eat
	輸入整數：24

	輸入字串：3
	輸入整數：17

	輸入字串：Lynn
	輸入整數：19

	輸入字串：hello_world
	輸入整數：265

	輸入字串：5578
	輸入整數：201

	{'3':17, 'Lynn':19, '5578':201, 'hello_world':265, 'eat':24}
	```
	<a name='value_key' />

	+ 利用 Value 反查 Key
	```python
	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	target = 2
	for key in d:
		if d[key] == traget:
			print('key = ', key)
			break
		else:
			print('404 NOT FOUND!')
	
	## Output
	key = two
	```
	<a name='dict_key' />

	+ 檢查 Dict 中有無包含特定的 Key

	```python
	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print('one' in d)
	print(1 in d)

	## Output
	True
	False

	- - - -
	# 若想拿到一個由所有key組成的list、或一個由所有value組成的list，可以使用dict.keys()或是dict.values()。結合反查的方法，可以檢查一個特定的key或value在這個dict中存不存在。

	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print(0 in d.keys())
	print(1 in d.values())
	print('one' in d.keys())
	print(9 in d.values())

	## Output
	False
	True
	True
	False

	- - - -
	# d.get(key, default_value): 是比較安全的作法，如果key不存在的話就會回傳 default_value (下面例子中的deafult_value就是’找不到耶’)。

	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print(d['one'])
	print(d.get('two','NOT FOUND'))
	print(d.get(2,'NOT FOUND'))


	## Output
	1
	2
	NOT FOUND
	```

<a name='cal' />

+ #### 運算子

	<a name='calculate' />

	+ 算數邏輯
		+ \+ - * /
		+ % 取餘數
		+ // 取商數
		+ a ** b  a的b次方

	<a name='compare' />

	+ 比較邏輯
		+ `==` `!=` `>` `<` `>=` `<=`

	
	<a name='=give_value' />

	+ 賦值邏輯
		+ c = a + b
			> 將a + b 的運算结果赋值為 c
		+ c += a
			> c = c + a
		+ c -= a
			> c = c - a
		+ c *= a
			> c = c * a
		+ c /= a
			> c = c / a
		+ c %= a
			> c = c % a
		+ c //= a
			> c = c // a
		+ c **= a
			> c = c ** a

	<a name='binary_logic' />

	+ 二進位邏輯
		+ &
			> And Gate
		+ |
			> Or Gate
		+ ^
			> NOR Gate  
			> 兩對應二進位相異時, 輸出1
		+ ~
			> 補數
		+ \>>n
			> 右移n單位
		+ <<n
			> 左移n單位

		#### Example
		```
		a = 0011 1100
		b = 0000 1101

		a & b = 0000 1100
		a | b = 0011 1101
		a ^ b = 0011 0001
		~a = 1100 0011
		a >>2 = 1111 0000
		a <<2 = 0000 1111
		```

	<a name='logic_gate' />
	
	+ 邏輯閘
		+ And
		+ Or
		+ NOT

	<a name='member' />

	+ 成員
		+ in
		+ not in

<a name='Python_input' />
 
+ ### Input
	+ For `Python3`
		+ Use `raw_input` in `Python2`
		+ There is another function for `input` in `Python2`

		### Example
		```python
		a = input()
		print('a= ',a)

		b = input('Your Name: ')
		print('Your Name: ',b)


		## Output
		289
		a = 289
		Your Name: aaa
		Your Name: aaa

		- - - -

		a = int(input('整數1 = '))
		b = int(input('整數2 = '))
		print(a+b)
		print(a-b)
		print(a*b)
		print(a/b)


		## Output
		整數1 = 10
		整數2 = 101
		111
		-91
		1010
		0.099.....

		```
	
<a name='Python_If_Else' />

+ ### If-Else Function
	```python
	if 條件:
		do 1st
		do 2nd
	else: #else 不接條件
		do 3rd



	if 條件1:
		do 1st
	elif 條件2:
		do 2nd
	else
		do 3rd
	```

<a name='Python_Loop_Function' />

+ ### For Loop Function
	```python
	for i in range(0,10):
		print(i)


	## Output
	0
	1
	2
	3
	...
	9
	```
	range(n) = range(0,n)  
	資料只取到`n-1`  
	range 結構: range(起點,終點,間距)

	```python
	for i in range(1,10):
		for j in range(1,10):
			print(i*j,end='')
		print(end='\n')
	
	# end=' '  不希望print出來的結果換行且要有空格
	# end='\n'  若要再換行可使用end='\n'

	## Output
	99 乘法表


	for i in range(1,10,2):
		print(i)

	## Output
	1
	3
	5
	7
	9

	for i in range(10,1,-3):
		print(i)

	## Output
	10
	7
	4
	```

<a name='Python_Import' />

+ ### Import
	+ import `module`
		> import whole module
	+ from `module` import *
		> import all functions from module
	+ from `module` import `function`
		> import the function from module
	+ from `module` import `1st_function`, `2nd_function`...
		> import few functions from module

<a name='Python_Function' />

+ ### Function
	+ ### 自定義函數
		- 以 `def` 開頭 後接函數名稱和 `()`
		- 任何傳入參數和自變量必須置於 `()` 中間 `()`可用於定義參數
		- 函數的第一行可選擇性使用文檔字符 用於存放函數說明
		- 函數內容以 `:` 起始 且需縮排
		- `return[express(表達式)]` 結束函數並選擇性返回一個值給調用方
		- 不帶表達式的return則返回 `NONE`

			Example:
			```python
			def function_name(parameters):
				"函數_文檔字符串"
				function_suite
				return[express]

			- - - -
			def printme(str):
				"print 傳入的字符串到 console上 "
				print(str)
				return
			```
	+ ### 調用函數
		```python
		def printme(str):
				"print 傳入的字符串到 console上 "
				print(str)
				return

		# 調用函數
		printme("調用自定義函數")
		printme("再次調用函數")


		## Output
		調用自定義函數
		再次調用函數



		```

	+ ### BeautifulSoup
		+ 解析 HTML
	+ ### 

<a name = "Python_Scapying"/>

### 爬蟲
#### Ref : https://www.largitdata.com/course_list/1
#### Steps
+ Install `Requests`, `BeatifulSoap4`
> pip install requests  
> pip install BeautifulSoap
#### GET POST
+ GET
+ POST

<a name = "Python_VoiceKit"/>

### AIY Goolge Voice Kit with raspberrypi model B+ (Version 1)

+ ### Setup Voice Kit
	+ #### Software (raspberrypi)
	+ #### Hardware
+ ### Custom Your Own Kit
	+ #### Control speaker