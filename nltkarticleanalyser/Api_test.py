from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='6e0889093eff41548dc316635e3d2e38')


req_data = {"id": [], "publishedAt": [], "name": [], "title": [], "description": [] }

titledata=[]
descdata=[]

def informationgather(input) :
    all_articles = newsapi.get_everything(q=input,
                                          from_param='2022-01-09',
                                          to='2022-02-09',
                                          language='en',
                                          sort_by='relevancy')
    x = len(all_articles['articles'])
    for i in range(5):
        titledata.append(all_articles['articles'][i]['title'])
        descdata.append(all_articles['articles'][i]['description'])
    return (titledata , descdata)





