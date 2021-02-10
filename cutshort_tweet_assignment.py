from collections import Counter
input_test_cases=int(input())
output=[]

for i in range(input_test_cases):
    tweets=[]
    input_tweets_number=int(input())
    for i in range(input_tweets_number):
        tweet_input=input().split()
        if(len(tweet_input)==2):
            tweets.append(tweet_input[0])
        else: 
            print('enter data in correct format. Terminating!!!')
            break
        
    dict_tweets=dict(Counter(sorted(tweets)))
    #print(dict_tweets)
    max_tweets=max(dict_tweets.values())
    #print(max_tweets)
    for key, values in dict_tweets.items():
        if (values==max_tweets):
            #print(key,values)
            output.append(key)
            output.append(values)
            
# Note: I am excluding SPACE here as the editor enables space. 
[print(output[i],' ',output[i+1]) for i in range(0,len(output)-1,2)]        