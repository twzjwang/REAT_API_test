if __name__ == '__main__':
    requests = 0
    total_response_time = 0
    http_stat = {}
    with open('log') as log:
        for line in log:
            requests = requests + 1
            [http_code, response_time] = line.split(' ')
            if http_code in http_stat:
                http_stat[http_code] = http_stat[http_code] + 1
            else:
                http_stat[http_code] = 1
            total_response_time = total_response_time + float(response_time)
    print('requests  :\t'+str(requests))
    for key in http_stat:
        value = http_stat[key]
        print('"HTTP '+key+'":\t'+str(value)+'\t'+str(value/requests*100)+'%')
    print('mean time :\t'+str(total_response_time/requests)+' (ms)')
