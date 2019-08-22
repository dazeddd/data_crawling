from bs4 import BeautifulSoup

html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

# col_names = {'국적': 'nation', '활동장르': 'act_genre', '데뷔': 'debut', '수상이력': 'award'}

soup = BeautifulSoup(html, 'html.parser')

dl = soup.find('dl')
dt_list = []
dd_list = []

for dts in dl:
    if not dts.name: continue
    
    if dts.name == 'dt':
        dt_list.append(dts.text)
    else:                                   # 'dd' 인경우
        span = dts.select_one('span')
        if span != None:
            dd_list.append(span.next.strip())
        else:
            dd_list.append(dts.text)


a = tuple(dt_list)
b = tuple(dd_list)
sql_insert = 'insert into Singer{} values{};'.format(a, b)
print(sql_insert)





