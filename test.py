import sys

output_file = sys.argv[-1]
input_files = sys.argv[1:-1]

results = []

for filename in input_files:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        l_count = len(lines)
        w_count = sum(len(line.split()) for line in lines)
        c_count = sum(len(line) for line in lines)
        
        # データの整形
        results.append(f"file: {filename}")
        results.append(f"lines: {l_count}")
        results.append(f"words: {w_count}")
        results.append(f"chars: {c_count}\n")

# --- 追加：cmd上への表示とファイル書き込み ---
output_text = "\n".join(results)
print(output_text)

# ファイルに保存
with open(output_file, 'w', encoding='utf-8') as f_out:
    f_out.write(output_text)