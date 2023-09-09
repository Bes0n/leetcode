#!/usr/bin/python3.10
from collections import defaultdict

# text = "loonbalxballpoon"
# text = "balllllllllllloooooooooon"
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"

def maxNumberOfBalloons(text):
    b = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
    }
    h = defaultdict(int)
    if len(text) < 7:
        return 0
    
    for c in text:
        if c in b:
            h[c] += 1
    
    for c in h:
        h[c] = h[c] // b[c]

    return min(h.values())

print(maxNumberOfBalloons(text))