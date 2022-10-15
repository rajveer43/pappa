//web scrap from https://www.freejobalert.com/police-defence-jobs/

var job = require('job');
var job = new job();

var url = "https://www.freejobalert.com/police-defence-jobs/";
var jobList = job.getJobList(url);
var jobList = jobList.slice(0, 10);
var jobList = jobList.map(function (job) {
    return job.title;
}
);
console.log(jobList);

