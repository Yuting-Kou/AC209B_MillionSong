dropcol = ['artist.id', 'artist.name','artist_mbtags',
           'artist_mbtags_count',
           'song.id',#'familiarity',
           'longitude','release.name','song.hotttnesss',
           'artist.id','year','release.id','terms', #'terms_freq',
            'title','location','latitude', #'mbtags_count',
           'country','similar','Youtube_Hotness', #'Unnamed: 0.1','Unnamed: 0',
           'similar_hotness',
          #'title_svd_3_10','title_svd_4_10',
          #'y_fit_title','y_fit_release','y_fit_term', # 'bars_confidence', 'beats_confidence', 
          #'key_confidence', 'mode_confidence', 'tatums_confidence', 'time_signature_confidence',
          'mbtag_0', 'mbtag_1', 'mbtag_2']

mbtag = ['artist_mbtags',
 'artist_mbtags_count',
 'mbtags_count',
 'mbtag_0',
 'mbtag_1',
 'mbtag_2']

raw_data_col = ['Youtube_Hotness', 'artist.hotttnesss', 
       'bars_confidence', 'bars_start',
       'beats_confidence', 'beats_start', 'duration', 'end_of_fade_in',
       'familiarity', 'key', 'key_confidence','loudness', 'mode', 'mode_confidence', 
       'start_of_fade_out', 'tatums_confidence', 'tatums_start', 'tempo',
       'terms_freq', 'time_signature', 'time_signature_confidence',
        'decade', 'artist_firstname', 'artist_lastname',
       'mbtags_count']

engineered = ['release.name_neu','release.name_pos','release.name_neg',
             'title_neg','title_neu', 'title_pos',
              'mbtag_0', 'mbtag_1', 'mbtag_2','artist_firstname',
              'artist_lastname','title_compound',
              'release.name_compound','similar_hotness']

augmented = ['artist_freq','grammy_relevance']

select= ['y_fit_release', 'y_fit_term', 'duration', 'loudness', 'artist_freq',
       'artist_firstname', 'y_fit_title', 'start_of_fade_out', 'tempo']
