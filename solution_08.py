
def unique(chars):
    if len(chars) in [2, 4, 3, 7]:
        return 1
    return 0


def decode(encoded):
    enco = [''.join(sorted(e)) for e in encoded.split()]
    decoder = {}
    lens = [len(e) for e in enco]
    decoder[enco[lens.index(2)]] = '1'
    decoder[enco[lens.index(3)]] = '7'
    decoder[enco[lens.index(4)]] = '4'
    decoder[enco[lens.index(7)]] = '8'

    one = enco[lens.index(2)]
    four = enco[lens.index(4)]
    three = ''
    for e in enco:
        if len(e) == 5:
            if one[0] in e and one[1] in e:
                decoder[e] = '3'
                three = e
        elif len(e) == 6:
            if one[0] not in e or one[1] not in e:
                decoder[e] = '6'
    for e in enco:
        if len(e) == 6 and e not in decoder:
            if all([i in e for i in three]):
                decoder[e] = '9'
            else:
                decoder[e] = '0'
        elif len(e) == 5 and e not in decoder:
            if sum([i in e for i in four]) == 3:
                decoder[e] = '5'
            else:
                decoder[e] = '2'

    return decoder


def value(decoder, digits):
    return int(''.join([decoder[''.join(sorted(i))] for i in digits.split()]))


if __name__ == "__main__":

    digits = [i.split('|')[-1].strip()
              for i in open("input_08.txt").readlines()]
    total = 0
    for d in digits:
        nums = [n for n in d.split()]
        total += (sum([unique(n) for n in nums]))
    print("star 1:", total)

    encoded = [i.split('|')[0].strip()
               for i in open("input_08.txt").readlines()]
    total = 0

    for d, e in zip(digits, encoded):
        decoder = decode(e)
        total += value(decoder, d)
    print("star 2", total)
