def from_package_import():
    from cal.ez import add
    res = add(1, 2)
    print(res)


def from_subpackage_import():
    from cal.ext.formater import format_string
    format_string('Falconluca')


if __name__ == '__main__':
    from_package_import()
    from_subpackage_import()

