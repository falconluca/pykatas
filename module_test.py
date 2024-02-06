def import_module():
    import module_luca
    module_luca.say('我操')
    module_luca.greet('Falconluca')

    say = module_luca.say
    say('卧槽')


def from_module_import():
    from module_luca import say, greet
    say('卧槽')
    greet('Falconluca')


def import_module_as():
    import module_luca as ts
    ts.say('卧槽')


if __name__ == '__main__':
    import_module()
    from_module_import()
    import_module_as()
