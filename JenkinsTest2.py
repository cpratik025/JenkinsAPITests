import jenkinsapi

def jenkinsconn():
    server = jenkins.Jenkins('http://localhost:8080', username='pratik025', password='118c8df204629792403c6898be4c42ef0b')
    jobs = server.get_jobs()
    job_name_list = []
    build_number_list = []
    build_info_list = []
    status_list_dict = {}
    success = 0
    failure = 0
    unstable = 0
    aborted = 0
    # print dir(server)
    for i in range(len(jobs)):
        job_name = jobs[i]['name']
        job_name_list.append(job_name)
    for i in range(len(job_name_list)):
        job_info = server.get_job_info(job_name_list[i])
    lastbuilt = job_info['lastSuccessfulBuild']
    if lastbuilt:
        b_number = job_info['lastSuccessfulBuild']['number']
        build_number_list.append(b_number)



    build_zipped = zip(job_name_list, build_number_list)
    for i, j in build_zipped:
        success = 0
        failure = 0
        unstable = 0
        aborted = 0
        for k in range(j):
            build_info = server.get_build_info(i, k + 1)
            build_info_list.append(build_info)
            status = build_info['result']
            if status == "SUCCESS":
                success += 1
            elif status == "FAILURE":
                failure += 1
            elif status == "UNSTABLE":
                unstable += 1
            else:
                aborted += 1
            statuscount = [success, failure, unstable, aborted]
            status_list_dict[i] = statuscount
jenkinsconn()
