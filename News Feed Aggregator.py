import json as j
import datetime as dt
import os 
company_name = 'VEER NEWS '

def desgin():
    print(f'{'='*35}\n{company_name.center(25)}\n{'='*35}')
    print()

def menu():
    desgin()
    print('GOOD MORING SIR, WELCOME TO OUR SITE')
    while True:
        try: 
            global purpose
            print()
            purpose = str(input('DO U WANA ADD ARTICAL OR WANA READ : ')).strip().lower()
            if purpose not in ['add', 'read']:
                print('RESPONSE MUST BE ADD OR READ')
            else:
                break
        except ValueError :
            print('DONT ENTER NUMBERS U IDIOT')
        
def add_article():
    
    global all_articles
    all_articles = []
    try:
        with open('news.json',"r") as f:
            all_articles= j.load(f)
            if isinstance(all_articles,dict):
                all_articles= []
    except FileNotFoundError:          
        all_articles = []
        
    try:
            if purpose == 'add':
                date = dt.date.today()
                articletitle = input("Enter the title : ").strip().lower()
                print()
                print("Enter your Article (Enter done to finish)")
                lines2= []
                while True:
                    line = input().strip().lower()
                    if line == 'done':
                        break  
                    lines2.append(line)
                article = ' '.join(lines2)
                print()
                lines = []
                print('Enter Your summary (enter done to finsh)')
                while True:
                    line = input().strip().lower()
                    if line == 'done':
                        break  
                    lines.append(line)
                summary = ' '.join(lines)
                print()
                source = input('Where did you get this information? ').strip().lower()

                
                new_articles= {
                    'title' : articletitle,
                    'article': article,
                    'date': str(date),           
                    'source': source,
                    'summary': summary
                }
                
                all_articles.append(new_articles)
                with open('news.json','w') as f:
                    j.dump(all_articles , f , indent= 4) 
                print('Artical saved succesfully')
            
    except Exception as e:
            print(f'Something went wrong: {e}')  
                
def search_for_artical():
    if purpose =='read':
        try:
            with open('news.json','r') as f:
                all_articles = j.load(f)
        except FileNotFoundError:      
            with open('news.json','w') as f:
                j.dump([], f)
            print('No articles found')
            return
        try:
            artical_name = input('ENTER ARTICAL TITLE : ').strip().lower()
            found = False
            for articel in all_articles:
                if artical_name.strip().lower() in articel['title']:
                    print(f'Date of Publish : {articel['date']}')
                    print()
                    print(f'Article : {articel['article']}')
                    print()
                    print(f'Summary : {articel['summary']}')
                    found = True
            if found == False:
                    print('Article not found')
                    
        except Exception as e :
            print(f'Something went wrong: {e}')  



def main():
    menu()
    if purpose =='add':
        add_article()
    elif purpose =='read':
        search_for_artical()
        
     
main()
    