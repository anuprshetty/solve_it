# Assignment: Find who tweeted the most

You will be given a list of tweets
Your program should find the user who has tweeted the most

Note:
If multiple users are having the same number of tweets, then print all the users in alphabetical order of user names.
Use Python 3
Follow python coding style guide
Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

## Input format

Read the input from the console.
The first line of input should be the number of test cases
The remaining lines of input should contain each test case input.

For each test case input:
First-line should contain the number of tweets.
Followed by N lines, each containing user name and tweet id separated by a space.

## Output format

Find the user with max number of tweets. Print user name and the total number of tweets.

Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3

Sample 2:
Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output
kohli 2
sachin 2
sehwag 2

Sample 3:
Input 
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

Output
sachin 2
sehwag 2
dhoni 4

Sample 4:
Input
3
4
sehwag tweet_id_2
sehwag tweet_id_4
sachin tweet_id_1
sachin tweet_id_3
7
sehwag tweet_id_10
sehwag tweet_id_11
kohli tweet_id_12
sachin tweet_id_13
sachin tweet_id_14
sachin tweet_id_1
sehwag tweet_id_4
5
sachin tweet_id_2
kohli tweet_id_4
kohli tweet_id_1
kohli tweet_id_3
sachin tweet_id_5

Output
sachin 2
sehwag 2
sachin 3
sehwag 3
kohli 3
