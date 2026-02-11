from collections import defaultdict

def findWinners(self, matches):   
    win, loss, freq = [],[],defaultdict(int)
    for w, l in matches:
        freq[w] += 0
        freq[l] += 1
    for k, v in freq.items():
        if v == 1:
            loss.append(k)
        if v == 0:
            win.append(k)
    print(freq)
    return [sorted(win), sorted(loss)]