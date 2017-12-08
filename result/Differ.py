'''
f = open('result.txt', 'r', errors='ignore')
f2 = open('700raw.txt', 'w')
i = 0
for line in f:
    f2.write(line)
    i = i + 1
    if i == 700:
        break
f.close()
f2.close()
'''
'''
f = open('700raw.txt', 'r', errors='ignore')
f2 = open('700differ.txt', 'w')
for line in f:
    i = 0
    #print(line)
    f3 = open('700result.txt', 'r', errors='ignore')
    for x in f3:
        #print(x)
        if x == line:
            #print(x)
            #print(line)
            i = 1
    if i == 0:
        f2.write(line)
f.close()
f2.close()
f3.close()
'''
import optparse
def differ(ID_file, resource, start, end):
    f = open(resource, 'r', errors='ignore')
    f2 = open('700result.txt', 'w')

    tem = ''
    for line in f:
        objects = line.split(':')
        if objects[0] == 'ASIN' and objects[1][1:] != tem:
            tem = objects[1][1:]
            f2.write(objects[1][1:])
    f.close()
    f2.close()

    f = open(ID_file, 'r', errors='ignore')
    f2 = open('700raw.txt', 'w')
    i = 1
    for line in f:
        if i >= start and i <= end:
            f2.write(line)
        i = i + 1
        if i > end:
            break
    f.close()
    f2.close()

    f = open('700raw.txt', 'r', errors='ignore')
    f2 = open('700differ.txt', 'w')
    for line in f:
        i = 0
        # print(line)
        f3 = open('700result.txt', 'r', errors='ignore')
        for x in f3:
            # print(x)
            if x == line:
                # print(x)
                # print(line)
                i = 1
        f3.close()
        if i == 0:
            f2.write(line)
    f.close()
    f2.close()


def main():
    parser = optparse.OptionParser('usage%prog -i <ID file> -r <resource file> -s <start line> -e <end_line>')
    parser.add_option('-i', dest='ID_file', type='string', help='specify path of ID file')
    parser.add_option('-r', dest='resource_file', type='string', help='specify path of resource file')
    parser.add_option('-s', dest='start_line', type='int', help='specify start line in ID file')
    parser.add_option('-e', dest='end_line', type='int', help='specify end line in ID file')
    (options, args) = parser.parse_args()
    ID_file = options.ID_file
    resource = options.resource_file
    start = options.start_line
    end = options.end_line
    differ(ID_file, resource, start, end)


if __name__ == '__main__':
    main()