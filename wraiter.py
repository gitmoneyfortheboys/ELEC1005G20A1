'''
Author: Yuvraj Sood
Project: WRAITER : Next Genaration AI Content Writer
'''
import openai
import os
import webbrowser
import pyperclip as pc
from dotenv import load_dotenv

load_dotenv()

openai.api_key = "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" #os.getenv('OPENAI_API_KEY')
model_engine = "text-davinci-003"

def email_parameters(name):
    '''
    This takes in user information to generate a prompt to pass through to the OPENAI API.
    '''
    print()
    recipient = input("Who are you writing this email to? (e.x. Mother, Father, Friend, Teacher) - ")
    emailid = input("Enter the email id of the recipeient - ")
    subject = input("What is the subject of your email? (e.x. Request for absence) - ")
    tone = input("what is the tone of your email? (e.x. formal,informal) - ")
    info = input("Enter any additional information to include and other requirements that you may have - ")
    prompt = (f'''Write an email to my {recipient} about {subject} in a {tone} tone in no less than 300 words.
    Exclude stating the subject. Be sure to include the email signature with my name which is {name}. {info}''')
    return prompt, recipient, emailid, subject, tone

def blog_parameters():
    print()
    subject = input("What is the subject of this blog post? (e.x. Will AI take your job?) - ")
    audience = input("Enter any demographic information about your audience (e.x. Adults aged 18-25, Majority male and based in the US) - ")
    sections = input("What are the different sections of the blog? (e.x. Introduction, What is AI, Is my job in danger?) - " )
    info = input("Enter any additional information to include and other requirements that you may have - ")
    prompt = (f'''Write a proffessional blog based on the following information -
     Subject - {subject}
     Audience - {audience}, (DO NOT state the audience but use it as a parameter for generating content that would appeal to them)
     sections - {sections}
     extra info - {info}''')
    return prompt

def caption_parameters():
    print()
    subject = input("What is the subject of the social media post? (e.x. Promoting a Social event) - ")
    platform = input("Which platform is this caption for? (e.x. Instagram, Reddit) - ")
    adjectives = input("Enter any relevant adjectives for the caption. (e.x. Cheesy, Funny, Pun) - ")
    info = input("Enter any additional information to include and other requirements that you may have - ")
    prompt = (f'''Write a social media caption based on the following information -
     Subject - {subject}
     Platform - {platform}
     Caption Tone/Vibe - {adjectives}
     extra info - {info}, also generate 10 hashtags relevant to this context along with the caption, try to keep your response limited to 150 characters not inclusive of hashtags.''')
    return prompt

def api_request(user_prompt):
    '''
    this calls the OPENAI API and generates a response.
    '''
    completion = openai.Completion.create(
    engine = model_engine,
    prompt = user_prompt,
    max_tokens = 3700,
    n = 1,
    stop = None,
    temperature = 0.4,)

    response = completion.choices[0].text 
    return (response)
    


def main():
    name = input("Hi, what is your name? ")
    print(f'Hope you are having a good day {name}!\n')

    menu = input('''What do you want to write today?
1. Email
2. Blog
3. Social Media Caption
''')

    while not(menu=='1' or menu=='2' or menu=='3') :
        print("Invalid Output! Choose an option from 1 to 3.")
        menu = input('''What do you want to write today?
1. Email
2. Blog
3. Social Media Caption
''')

    if menu == '1':
        information = email_parameters(name)
        body = api_request(information[0])
        webbrowser.open('mailto:?to=' + information[2] + '&subject=' + information[3] + '&body=' + body)#, new=1)
    elif menu == '2':
        information = blog_parameters()
        blog = api_request(information)
        pc.copy(blog)
        print(blog)
        print("\nThe blog has been copied to your clipboard!")

    else:
        information = caption_parameters()
        caption = api_request(information)
        pc.copy(caption)
        print(caption)
        print("\nThe caption has been copied to your clipboard!\n")
        


if __name__ == '__main__':
    main()
