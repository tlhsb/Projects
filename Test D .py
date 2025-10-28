def calculate_average(filepath):

    try:
        with open(filepath, "r") as f:  
            lines = f.readlines()
        
        total_score = 0
        count = 0
        invalid_lines = []
        
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()  
            if not line: 
                continue
                
            try:
                name, score_str = line.split(',')
                score = int(score_str)
                total_score += score
                count += 1
                print(f"Line {line_num} : {name} = {score}")
                
            except ValueError:  
                invalid_lines.append(line)
                print(f"Line {line_num} can't work: {line}")
            except Exception as e:
                print(f"Line {line_num} can't work: {e}")
        
        if count == 0:
            print("\nerror")
            return None
        
        average = total_score / count
        
  
        
    except FileNotFoundError:  
        print(f"Can't  find datas.")
        return None




# 主程序
if __name__ == "__main__":
    print("=" * 60)
    print("Calculating scores")
    print("=" * 60)
    
    result = calculate_average("scores.txt")
    
    if result is not None:
        print(f"\nAverage scores: {result:.2f}")
        print("\nCaculate succeed！")
    else:
        print("\nCalculate failed.")
    
    print("=" * 60)
    print("Process is over")
    print("Finished")  # ✅ 只在这里显示一次

