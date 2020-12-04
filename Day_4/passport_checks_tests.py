import passport_checks

print(True == passport_checks.check_birth(str(2002)))
print(False == passport_checks.check_birth(str(2003)))

print(True == passport_checks.check_height('60in'))
print(True == passport_checks.check_height('190cm'))
print(False == passport_checks.check_height('190in'))
print(False == passport_checks.check_height('190'))

print(True == passport_checks.check_hair('#123abc'))
print(False == passport_checks.check_hair('#123abz'))
print(False == passport_checks.check_hair('123abc'))

print(True == passport_checks.check_eye('brn'))
print(False == passport_checks.check_eye('wat'))

print(True == passport_checks.check_id('000000001'))
print(False == passport_checks.check_id('0123456789'))
