# Task 1: Word Wrap using Dynamic Programming
from math import inf

def word_wrap(words, width):
    n=len(words)
    dp=[inf]*(n+1); nxt=[None]*(n+1)
    dp[n]=0
    states=[]
    for i in range(n-1,-1,-1):
        used=0
        for j in range(i,n):
            used += len(words[j]) + (1 if j>i else 0)
            if used>width: break
            slack=width-used
            penalty=0 if j==n-1 else slack**2
            candidate=penalty+dp[j+1]
            states.append((i,j,used,slack,penalty,dp[j+1],candidate))
            if candidate<dp[i]:
                dp[i]=candidate; nxt[i]=j+1
    lines=[]; i=0
    while i<n:
        j=nxt[i]
        if j is None: return None, dp, nxt, states
        line=words[i:j]; used=sum(map(len,line))+len(line)-1
        slack=width-used; pen=0 if j==n else slack**2
        lines.append((line,slack,pen))
        i=j
    return lines,dp,nxt,states

def run_case(text,width):
    words=text.split()
    lines,dp,nxt,states=word_wrap(words,width)
    print(f"INPUT width={width}; words={words}")
    print("DP states (dp[i] = minimum penalty from word i to end):")
    for i,v in enumerate(dp): print(f"  dp[{i}]={v}")
    print("Candidate transitions (i,j,used,slack,linePenalty,tail,candidate):")
    for s in states: print(" ",s)
    if lines is None:
        print("FAIL: width too small to fit at least one word.")
        return
    print("Chosen lines:")
    for k,(line,slack,pen) in enumerate(lines,1):
        print(f"  Line {k}: {' '.join(line)} | unused={slack} | penalty={pen}")
    print("Minimum total penalty:",dp[0])

if __name__=="__main__":
    sample="Dynamic programming creates optimal document layouts with balanced line spacing"
    for w in [16,22,30]:
        run_case(sample,w); print("-"*60)
    print("BOUNDARY: single word longer than width")
    run_case("extraordinary",5)
