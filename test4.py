from bs4 import BeautifulSoup
import re
import time
import random

def parse(id, ASIN):
    soup = BeautifulSoup(open('xxx' + str(id) + '.txt', errors='ignore'), "lxml")
    ss = soup.select('#dv-center-features')
    if ss != []:
        #return
        sn = soup.select('#aiv-content-title')
        parse1(ss, sn, id, ASIN)
    else :
        ss = soup.select('#detail-bullets')
        sn = soup.select('#productTitle')
        if sn == []:
            print('333333333333333')
            f = open('zyj' + str(id) + '.txt', 'a', errors='ignore')
            f.write(ASIN)
            f.close()
            return
        parse2(ss, sn, id, ASIN)

def parse1(ss, sn, id, ASIN):
    genres = ['genres:']
    director = ['directors:']
    starring = ['starring:']
    supporting_actors = ['supporting actors:']
    studio = ['studio:']
    MPAA_rating = ['MPAA rating:']
    my_format = ['format:']
    captions_subtitles = ['captions and subtitles:']
    purchase_right = ['purchase right:']
    name = 'movie:'
    type = 'type:1'
    for block in sn:
        b = block.get_text().strip()
        name = name + b
    for block in ss:
        b = block.get_text()
        b1 = re.split(r'[ \n]+', b)
        p_last = ''
        while len(b1) != 0:
            s = ''
            p = b1.pop(0)
            while p != 'Genres' and p != 'Director' and p != 'Starring' and p != 'Studio' and p != 'MPAA' \
                    and p != 'Format' and p != 'Supporting' and p != 'MPAA' and p != 'Captions' and p != 'Purchase':
                if len(b1) == 0:
                    break
                elif p_last == 'Genres':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        genres.append(s[1:])
                        s = ''
                elif p_last == 'Director':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        director.append(s[1:])
                        s = ''
                elif p_last == 'Starring':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        starring.append(s[1:])
                        s = ''
                elif p_last == 'Studio':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        studio.append(s[1:])
                        s = ''
                elif p_last == 'Format':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        my_format.append(s[1:])
                        s = ''
                elif p_last == 'Supporting' or p_last == 'Supporting actors':
                    if p_last == 'Supporting' and p == 'actors':
                        p_last = p_last + ' ' + p
                    elif p_last == 'Supporting actors':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            supporting_actors.append(s[1:])
                            s = ''
                    else:
                        break
                elif p_last == 'MPAA' or p_last == 'MPAA rating':
                    if p_last == 'MPAA' and p == 'rating':
                        p_last = p_last + ' ' + p
                    elif p_last == 'MPAA rating':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            MPAA_rating.append(s[1:])
                            s = ''
                    else:
                        break
                elif p_last == 'Purchase' or p_last == 'Purchase rights':
                    if p_last == 'Purchase' and p == 'rights':
                        p_last = p_last + ' ' + p
                    elif p_last == 'Purchase rights':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            purchase_right.append(s[1:])
                            s = ''
                    else:
                        break
                elif p_last == 'Captions' or p_last == 'Captions and' or p_last == 'Captions and subtitles':
                    if p_last == 'Captions' and p == 'and':
                        p_last = p_last + ' ' + p
                    elif p_last == 'Captions and' and p == 'subtitles':
                        p_last = p_last + ' ' + p
                    elif p_last == 'Captions and subtitles':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            captions_subtitles.append(s[1:])
                            s = ''
                    else:
                        break

                p = b1.pop(0)
            if s != '' and p_last == 'Genres':
                genres.append(s[1:])
            elif s != '' and p_last == 'Starring':
                starring.append(s[1:])
            elif s != '' and p_last == 'Director':
                director.append(s[1:])
            elif s != '' and p_last == 'Studio':
                studio.append(s[1:])
            elif s != '' and p_last == 'Format':
                my_format.append(s[1:])
            elif s != '' and p_last == 'Supporting actors':
                supporting_actors.append(s[1:])
            elif s != '' and p_last == 'MPAA rating':
                MPAA_rating.append(s[1:])
            elif s != '' and p_last == 'Captions and subtitles':
                captions_subtitles.append(s[1:])
            elif s != '' and p_last == 'Purchase rights':
                purchase_right.append(s[1:])
            p_last = p


        try:
            fr = open('gst' + str(id) + '.txt', 'a', errors='ignore')
            fr.write(type)
            fr.write('\n')
            fr.write('ASIN: ' + ASIN)
            fr.write(name)
            fr.write('\n')
            fr.write(str(director))
            fr.write('\n')
            fr.write(str(starring))
            fr.write('\n')
            fr.write(str(supporting_actors))
            fr.write('\n')
            fr.write(str(studio))
            fr.write('\n')
            fr.write(str(MPAA_rating))
            fr.write('\n')
            fr.write(str(captions_subtitles))
            fr.write('\n')
            fr.write(str(purchase_right))
            fr.write('\n')
            fr.write(str(my_format))
            fr.write('\n')
            fr.write('\n')
            fr.close()
        except Exception as e:
            print(e)

