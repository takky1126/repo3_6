data = []

file_path = input("ファイル：")
Rule = input("ルール（昇順：0,降順：1）")

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.split(':')
        date = parts[0]
        temp = float(parts[1])
        data.append((date, temp))

#ソート処理 (昇順: 0, 降順: 1)
# reverse=True で降順、False で昇順
is_reverse = True if Rule == "1" else False

#温度を基準にソート
data.sort(key=lambda x: x[1], reverse=is_reverse)

#出力処理
for date, temp in data:
    print(f"{date}: {temp}")

#ファイル書き換え（上書き）
with open(file_path, 'w', encoding='utf-8') as f:
    for date, temp in data:
        f.write(f"{date}: {temp}\n")