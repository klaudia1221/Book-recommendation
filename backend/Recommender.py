import books as b
import pandas as pd
import numpy as np


class Recommender:
    def __init__(self):
        self.book_tags=self.load_from_db_to_df('book_tags',cols=['goodreads_book_id','tag_id','count'])
        self.tags =self.load_from_db_to_df('tags',cols=['tag_id','tag_name'])
        self.to_read = self.load_from_db_to_df('to_read',cols=['user_id','book_id'])
        self.ratings = self.load_from_db_to_df('ratings',cols=['book_id','user_id','rating'])
        # self.books=self.load_from_db_to_df('books')

    def load_from_db_to_df(self,table_name, cols):
        data=b.get_data_from_db("SELECT * FROM {}".format(table_name))
        cols.insert(0,'index')
        df = pd.DataFrame(data, columns=cols)
        df.drop('index', axis=1)
        return df

    def create_genres(self):
        genres = [
            'fiction', 'novels', 'contemporary', 'series', 'fantasy', 'romance', 'novel', 'mystery', 'adventure',
            'drama', 'classics', 'contemporary-fiction', 'historical-fiction', 'historical', 'thriller',
            'sci-fi-fantasy', 'suspense', 'sci-fi', 'science-fiction',
            'action', 'humor', 'family', 'history', 'non-fiction', 'crime', 'fantasy-sci-fi', 'chick-lit', 'paranormal',
            'classic',
            'magic', 'mystery-thriller', 'supernatural', 'nonfiction', 'funny', 'scifi-fantasy', 'love',
            'part-of-a-series', 'mystery-suspense',
            'mysteries', 'urban-fantasy', 'thrillers', 'horror', 'science-fiction-fantasy', 'science', 'friendship',
            'scifi', 'humour', 'action-adventure', 'biography',
            'coming-of-age', 'contemporary-romance', 'women', 'philosophy', 'war', 'fantasy-scifi', 'mystery-crime',
            'comedy', 'suspense-thriller', 'ya-fantasy', 'crime-mystery', 'detective', 'crime-fiction',
            'relationships', 'memoir', 'religion', 'crime-thriller', 'murder', 'paranormal-romance', 'dark',
            'psychology', 'politics', 'sci-fi-and-fantasy', 'murder-mystery', 'sf', 'dystopian', 'classic-literature',
            'biography-memoir', 'memoirs', 'biographies', 'thriller-mystery', 'dystopia', 'sf-fantasy', 'inspirational',
            'thriller-suspense', 'paranormal-fantasy', 'autobiography', 'humorous', 'mystery-thrillers',
            'vampires', 'epic-fantasy', 'fantasy-paranormal', 'fun', 'epic', 'memoir-biography', 'animals', 'mythology',
            'chicklit', 'vampire', 'erotica', 'realistic', 'chic-lit',
            'mystery-suspense-thriller', 'spirituality', 'mystery-thriller-suspense', 'fantasy-fiction', 'spiritual',
            'comics', 'political', 'survival', 'biographical', 'travel', 'military',
            'biography-autobiography', 'art', 'comic', 'sf-f', 'love-triangle', 'witches', 'erotic', 'self-improvement',
            'religious', 'biographies-memoirs', 'vamps', 'romantic', 'sociology', 'poetry',
            'business', 'feminism', 'psychological', 'fiction-fantasy', 'fantasy-series', 'mystery-series', 'demons',
            'personal-development', 'christian', 'satire', 'mystery-detective', 'romance-contemporary', 'espionage',
            'science-fictions-and-fantasy', 'young-adult-fantasy', 'horror-thriller', 'erotic-romance', 'ghosts',
            'romantic-suspense', 'fantasy-science-fiction', 'dark-fantasy', 'lgbt', 'comic-books', 'comics-manga',
            'historical-romance', 'gothic', 'historic-fiction', 'autobiography-memoir', 'werewolves', 'faith',
            'futuristic', 'self-development', 'self development', 'personal-growth', 'mental-health', 'christianity',
            'inspiration', 'fairy-tales', 'graphic-novels-manga', 'apocalyptic', 'medieval', 'fantasy-romance',
            'future', 'memoir-bio', 'detectives', 'health', 'auto-biography', 'time-travel',
            'fantasy-and-sci-fi', 'memoirs-biographies', 'genre-fantasy', 'aliens', 'wwii', 'sciencefiction', 'dragons',
            'comix', 'vampire-books', 'memoir-autobiography', 'theology',
            'fantasy-epic', 'comic-book', 'lgbtq', 'spy', 'economics', 'urban', 'educational', 'romance-paranormal',
            'world-war-ii', 'psychological-thriller', 'crime-and-mystery',
            'historical-fiction', 'manga-comics', 'social-science', 'fantasy-sf', 'medical', 'fairies',
            'biography-and-memoir', 'apocalypse', 'christian-books', 'ww2', 'fairy-tale', 'sports', 'manga',
            'manga-graphic-novels', 'detective-fiction', 'feminist', 'queer', 'ghost', 'religion-spirituality',
            'autobiographies', 'werewolf', 'angels', 'world-war-2', 'love-story', 'animal',
            'development', 'biographies-and-memoirs', 'fairytales', 'scary', 'spies', 'suspense-mystery', 'krimi',
            'spy-thriller', 'love-stories', 'philosophical', 'fairytale', 'angels-demons',
            'biography-memoirs', 'animal-stories', 'jewish', 'angels-and-demons', 'comic-manga', 'lgbtqia',
            'graphic-novel-manga', 'holocaust', 'world-history', 'serial-killer', 'cooking', 'medicine', 'arts',
            'vampire-romance', 'love-triangles', 'mangas', 'anime']

        self.tags = self.tags[self.tags.tag_name.isin(genres)]
        autobiography_biography_memoir = ['biography', 'memoir', 'autobiography', 'biographies', 'biographies-memoirs',
                                          'autobiography-memoir', 'biography-and-memoir',
                                          'biography-memoirs', 'biography-memoir', 'memoir-biography',
                                          'biography-autobiography', 'memoirs', 'biographical', 'auto-biography',
                                          'memoir-autobiography',
                                          'memoirs-biographies', 'memoir-bio', 'autobiographies',
                                          'biographies-and-memoirs']
        fantasy = ['urban-fantasy', 'epic-fantasy', 'fantasy-paranormal', 'paranormal-fantasy', 'fantasy-series',
                   'dark-fantasy', 'genre-fantasy', 'fantasy-epic', 'fantasy-fiction',
                   'witches', 'angels', 'angels-demons', 'young-adult-fantasy', 'ya-fantasy', 'fiction-fantasy',
                   'ghost', 'angels-and-demons', 'ghosts', 'werewolves', 'werewolf', 'vamps', 'vampires', 'vampire',
                   'magic', 'vampire-books',
                   'dragons', 'demons', 'fairytale', 'paranormal', 'supernatural', 'fairy-tales', 'fairies',
                   'fairy-tale', 'fairytales', 'mythology']
        science_fiction = ['sci-fi', 'sci-fi', 'sf', 'scifi', 'time-travel', 'future', 'futuristic', 'sciencefiction']
        science_fiction_fantasy = ['fantasy-sci-fi', 'sci-fi-fantasy', 'fantasy-sci-fi', 'fantasy-science-fiction',
                                   'sf-fantasy', 'sci-fi-and-fantasy', 'science-fiction-fantasy',
                                   'science-fictions-and-fantasy',
                                   'fantasy-and-sci-fi', 'fantasy-sf', 'sf-f', 'scifi-fantasy', 'fantasy-scifi']
        history = ['world-history', 'wwii', 'ww2', 'historical', 'world-war-2', 'holocaust', 'world-war-ii', 'jewish',
                   'historic-fiction', 'medieval', 'historical-fiction']
        comics = ['graphic-novel-manga', 'manga', 'comic-manga', 'mangas', 'anime', 'graphic-novels-manga',
                  'manga-comics', 'comic', 'comics-manga', 'comic-books', 'manga-graphic-novels', 'comix', 'comic-book']
        crime = ['murder', 'serial-killer', 'murder-mystery', 'crime-fiction', 'detective', 'detectives',
                 'crime-mystery', 'mystery-detective', 'crime-and-mystery', 'krimi', 'spies', 'espionage',
                 'detective-fiction', 'spy',
                 'mystery-series', 'crime-thriller', 'mystery-crime', 'mystery']
        thriller = ['thriller-suspense', 'mystery-thrillers', 'mystery-thriller', 'suspense-thriller',
                    'mystery-suspense', 'thrillers', 'thriller-mystery', 'spy-thriller', 'psychological-thriller',
                    'mystery-thriller-suspense', 'suspense', 'mystery-suspense-thriller', 'suspense-mystery']
        self_development = ['self-development', 'personal-development', 'personal-growth', 'mental-health',
                            'development', 'self-improvement', 'inspiration', 'inspirational', 'self development']
        religion = ['christian-books', 'faith', 'theology', 'religion-spirituality', 'spiritual', 'christian',
                    'christianity', 'spirituality']
        romance = ['romance', 'romance-paranormal', 'fantasy-romance', 'erotic-romance', 'vampire-romance',
                   'love-triangles', 'love-triangle', 'love-stories', 'contemporary-romance', 'romance-contemporary',
                   'love-story', 'religious', 'romantic', 'paranormal-romance',
                   'erotica', 'erotic', 'romantic-suspense', 'historical-romance', 'love']
        horror = ['dark', 'horror-thriller', 'scary', 'aliens', 'gothic']
        lgbt = ['lgbtqia', 'lgbtq', 'queer']
        comedy = ['funny', 'humour', 'humorous', 'humor', 'fun']
        feminism = ['women', 'feminist']
        animals = ['animal-stories', 'animals', 'animal']
        chick_lit = ['chick-lit', 'chicklit', 'chic-lit']
        economy_politics = ['political', 'business', 'economics', 'politics']
        social_sciences = ['psychological', 'philosophical', 'sociology', 'social-science', 'psychology']
        dystopia = ['dystopian', 'dystopia', 'apocalyptic', 'apocalypse']
        travel = ['travel', 'survival', ]
        fiction = ['fiction', 'contemporary-fiction', 'epic', 'realistic']
        action = ['action', 'adventure', 'action-adventure']
        science = ['science''medicine', 'medical', 'health', 'educational']
        non_fiction = ['nonfiction', 'non-fiction']
        relationships = ['friendship', 'relationships', 'coming-of-age', 'family']
        novel = ['novel', 'novels']
        war = ['military', 'war']
        art = ['art', 'arts']
        classics = ['classics', 'classic-literature', 'classic']
        conditions = [
            (self.tags['tag_name'].isin(fantasy)), (self.tags['tag_name'].isin(science_fiction_fantasy)),
            (self.tags['tag_name'].isin(science_fiction)),
            (self.tags['tag_name'].isin(autobiography_biography_memoir)),
            (self.tags['tag_name'].isin(history)),
            (self.tags['tag_name'].isin(comics)),
            (self.tags['tag_name'].isin(crime)),
            (self.tags['tag_name'].isin(thriller)),
            (self.tags['tag_name'].isin(self_development)),
            (self.tags['tag_name'].isin(religion)),
            (self.tags['tag_name'].isin(romance)),
            (self.tags['tag_name'].isin(horror)),
            (self.tags['tag_name'].isin(lgbt)),
            (self.tags['tag_name'].isin(comedy)),
            (self.tags['tag_name'].isin(feminism)),
            (self.tags['tag_name'].isin(animals)),
            (self.tags['tag_name'].isin(chick_lit)),
            (self.tags['tag_name'].isin(economy_politics)),
            (self.tags['tag_name'].isin(social_sciences)),
            (self.tags['tag_name'].isin(dystopia)),
            (self.tags['tag_name'].isin(travel)),
            (self.tags['tag_name'].isin(fiction)),
            (self.tags['tag_name'].isin(action)),
            (self.tags['tag_name'].isin(science)),
            (self.tags['tag_name'].isin(non_fiction)),
            (self.tags['tag_name'].isin(relationships)),
            (self.tags['tag_name'].isin(novel)),
            (self.tags['tag_name'].isin(war)),
            (self.tags['tag_name'].isin(art)),
            (self.tags['tag_name'].isin(classics))

        ]
        choices = ['fantasy', 'fantasy/science-fiction', 'science-fiction', 'biography/autobiography/memoir', 'history',
                   'comics', 'crime', 'thriller', 'self development', 'religion', 'romance',
                   'horror', 'lgbt', 'comedy', 'feminism', 'animals', 'chick_lit', 'economy_politics',
                   'social_sciences', 'dystopia', 'travel', 'fiction', 'action', 'science', 'non_fiction',
                   'relationships', 'novel', 'war', 'art', 'classics'
                   ]
        self.tags['genre'] = np.select(conditions, choices, default=self.tags['tag_name'])
        self.book_tags = self.book_tags.merge(self.tags[['tag_id', 'tag_name', 'genre']], on='tag_id', how='left')
        self.book_tags = self.book_tags[~self.book_tags.genre.isna()]
        books_genres = self.book_tags.groupby(['goodreads_book_id', 'genre']).agg({'count': 'sum'})
        b.create_table_from_df(books_genres,'books_genres')
r=Recommender()
# r.create_genres()

