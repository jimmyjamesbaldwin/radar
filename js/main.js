function mapCalculation(){
    var jsonInput = '[{"room":"PG07","availability":"1"},{"room":"PG06","availability":"0"}]';
    var jsonParsed = $.parseJSON(jsonInput);

    $.each(jsonParsed, function() {
        console.log(this['room']);
        var currentRoom = '#' + this['room'];
        var currentRoomLabel = currentRoom + '-label';
        if(this['availability'] === '0'){
            $(currentRoom).css({ fill: "#A81C07"});
            $(currentRoomLabel).css('color', 'white'); //TODO fix text colour
        } else {
            $(currentRoom).css({ fill: "#77DD77"});
        }
    });
}
