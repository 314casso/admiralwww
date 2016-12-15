$(function() {
		
	function success(form) {
		var tablo = $('#success'); 
		tablo.show();
		tablo.html("<div class='alert alert-success'>");
        $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
        $('#success > .alert-success')
            .append("<strong>Ваше сообщение было успешно отправлено. </strong>");
        $('#success > .alert-success')
            .append('</div>');       
        form.trigger("reset");
        tablo.delay(5000).fadeOut();
	}
	
	function error(form) {
		var tablo = $('#success');
		tablo.show();
		tablo.html("<div class='alert alert-danger'>");
        $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
        $('#success > .alert-danger').append("<strong>Извините, в данный момент почтовый сервер недоступен. Попробуйте отправить сообщение позднее!");
        $('#success > .alert-danger').append('</div>');        
	} 
	
	function sendData($form) {		
		var d = {}
		$form.find('.form-control').each(function() {
			var el = $(this);
			d[el.attr("name")] = el.val();
		});	
        $.ajax({
            url: "/sendmail/",
            type: "POST",                                
            data: d,
            cache: false,
            tryCount : 0,
            retryLimit : 3,
            success: function() {
            	success($form);                    
            },
            error: function(xhr) {         	 
                this.tryCount++;
                if (this.tryCount <= this.retryLimit) {
                    $.ajax(this);
                    return;                    
                }          
                error($form);                
            },
        });
	}
	
	$.each([ 'sea', 'truck', 'train' ], function( index, value ) {		
		$("#form-" + value + "-shipping input, #form-" + value + "-shipping textarea").jqBootstrapValidation({
	        preventSubmit: true,
	        submitError: function($form, event, errors) {
	            
	        },
	        submitSuccess: function($form, event) {
	            event.preventDefault();
	            $("#modal-" + value + "-shipping").modal('toggle');          
	            sendData($form);          
	        },
	        filter: function() {
	            return $(this).is(":visible");
	        },
	    });		  
	});
	    
});