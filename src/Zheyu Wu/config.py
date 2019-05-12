dropcol = ['artist.id', 'artist.name','artist_mbtags',
           'artist_mbtags_count',
           'song.id','familiarity',
           'longitude','release.name','song.hotttnesss',
           'artist.id','year','release.id','terms', 'terms_freq',
            'title','location','latitude','mbtags_count',
           'country','similar','Unnamed: 0',
           'similar_hotness','hotness',
          'title_svd_3_10','title_svd_4_10',
          'y_fit_title','y_fit_release','y_fit_term']

mbtag = ['artist_mbtags',
 'artist_mbtags_count',
 'mbtags_count',
 'mbtag_0',
 'mbtag_1',
 'mbtag_2',
 'artist_mbtags.1',
 'artist_mbtags_count.1',
 'mbtags_count.1',
 'mbtag_0.1',
 'mbtag_1.1',
 'mbtag_2.1']

engineered = ['release.name_neu','release.name_pos','release.name_neg',
             'title_neg','title_neu', 'title_pos',
              'mbtag_0', 'mbtag_1', 'mbtag_2','artist_firstname',
              'artist_lastname','title_compound',
              'release.name_compound','similar_hotness']

augmented = ['artist_freq','grammy_relevance']

select= ['y_fit_release', 'y_fit_term', 'duration', 'loudness', 'artist_freq',
       'artist_firstname', 'y_fit_title', 'start_of_fade_out', 'tempo']
