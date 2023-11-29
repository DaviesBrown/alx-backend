import Kue from "kue";

const push_notification_code = Kue.createQueue();
const job = push_notification_code.create('push_notification_code', {
    phoneNumber: "0123456789",
    message: "notification",
});

job.on('complete', function() {
    console.log("Notification job completed");
}).on('enqueue', function(job_id) {
    console.log('Notification job created: ', job.id);
}).on('failed', function() {
    console.log('Job failed');
});

job.save((err) => {
    if (err) {
        console.log("Error creating job: ", err);
    }
});
