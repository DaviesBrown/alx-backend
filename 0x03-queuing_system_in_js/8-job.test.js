const chai = require("chai");
const mocha = require("mocha");
const expect = chai.expect;
import kue from 'kue';

import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518790',
    message: 'This is the code 1244 to verify your account'
    },
]

describe("createPushNotificationsJobs", () => {
    before(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });
    
    after(() => {
        queue.testMode.exit()
    });
    it("display a error message if jobs is not an array", () => {
        const list1 = ''
        expect(createPushNotificationsJobs(list1, queue)).throws(Error, "", "Jobs is not an array");
    });
    it("create two new jobs to the queue", () => {
        queue.createJob('pushNotificationJob', list[0]).save();
        queue.createJob('pushNotificationJob', list[1]).save();
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('pushNotificationJob');
        expect(queue.testMode.jobs[0].data).to.eql(list[0]);
    });
});
