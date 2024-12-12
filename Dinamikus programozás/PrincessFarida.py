def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for i in range(t):
        n = int(data[index])
        index += 1
        
        if n == 0:
            print(f"Case {i + 1}: 0")
            continue
        
        arr = list(map(int, data[index:index + n]))
        index += n
        
        if n == 1:
            print(f"Case {i + 1}: {arr[0]}")
            continue
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for j in range(2, n):
            dp[j] = max(dp[j - 1], dp[j - 2] + arr[j])
        
        print(f"Case {i + 1}: {dp[n - 1]}")

if __name__ == "__main__":
    main()