def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return '0s'

    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600

    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60

    hms = []
    if hours >= 1:
        hms.append(str(hours) + 'h')

    if minutes >= 1:
        hms.append(str(minutes) + 'm')

    if totalSeconds >= 1:
        hms.append(str(totalSeconds) + 's')

    return ' '.join(hms)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
