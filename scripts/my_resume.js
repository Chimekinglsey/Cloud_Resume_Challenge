$(document).ready(function(){
    $('nav a').click(function(){
        let target = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 800);
        return false;
    });

    $(window).scroll(function() {
        if ($(this).scrollTop() > $(window).height()) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });

    // Function to scroll to top when back-to-top button is clicked
    $('.back-to-top').click(function() {
        $('html, body').animate({scrollTop: 0}, 'slow');
        return false;
    });

    // update #visitorsCount from api
    let updateCount = () => {
        let url = "https://d7jvzrwts2.execute-api.us-east-1.amazonaws.com/Prod/views";
    
        $.ajax({
            method: 'GET',
            url: url,
            headers: {
                'Content-Type': 'application/json',
                // 'Access-Control-Allow-Origin': '*', // Required for CORS support to work
            },
            success: function(data) {
                let views = data['views']
                $('#visitorsCount').text(views);
                console.log(views)
            },
            error: function(err){
                console.log(err)
            }
        });
    };
    updateCount()
    });
