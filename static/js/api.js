$(function(){
    
	$("form#team").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/team',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
    });
});

	$("form#fixture").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/fixture',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
    });


});

	$("form#result").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/result',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
    });


});

	$("form#award").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/award',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
    });


});

	$("form#scorer").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/scorer',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
    });


});

    $("form#player").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);

    $.ajax({
        url: 'http://localhost:5000/admin/add/player',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert('Operation success')
        },
        cache: false,
        contentType: false,
        processData: false
        
    });


});




});

// $(document).ready(function () {  
//      $("#submit_team").click(function () {  
                  
//          var name_ = $('#team_name').val();  
//          var email_ = $('#team_cat').val(); 
//          var password_ = $('#team_logo').val();

//                  $.ajax({  
//                      url: 'http://localhost:5000/register',  
//                      type: 'POST',  
//                      dataType: 'json',  
//                      data: {
//                      	name : name_,
//                      	email : email_,
//                      	password : password_
//                      },  
//                      success: function (data, textStatus, xhr) {  
//                          console.log(data);  
//                      },  
//                      error: function (xhr, textStatus, errorThrown) {  
//                          console.log('Error in Operation');  
//                      }  
//                  });  
//              });  
//          });  


