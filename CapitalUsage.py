def capital_usage(s):
    rules = [lambda s: all(x.isupper() for x in s),  
        lambda s: all(x.islower() for x in s),
        lambda x: (0 and x.isupper() for x in s )
        ]
    if any(rule(s) for rule in rules):
        return True
    else:
        return False
st = "Google"
print(capital_usage(st))
    