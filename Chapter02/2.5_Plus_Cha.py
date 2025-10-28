bite = int(input('바이트 단위 데이터: '))
megabite = bite // 1048576
bite = bite % 1048576
kilobite = bite // 1024
bite = bite % 1024
print(f'{megabite}MB {kilobite}KB {bite}B')