$(document).ready(function () {
    $.ajax({
        url: '/static/data.json',
        dataType: 'json',
        type: 'get',
        success: function (data) {
            var sensor1 = {id: data.sensors[0]['id'], distance: data.sensors[0]['distance']};
            var sensor2 = {id: data.sensors[1]['id'], distance: data.sensors[1]['distance']};
            var sensor3 = {id: data.sensors[2]['id'], distance: data.sensors[2]['distance']};

            if (sensor1.distance < 20) {
                $('#sens' + sensor1.id).css("background-color", "red");
                $('#sensor' + sensor1.id).text('Distance of sensor ' + sensor1.id + " is: " + sensor1.distance + "m.");
            } else {
                $('#sens' + sensor1.id).css("background-color", "green");
                $('#sensor' + sensor1.id).text('Distance of sensor ' + sensor1.id + " is: " + sensor1.distance);

            }

            if (sensor2.distance < 20) {
                $('#sens' + sensor2.id).css("background-color", "red");
                $('#sensor' + sensor2.id).text('Distance of sensor ' + sensor2.id + " is: " + sensor2.distance);

            } else {
                $('#sens' + sensor2.id).css("background-color", "green");
                $('#sensor' + sensor2.id).text('Distance of sensor ' + sensor2.id + " is: " + sensor2.distance);

            }

            if (sensor3.distance < 20) {
                $('#sens' + sensor3.id).css("background-color", "red");
                $('#sensor' + sensor3.id).text('Distance of sensor ' + sensor3.id + " is: " + sensor3.distance);

            } else {
                $('#sens' + sensor3.id).css("background-color", "green");
                $('#sensor' + sensor3.id).text('Distance of sensor ' + sensor3.id + " is: " + sensor3.distance);

            }

        }
    });
});


$(document).ready(function () {
    $('.writerButton').on('click', function () {

        var state = $(this).attr('ready');

        if (state === "true") {
            req = $.ajax({
                url: '/begin',
                type: 'POST',
                data: {'success': 'yes'}
            });

            $('.writerButton').attr('ready', 'false');
        }
    });
});

function guiUpdater() {
    $.ajax({
        url: '/static/data.json',
        dataType: 'json',
        type: 'get',
        cache: false,
        success: function (data) {
            var sensor1 = {id: data.sensors[0]['id'], distance: data.sensors[0]['distance']};
            var sensor2 = {id: data.sensors[1]['id'], distance: data.sensors[1]['distance']};
            var sensor3 = {id: data.sensors[2]['id'], distance: data.sensors[2]['distance']};
            //Debugging purposes
            console.log(sensor1);
            console.log(sensor2);
            console.log(sensor3);


            if (sensor1.distance < 20.0) {
                $('#sens' + sensor1.id).css("background-color", "red");
                $('#sensor' + sensor1.id).text('You are too close to Sensor  ' + sensor1.id + " Distance is: " + sensor1.distance + " cm, Please drive Carefully");
            } else {
                $('#sens' + sensor1.id).css("background-color", "green");
                $('#sensor' + sensor1.id).text('Distance of sensor ' + sensor1.id + " is: " + sensor1.distance + " cm");
            }

            if (sensor2.distance < 20.0) {
                $('#sens' + sensor2.id).css("background-color", "red");
                $('#sensor' + sensor2.id).text('You are too close to Sensor ' + sensor2.id + " Distance is: " + sensor2.distance + " cm, Please drive Carefully");

            } else {
                $('#sens' + sensor2.id).css("background-color", "green");
                $('#sensor' + sensor2.id).text('Distance of sensor ' + sensor2.id + " is: " + sensor2.distance + " cm");
            }

            if (sensor3.distance < 20.0) {
                $('#sens' + sensor3.id).css("background-color", "red");
                $('#sensor' + sensor3.id).text('You are too close to Sensor ' + sensor3.id + " Distance is: " + sensor3.distance + " cm, Please drive Carefully");

            } else {
                $('#sens' + sensor3.id).css("background-color", "green");
                $('#sensor' + sensor3.id).text('Distance of sensor ' + sensor3.id + " is: " + sensor3.distance + " cm");

            }

            if (sensor3.distance < 20.0 || sensor2.distance< 20.0 || sensor1.distance< 20.0) {
                var obj = document.createElement("audio");
                obj.src = "/static/Beep.mp3";
                obj.volume = 0.1;
                obj.autoPlay = false;
                obj.preLoad = true;
                obj.controls = true;

                obj.play();
            }

        }
    });
}
