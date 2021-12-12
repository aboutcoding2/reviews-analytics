import time
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成','總共有', len(data), '筆資料')

#留言平均長度
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))	


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


start_time = time.time()
word_count = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 100000:
		print(word, word_count[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')

print(len(word_count))

while True:
	word = input('請輸入要查詢的字: ')
	if word == 'q':
		break
	print(word,'出現', word_count[word], '次')
print('感謝使用本查詢功能')