def parse2(ss, sn, id, ASIN):
    director = ['directors:']
    starring = ['actors:']
    my_format = ['format:']
    writers = ['writers:']
    producers = ['producers:']
    subtitles = ['subtitles:']
    region = ['region:']
    number_of_discs = ['number of discs:']
    rated = ['rated:']
    studio = ['studio:']
    DVD_release_date = ['DVD release data:']
    run_time = ['run time:']
    language = ['language:']
    aspect_radio = ['aspect radio:']
    dubbed = ['dubbed:']
    vhs = ['vhs release date:']
    name = 'movie:'
    for block in sn:
        b = block.get_text().strip()
        name = name + b
    for block in ss:
        b = block.get_text()
        b1 = re.split(r'[ \n]+', b)
        p_last = ''
        while len(b1) != 0:
            s = ''
            p = b1.pop(0)
            while p != 'Writers:' and p != 'Directors:' and p != 'Actors:' and p != 'Producers:' \
                    and p != 'Format:' and p != 'Subtitles:' and p != 'Region:' and p != 'Number' \
                    and p != 'Rated:' and p != 'Studio:' and p != 'Run' and p != 'Language:' \
                    and p != 'Aspect' and p != 'Average' and p != 'ASIN' and p != 'Amazon' and p != 'DVD' \
                    and p != 'PLEASE' and p != 'Subtitles' and p != 'Dubbed:' and p != 'VHS':
                if len(b1) == 0:
                    break
                elif p_last == 'Directors:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        director.append(s[1:])
                        s = ''
                elif p_last == 'Actors:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        starring.append(s[1:])
                        s = ''
                elif p_last == 'Writers:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        writers.append(s[1:])
                        s = ''
                elif p_last == 'Producers:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        producers.append(s[1:])
                        s = ''
                elif p_last == 'Format:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        my_format.append(s[1:])
                        s = ''
                elif p_last == 'Subtitles:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        subtitles.append(s[1:])
                        s = ''
                elif p_last == 'Region:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        region.append(s[1:])
                        s = ''
                elif p_last == 'Number' or p_last == 'Number of' or p_last == 'Number of discs:':
                    if p_last == 'Number' and p == 'of':
                        p_last = p_last + ' ' + p
                    elif p_last == 'Number of' and p == 'discs:':
                        p_last = p_last + ' ' + p
                    elif p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        number_of_discs.append(s[1:])
                        s = ''
                elif p_last == 'Rated:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        rated.append(s[1:])
                        s = ''
                elif p_last == 'Studio:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        studio.append(s[1:])
                        s = ''
                elif p_last == 'Run' or p_last == 'Run Time:':
                    if p_last == 'Run' and p == 'Time:':
                        p_last = p_last + ' ' + p
                    elif p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        run_time.append(s[1:])
                        s = ''
                elif p_last == 'Language:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        language.append(s[1:])
                        s = ''
                elif p_last == 'Aspect' or p_last == 'Aspect Ratio:':
                    if p_last == 'Aspect' and p == 'Ratio:':
                        p_last = p_last + ' ' + p
                    elif p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        aspect_radio.append(s[1:])
                        s = ''
                elif p_last == 'DVD' or p_last == 'DVD Release' or p_last == 'DVD Release Date:':
                    if p_last == 'DVD' and p == 'Release':
                        p_last = p_last + ' ' + p
                    elif p_last == 'DVD Release' and p == 'Date:':
                        p_last = p_last + ' ' + p
                    elif p_last == 'DVD Release Date:':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            DVD_release_date.append(s[1:])
                            s = ''
                    else:
                        break
                elif p_last == 'VHS' or p_last == 'VHS Release' or p_last == 'VHS Release Date:':
                    if p_last == 'VHS' and p == 'Release':
                        p_last = p_last + ' ' + p
                    elif p_last == 'VHS Release' and p == 'Date:':
                        p_last = p_last + ' ' + p
                    elif p_last == 'VHS Release Date:':
                        if p[-1] != ',':
                            s = s + ' ' + p
                        else:
                            s = s + ' ' + p[:-1]
                            vhs.append(s[1:])
                            s = ''
                    else:
                        break
                elif p_last == 'Dubbed:':
                    if p[-1] != ',':
                        s = s + ' ' + p
                    else:
                        s = s + ' ' + p[:-1]
                        dubbed.append(s[1:])
                        s = ''
                p = b1.pop(0)
            if s != '' and p_last == 'Actors:':
                starring.append(s[1:])
            elif s != '' and p_last == 'Directors:':
                director.append(s[1:])
            elif s != '' and p_last == 'Writers:':
                writers.append(s[1:])
            elif s != '' and p_last == 'Producers:':
                producers.append(s[1:])
            elif s != '' and p_last == 'Format:':
                my_format.append(s[1:])
            elif s != '' and p_last == 'Subtitles:':
                subtitles.append(s[1:])
            elif s != '' and p_last == 'Region:':
                region.append(s[1:])
            elif s != '' and p_last == 'Number of discs:':
                number_of_discs.append(s[1:])
            elif s != '' and p_last == 'Rated:':
                rated.append(s[1:])
            elif s != '' and p_last == 'Studio:':
                studio.append(s[1:])
            elif s != '' and p_last == 'Run Time:':
                run_time.append(s[1:])
            elif s != '' and p_last == 'Language:':
                language.append(s[1:])
            elif s != '' and p_last == 'Aspect Ratio:':
                aspect_radio.append(s[1:])
            elif s != '' and p_last == 'DVD Release Date:':
                DVD_release_date.append(s[1:])
            elif s != '' and p_last == 'VHS Release Date:':
                vhs.append(s[1:])
            elif s != '' and p_last == 'Dubbed:':
                dubbed.append(s[1:])
            p_last = p

        try:
            fr = open('gst' + str(id) + '.txt', 'a', errors='ignore')
            fr.write('ASIN: ' + ASIN)
            fr.write(name)
            fr.write('\n')
            fr.write(str(director))
            fr.write('\n')
            fr.write(str(starring))
            fr.write('\n')
            fr.write(str(writers))
            fr.write('\n')
            fr.write(str(producers))
            fr.write('\n')
            fr.write(str(my_format))
            fr.write('\n')
            fr.write(str(subtitles))
            fr.write('\n')
            fr.write(str(region))
            fr.write('\n')
            fr.write(str(language))
            fr.write('\n')
            fr.write(str(number_of_discs))
            fr.write('\n')
            fr.write(str(rated))
            fr.write('\n')
            fr.write(str(studio))
            fr.write('\n')
            fr.write(str(run_time))
            fr.write('\n')
            fr.write(str(aspect_radio))
            fr.write('\n')
            fr.write(str(dubbed))
            fr.write('\n')
            fr.write(str(DVD_release_date))
            fr.write('\n')
            fr.write(str(vhs))
            fr.write('\n')
            fr.write('\n')
            fr.close()
        except Exception as e:
            print(e)
