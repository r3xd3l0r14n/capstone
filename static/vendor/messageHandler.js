    function messageHandler(e){
        json = JSON.parse(e);
        if (!(json[0] instanceof Array))
            json = [json];

        for(var i =0; i < json.length; i++){
            var args = json[i];
            var cmd = json[i][0]
            switch(cmd){
                case("handshake"):
                    $("#connect").addClass("active")
                    $("#result").text("Connected User: " + args[1]);
                    $("#card-table").show()
                    playerID = args[2];
                    break
                case("p_joined"):
                    var id = args[1];
                    var name = args[2];
                    addPlayer(id, name);

                    if(id == playerID){
                        $("a#join").css("visibility", "hidden")
                    }
                    break;
                case("disconnect"):
                    $("#connect").classList.remove("active")
                    $("#result").text("Disconnected")
                    $("#card-table").hide()
                    break;
            }
        }
    }

    function addPlayer(id, name){
        $("#active-players").append('<div id="player' + id +'">'
                                    + '<div class="name">'+name+'</div>');
    }