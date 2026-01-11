import sys

output_file = sys.argv[-1]
input_files = sys.argv[1:-1]

results = []

for filename in input_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            l_count = len(lines)
            w_count = sum(len(line.split()) for line in lines)
            c_count = sum(len(line) for line in lines)
            
            # 各ファイルの結果を整形してリストに追加
            results.append(f"file: {filename}")
            results.append(f"lines: {l_count}")
            results.append(f"words: {w_count}")
            results.append(f"chars: {c_count}\n") # 各ブロックの間に空行
            
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# まとめて出力ファイルへ書き出し
with open(output_file, 'w', encoding='utf-8') as f_out:
    f_out.write("\n".join(results))
