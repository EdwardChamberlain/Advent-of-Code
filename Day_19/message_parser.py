import re


def rec_resolve_rule(rule, rules, specials=True):
    if 'a' in rule or 'b' in rule:
        res = rule.strip('"')
        return f"({res})"

    elif rule.strip() == '42 | 42 8' and specials:
        return f'(({rec_resolve_rule(rules[42], rules)})+)'

    elif rule == '42 31 | 42 11 31' and specials:
        solv_42 = rec_resolve_rule(rules[42], rules)
        solv_31 = rec_resolve_rule(rules[31], rules)
        result = '|'.join([f'(({solv_42}){{{i}}}({solv_31}){{{i}}})' for i in range(1,3)])
        print(result)
        return f"({result})"

    else:
        ors = []
        for o in rule.split(' | '):
                result = [rec_resolve_rule(rules[int(i)], rules) for i in o.split(' ')]
                ors.append( f"({''.join(result)})" )
        return f"({'|'.join(ors)})"

def is_complient(string, regex):
    search_res = re.search(regex, string)
    if search_res:
        return len(search_res[0]) == len(string)
    else:
        return False