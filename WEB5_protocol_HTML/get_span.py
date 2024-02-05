def span(envelope):
    a = abs(float(envelope['lowerCorner'].split()[0]) - float(envelope['upperCorner'].split()[0])) / 2.0
    b = abs(float(envelope['lowerCorner'].split()[1]) - float(envelope['upperCorner'].split()[1])) / 2.0
    return f'{a},{b}'