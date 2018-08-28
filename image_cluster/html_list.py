anchor_dict = {\
'은평': 'ws_ep', '마포': 'ws_mp', '서대문': 'ws_sdm', '강서': 'sw_gs',\
'양천': 'sw_yc', '영등포': 'sw_ydp', '구로': 'sw_gr', '종로': 'cs_jr',\
'중구': 'cs_jg', '용산': 'cs_ys', '동작': 'ss_dj', '관악': 'ss_ga',\
'금천': 'ss_gc', '서초': 'gn_sc', '강남': 'gn_gn', '도봉': 'gb_db',\
'강북': 'gb_gb', '성북': 'gb_sb', '노원': 'gb_nw', '동대문': 'es_ddm',\
'중랑': 'es_gl', '성동': 'es_sd', '광진': 'es_gj', '강동': 'se_gd', '송파': 'se_sp'}

html_anchors = ''
for area, path in anchor_dict.items():
    html_anchors += f'<a href="#{area}">{path} </a>'

area_names = {'ws' : ['ep', 'mp', 'sdm'],
              'sw' : ['gs', 'yc', 'ydp', 'gr'],
              'cs' : ['jr', 'jg', 'ys'],
              'ss' : ['dj', 'ga', 'gc'],
              'gn' : ['sc', 'gn'],
              'gb' : ['db', 'gb', 'sb', 'nw'],
              'es' : ['ddm', 'gl', 'sd', 'gj'],
              'se' : ['gd', 'sp']
             }

eng_path_list = [f'{k}_{v}_{i:02}.png'
            for k in area_names.keys()
            for v in area_names[k]
            for i in range(1,14)]

# html_image_list = '<p>'
# for path in path_list:
#     html_image_list += f'<img src=\"cafe_color_result/{path}.png\"> |'
# html_image_list += '</p>'

kor_area_names = {
            '서서울' : ['은평구', '마포구', '서대문구'],
            '서남' : ['강서', '영천', '영등포', '구로'],
            '도심' : ['종로', '중구', '용산'],
            '남서울' : ['동작', '관악', '금천'],
            '강북' : ['도봉', '강북', '성북', '노원'],
            '동서울' : ['동대문', '중랑', '성동구', '광진'],
            '동남' : ['강동', '송파']
            }
kor_area = sorted(kor_area_names.values())
print(kor_area)


kor_area = '강동구 강북구 강서구 관악구 광진구 구로구 금천구 노원구 도봉구 \
동대문구 동작구 마포구 서대문구 성동구 성북구 송파구 영등포구 영천구 \
용산구 은평구 종로구 중구 중랑구'.split(' ')

# kor_path_list = [f'{k} {v}'
#             for k in kor_area_names.keys()
#             for v in kor_area_names[k]
#             for i in range(1,14)]
