def str_replace(m):
    m = m.replace('C#', 'Q')
    m = m.replace('D#', 'W')
    m = m.replace('F#', 'R')
    m = m.replace('G#', 'T')
    m = m.replace('A#', 'Y')
    return m


def solution(m, musicinfos):
    answer = []

    m = str_replace(m)
    inx = 0
    for music in musicinfos:
        inx += 1
        music = music.split(',')
        start_time, end_time, title, codes = music[0], music[1], music[2], music[3]

        codes = str_replace(codes)
        music_len = len(codes)

        # 시간을 분단위로 쪼개기
        e_t = list(map(int, end_time.split(':')))
        endtime_min = e_t[0] * 60 + e_t[1]
        s_t = list(map(int, start_time.split(':')))
        startTime_min = s_t[0] * 60 + s_t[1]

        play_time = endtime_min - startTime_min

        # 재생된 음악 코드 이어붙이기
        total = codes * (play_time // music_len) + codes[:play_time % music_len]

        if m in total:
            answer.append([title, play_time, inx])

    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][0]
    else:
        answer = sorted(answer, key=lambda x: (-x[1], x[2]))
        return answer[0][0]