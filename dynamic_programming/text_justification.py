import sys

def badness(line_length, text_total):
    return (line_length - text_total) ^ 3

def badness2(line_length, text_total):
    return (line_length - text_total)

def text_bad(line_length, word_sum):
    return badness(line_length, word_sum)

def sum_words(words):
    return sum([len(w) for w in words])

def min_badness(words, line_length):
    # start with the intuition that every line will start with a word
    # so we only need to find where to break the words.
    len_words = len(words)
    dp = [sys.maxint] * (len_words + 1)
    dp[len_words] = 0
    d = {}
    for i in range(len_words)[::-1]:
        for j in range(i + 1):
            print "i: ", i, " j: ", j
            print words[i - j: i]

            word_sum = sum_words(words[i - j: i])

            print "word_sum: ", word_sum

            if word_sum <= line_length:
                candidate = dp[i - j + 1] + text_bad(line_length, word_sum) 
            
                print "dp[i - j]: ", dp[i - j + 1]
                print "candidate: ", candidate
                
                if candidate < dp[i - j]:
                    d[i - j] = i
                    dp[i - j] = candidate
            else:
#             curr_min = min(curr_min, dp[i - j] + text_bad(line_length, words[i - j: i]))
                break
        print "dp: ", dp
        print "d: ", d

    return dp[0]

def test():
    words = ["we", "are", "not", "solving", "print", "the", "shortest", "path", "we", "are", "solving", "find","min", "value", "of", "shortest", "path"]
    print min_badness(words, 20)

if __name__ == "__main__":
    test()

