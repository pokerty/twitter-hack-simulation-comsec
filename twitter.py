import requests

class TwitterClient:
    def __init__(self):
        self.base_url = "https://api.twitter.com/1.1"
        self.users = {'abcd@gmail.com':['token1','twitteruser1'],'abcdef@gmail.com':['token2','twitteruser1']}

    def discover_twitter_id(self, user_input):
        # first post request
        print("Sending post request with email")
        header = {"User-Agent":user_input}
        body = {"flow_token":None}
        response = requests.post(self.base_url, data=body, headers=header)

        # simulate vulnerability response
        if user_input in self.users:
            response = {"flow_token":self.users[user_input][0],"status":"success"}
            print(f"HTTP Response: {response}")

            # second post request
            print("Sending post request with the found flow_token")
            body_2 = {"flow_token":self.users[user_input][0]}
            response_2 = requests.post(self.base_url, data=body_2, headers=header)

            # simulate response
            response_2 = {"flow_token":self.users[user_input][0],"status":"success", "user_id":self.users[user_input][1]}
            print(f"HTTP Response: {response_2}")

            # return id
            twitter_id = self.users[user_input][1]
            return twitter_id
        
        else:
            print("No user with this email address")

if __name__ == "__main__":
    # Instantiate the Twitter client
    twitter_client = TwitterClient()

    # Simulate user input (phone number or email address)
    user_input = input("Enter phone number or email address: ")

    # Discover Twitter ID based on user input
    twitter_id = twitter_client.discover_twitter_id(user_input)

    if twitter_id:
        print(f"Discovered Twitter ID: {twitter_id}")
    else:
        print("No Twitter ID found.")