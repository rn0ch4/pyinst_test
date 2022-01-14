import sys
import yara


def main(fpath_rule, fpath_target):
    rule = yara.compile(source=open(fpath_rule).read())
    content = open(fpath_target, 'rb').read()
    matches = rule.match(data=content)
    print(matches)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('{} <RULE> <TARGET>'.format(sys.argv[0]))
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2])
